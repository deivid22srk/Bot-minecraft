import google.generativeai as genai
import json
import logging

logger = logging.getLogger(__name__)

class GeminiHandler:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
        self.system_prompt = """Você é uma IA que controla um bot no Minecraft Bedrock.
Seu objetivo é interpretar comandos dos jogadores e retornar ações estruturadas em JSON.

Ações disponíveis:
- goto_player: vai até um jogador específico
- collect_blocks: coleta blocos específicos (madeira, pedra, etc)
- give_items: entrega itens ao jogador
- chat: envia mensagem no chat
- follow_player: segue um jogador
- stop: para todas as ações

Exemplos:
Comando: "venha ate mim"
Resposta: {"action": "goto_player", "response": "Indo até você!"}

Comando: "pegue madeira pra mim e me entregue"
Resposta: {"action": "collect_and_give", "block_type": "wood", "quantity": 10, "response": "Vou coletar madeira e entregar para você!"}

Comando: "me siga"
Resposta: {"action": "follow_player", "response": "Vou seguir você!"}

SEMPRE responda em JSON válido com os campos 'action' e 'response'.
"""

    async def process_command(self, player_name, command_text):
        try:
            prompt = f"{self.system_prompt}\n\nJogador: {player_name}\nComando: {command_text}\n\nResposta JSON:"
            
            response = await asyncio.to_thread(
                self.model.generate_content,
                prompt
            )
            
            response_text = response.text.strip()
            
            if response_text.startswith('```json'):
                response_text = response_text[7:-3].strip()
            elif response_text.startswith('```'):
                response_text = response_text[3:-3].strip()
            
            action_data = json.loads(response_text)
            action_data['player'] = player_name
            
            logger.info(f"Gemini processou comando de {player_name}: {action_data}")
            return action_data
            
        except json.JSONDecodeError as e:
            logger.error(f"Erro ao decodificar resposta do Gemini: {e}")
            return {
                "action": "chat",
                "response": "Desculpe, não consegui processar esse comando.",
                "player": player_name
            }
        except Exception as e:
            logger.error(f"Erro no Gemini: {e}")
            return {
                "action": "chat",
                "response": "Ocorreu um erro ao processar seu comando.",
                "player": player_name
            }

import asyncio
