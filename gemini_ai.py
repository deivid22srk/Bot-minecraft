import google.generativeai as genai
import json
import logging

class GeminiAI:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
    async def process_command(self, command, context):
        prompt = f"""Você é um assistente que controla um bot no Minecraft Bedrock. 
Analise o comando do jogador e retorne um JSON com a ação a ser executada.

Contexto do bot:
- Posição atual: x={context.get('botPosition', {}).get('x', 0)}, y={context.get('botPosition', {}).get('y', 0)}, z={context.get('botPosition', {}).get('z', 0)}
- Jogador: {context.get('playerName', 'Desconhecido')}
- Posição do jogador: x={context.get('playerPosition', {}).get('x', 0)}, y={context.get('playerPosition', {}).get('y', 0)}, z={context.get('playerPosition', {}).get('z', 0)}

Comando do jogador: "{command}"

Ações disponíveis:
1. "goto" - ir até o jogador
2. "mine" - minerar um recurso específico
3. "give" - entregar itens ao jogador
4. "follow" - seguir o jogador
5. "stop" - parar de seguir
6. "respond" - apenas responder ao jogador

Retorne APENAS um JSON no seguinte formato (sem markdown, sem explicação):
{{
  "action": "nome_da_ação",
  "target": "recurso ou alvo (se aplicável)",
  "quantity": número (se aplicável),
  "response": "mensagem amigável para o jogador em português"
}}

Exemplos:
- "venha até mim" -> {{"action": "goto", "response": "Estou indo até você!"}}
- "pegue 10 madeiras" -> {{"action": "mine", "target": "oak_log", "quantity": 10, "response": "Vou buscar 10 madeiras para você!"}}
- "me entregue madeira" -> {{"action": "give", "target": "oak_log", "response": "Entregando a madeira!"}}
- "me siga" -> {{"action": "follow", "response": "Seguindo você agora!"}}
- "olá" -> {{"action": "respond", "response": "Olá! Como posso ajudar?"}}"""

        try:
            response = self.model.generate_content(prompt)
            text = response.text.strip()
            
            # Extrair JSON do texto
            start = text.find('{')
            end = text.rfind('}') + 1
            if start != -1 and end > start:
                json_text = text[start:end]
                parsed = json.loads(json_text)
                return parsed
            
            return {
                'action': 'respond',
                'response': 'Desculpe, não entendi o comando. Pode repetir?'
            }
        except Exception as e:
            logging.error(f"Erro ao processar comando com Gemini: {e}")
            return {
                'action': 'respond',
                'response': 'Desculpe, tive um problema ao processar seu comando.'
            }
