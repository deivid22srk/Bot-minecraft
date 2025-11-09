import { GoogleGenerativeAI } from '@google/generative-ai';

export class GeminiAI {
  constructor(apiKey) {
    this.genAI = new GoogleGenerativeAI(apiKey);
    this.model = this.genAI.getGenerativeModel({ model: 'gemini-1.5-flash' });
  }

  async processCommand(command, context) {
    const prompt = `Você é um assistente que controla um bot no Minecraft Bedrock. 
Analise o comando do jogador e retorne um JSON com a ação a ser executada.

Contexto do bot:
- Posição atual: x=${context.botPosition?.x || 0}, y=${context.botPosition?.y || 0}, z=${context.botPosition?.z || 0}
- Jogador: ${context.playerName}
- Posição do jogador: x=${context.playerPosition?.x || 0}, y=${context.playerPosition?.y || 0}, z=${context.playerPosition?.z || 0}

Comando do jogador: "${command}"

Ações disponíveis:
1. "goto" - ir até o jogador
2. "mine" - minerar um recurso específico
3. "give" - entregar itens ao jogador
4. "follow" - seguir o jogador
5. "stop" - parar de seguir
6. "respond" - apenas responder ao jogador

Retorne APENAS um JSON no seguinte formato (sem markdown, sem explicação):
{
  "action": "nome_da_ação",
  "target": "recurso ou alvo (se aplicável)",
  "quantity": número (se aplicável),
  "response": "mensagem amigável para o jogador em português"
}

Exemplos:
- "venha até mim" -> {"action": "goto", "response": "Estou indo até você!"}
- "pegue 10 madeiras" -> {"action": "mine", "target": "oak_log", "quantity": 10, "response": "Vou buscar 10 madeiras para você!"}
- "me entregue madeira" -> {"action": "give", "target": "oak_log", "response": "Entregando a madeira!"}
- "me siga" -> {"action": "follow", "response": "Seguindo você agora!"}
- "olá" -> {"action": "respond", "response": "Olá! Como posso ajudar?"}`;

    try {
      const result = await this.model.generateContent(prompt);
      const response = result.response;
      const text = response.text().trim();
      
      const jsonMatch = text.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        const parsed = JSON.parse(jsonMatch[0]);
        return parsed;
      }
      
      return {
        action: 'respond',
        response: 'Desculpe, não entendi o comando. Pode repetir?'
      };
    } catch (error) {
      console.error('Erro ao processar comando com Gemini:', error);
      return {
        action: 'respond',
        response: 'Desculpe, tive um problema ao processar seu comando.'
      };
    }
  }
}
