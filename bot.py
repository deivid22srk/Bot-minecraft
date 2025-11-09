#!/usr/bin/env python3
import asyncio
import json
import logging
import signal
import sys
from pathlib import Path

from gemini_ai import GeminiAI
from bedrock_client import BedrockClient

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)

class MinecraftBot:
    def __init__(self, config_path='config.json'):
        # Carregar configuração
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        
        # Inicializar componentes
        self.gemini = GeminiAI(self.config['gemini']['apiKey'])
        self.client = BedrockClient(
            self.config['server']['host'],
            self.config['server']['port'],
            self.config['botName']
        )
        
        self.command_prefix = self.config['commandPrefix']
        self.is_processing = False
        
        # Adicionar handler de mensagens
        self.client.add_message_handler(self.handle_message)
    
    async def handle_message(self, player_name, message):
        """Processar mensagem recebida"""
        if not message.startswith(self.command_prefix):
            return
        
        if self.is_processing:
            await self.client.send_chat("Aguarde, ainda estou processando o comando anterior!")
            return
        
        # Extrair comando
        command = message[len(self.command_prefix):].strip()
        if not command:
            return
        
        self.is_processing = True
        logging.info(f"🤖 Processando comando de {player_name}: '{command}'")
        
        try:
            # Processar com Gemini
            context = {
                'botPosition': self.client.position,
                'playerName': player_name,
                'playerPosition': self.client.players.get(player_name, {}).get('position', {'x': 0, 'y': 0, 'z': 0})
            }
            
            action_data = await self.gemini.process_command(command, context)
            logging.info(f"🧠 Gemini respondeu: {json.dumps(action_data, ensure_ascii=False, indent=2)}")
            
            # Executar ação
            await self.execute_action(action_data, player_name)
            
        except Exception as e:
            logging.error(f"❌ Erro ao executar comando: {e}")
            await self.client.send_chat("Desculpe, tive um erro ao processar seu comando.")
        finally:
            self.is_processing = False
    
    async def execute_action(self, action_data, player_name):
        """Executar ação baseada na resposta do Gemini"""
        action = action_data.get('action')
        response = action_data.get('response', '')
        
        # Enviar resposta
        if response:
            await self.client.send_chat(response)
        
        # Executar ação específica
        if action == 'goto':
            await self.goto_player(player_name)
        elif action == 'mine':
            target = action_data.get('target')
            quantity = action_data.get('quantity', 1)
            await self.mine_resource(target, quantity)
        elif action == 'give':
            target = action_data.get('target')
            quantity = action_data.get('quantity', 1)
            await self.give_items(player_name, target, quantity)
        elif action == 'follow':
            await self.follow_player(player_name)
        elif action == 'stop':
            await self.stop_following()
        elif action == 'respond':
            pass  # Apenas resposta, nenhuma ação adicional
    
    async def goto_player(self, player_name):
        """Ir até o jogador"""
        logging.info(f"🚶 Indo até {player_name}...")
        await asyncio.sleep(2)  # Simular movimento
        await self.client.send_chat("Cheguei!")
    
    async def mine_resource(self, resource, quantity):
        """Minerar recurso"""
        logging.info(f"⛏️ Minerando {quantity}x {resource}...")
        await asyncio.sleep(3)  # Simular mineração
        await self.client.send_chat(f"Coletei {quantity}x {resource}!")
    
    async def give_items(self, player_name, item, quantity):
        """Entregar itens ao jogador"""
        logging.info(f"🎁 Entregando {quantity}x {item} para {player_name}...")
        await asyncio.sleep(1)
        await self.client.send_chat(f"Aqui está! {quantity}x {item}")
    
    async def follow_player(self, player_name):
        """Seguir jogador"""
        logging.info(f"👣 Seguindo {player_name}...")
        await self.client.send_chat("Estou seguindo você!")
    
    async def stop_following(self):
        """Parar de seguir"""
        logging.info("🛑 Parando de seguir...")
        await self.client.send_chat("Ok, parei!")
    
    async def run(self):
        """Iniciar o bot"""
        # Conectar ao servidor
        connected = await self.client.connect()
        
        if not connected:
            logging.error("❌ Falha ao conectar. Tentando novamente em 10s...")
            await asyncio.sleep(10)
            return await self.run()
        
        logging.info(f"📍 Aguardando comandos com o prefixo: {self.command_prefix}")
        
        # Manter bot rodando
        try:
            while self.client.running:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            logging.info("\n👋 Encerrando bot...")
            self.client.disconnect()
    
    def stop(self):
        """Parar o bot"""
        self.client.disconnect()

# Instância global do bot
bot = None

def signal_handler(sig, frame):
    """Handler para Ctrl+C"""
    if bot:
        bot.stop()
    sys.exit(0)

async def main():
    global bot
    
    print("╔════════════════════════════════════════╗")
    print("║     Bot Hailgames - Minecraft Bot     ║")
    print("║         Powered by Gemini AI          ║")
    print("╚════════════════════════════════════════╝")
    print()
    
    # Configurar handler de sinais
    signal.signal(signal.SIGINT, signal_handler)
    
    # Criar e iniciar bot
    bot = MinecraftBot()
    await bot.run()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Encerrando bot...")
    except Exception as e:
        logging.error(f"❌ Erro fatal: {e}")
        sys.exit(1)
