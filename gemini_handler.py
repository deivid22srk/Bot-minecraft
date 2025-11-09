import requests
import json
import logging
import asyncio

logger = logging.getLogger(__name__)

class GeminiHandler:
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"
        
        self.system_prompt = """Você é uma IA que controla um bot no Minecraft Bedrock.
Seu objetivo é interpretar comandos dos jogadores e retornar ações estruturadas em JSON.

Ações disponíveis:
- goto_player: vai até um jogador específico
- collect_blocks: coleta blocos específicos (madeira, pedra, etc)
- give_items: entrega itens ao jogador
- chat: envia mensagem no chat
- follow_player: segue um jogador
- stop: para todas as ações
- collect_and_give: coleta blocos e entrega ao jogador

Exemplos:
Comando: "venha ate mim"
Resposta: {"action": "goto_player", "response": "Indo até você!"}

Comando: "pegue madeira pra mim e me entregue"
Resposta: {"action": "collect_and_give", "block_type": "wood", "quantity": 10, "response": "Vou coletar madeira e entregar para você!"}

Comando: "me siga"
Resposta: {"action": "follow_player", "response": "Vou seguir você!"}

Comando: "pare"
Resposta: {"action": "stop", "response": "Parado!"}

SEMPRE responda APENAS com JSON válido com os campos 'action' e 'response'.
NÃO adicione texto antes ou depois do JSON.
"""

    async def process_command(self, player_name, command_text):
        try:
            prompt = f"{self.system_prompt}\n\nJogador: {player_name}\nComando: {command_text}\n\nResposta JSON:"
            
            payload = {
                "contents": [{
                    "parts": [{
                        "text": prompt
                    }]
                }],
                "generationConfig": {
                    "temperature": 0.7,
                    "maxOutputTokens": 256
                }
            }
            
            response = await asyncio.to_thread(
                requests.post,
                self.api_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=10
            )
            
            if response.status_code != 200:
                logger.error(f"Erro na API Gemini: {response.status_code} - {response.text}")
                return {
                    "action": "chat",
                    "response": "Desculpe, não consegui processar esse comando.",
                    "player": player_name
                }
            
            result = response.json()
            
            if "candidates" not in result or len(result["candidates"]) == 0:
                logger.error("Resposta vazia do Gemini")
                return {
                    "action": "chat",
                    "response": "Desculpe, não consegui processar esse comando.",
                    "player": player_name
                }
            
            response_text = result["candidates"][0]["content"]["parts"][0]["text"].strip()
            
            if response_text.startswith('```json'):
                response_text = response_text[7:-3].strip()
            elif response_text.startswith('```'):
                response_text = response_text[3:-3].strip()
            
            response_text = response_text.replace('`', '').strip()
            
            action_data = json.loads(response_text)
            action_data['player'] = player_name
            
            logger.info(f"Gemini processou comando de {player_name}: {action_data}")
            return action_data
            
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao decodificar resposta do Gemini: {e}")
            logger.error(f"Resposta recebida: {response_text if 'response_text' in locals() else 'N/A'}")
            return {
                "action": "chat",
                "response": "Desculpe, não consegui processar esse comando.",
                "player": player_name
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Erro de conexão com Gemini: {e}")
            return {
                "action": "chat",
                "response": "Erro ao conectar com IA. Tente novamente.",
                "player": player_name
            }
        except Exception as e:
            logger.error(f"Erro no Gemini: {e}")
            return {
                "action": "chat",
                "response": "Ocorreu um erro ao processar seu comando.",
                "player": player_name
            }
