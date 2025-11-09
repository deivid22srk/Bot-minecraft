import asyncio
import logging
from bedrock_connection import BedrockConnection
from bot_actions import BotActions

logger = logging.getLogger(__name__)

class MinecraftBot:
    def __init__(self, config, gemini_handler):
        self.config = config
        self.gemini = gemini_handler
        self.bot_name = config['bot_name']
        self.command_prefix = config['command_prefix']
        
        self.connection = BedrockConnection(
            config['server']['host'],
            config['server']['port'],
            self.bot_name
        )
        
        self.actions = BotActions(self.connection)
        self.running = False
        self.players = {}
        
    async def start(self):
        logger.info(f"Conectando ao servidor {self.config['server']['host']}:{self.config['server']['port']}...")
        
        await self.connection.connect()
        self.running = True
        
        self.connection.on_chat_message(self.handle_chat_message)
        self.connection.on_player_position(self.handle_player_position)
        
        logger.info(f"{self.bot_name} conectado com sucesso!")
        
        await self.connection.send_chat(f"Olá! Sou o {self.bot_name}. Use {self.command_prefix} para me dar comandos!")
        
        while self.running:
            await self.connection.update()
            await asyncio.sleep(0.05)
    
    async def stop(self):
        logger.info("Desconectando bot...")
        self.running = False
        await self.connection.disconnect()
        
    async def handle_chat_message(self, player_name, message):
        if player_name == self.bot_name:
            return
        
        if not message.startswith(self.command_prefix):
            return
        
        command = message[len(self.command_prefix):].strip()
        
        if not command:
            return
        
        logger.info(f"Comando recebido de {player_name}: {command}")
        
        await self.connection.send_chat(f"Processando comando...")
        
        action_data = await self.gemini.process_command(player_name, command)
        
        await self.execute_action(action_data)
    
    async def handle_player_position(self, player_name, position):
        self.players[player_name] = position
    
    async def execute_action(self, action_data):
        action = action_data.get('action')
        player = action_data.get('player')
        response = action_data.get('response', '')
        
        if response:
            await self.connection.send_chat(response)
        
        try:
            if action == 'goto_player':
                await self.actions.goto_player(player)
                
            elif action == 'collect_and_give':
                block_type = action_data.get('block_type', 'wood')
                quantity = action_data.get('quantity', 10)
                await self.actions.collect_blocks(block_type, quantity)
                await self.actions.goto_player(player)
                await self.actions.give_items(player, block_type, quantity)
                await self.connection.send_chat(f"Entreguei {quantity} {block_type} para {player}!")
                
            elif action == 'follow_player':
                await self.actions.follow_player(player)
                
            elif action == 'stop':
                await self.actions.stop_all()
                
            elif action == 'chat':
                pass
                
            else:
                logger.warning(f"Ação desconhecida: {action}")
                
        except Exception as e:
            logger.error(f"Erro ao executar ação {action}: {e}")
            await self.connection.send_chat(f"Desculpe, ocorreu um erro ao executar a ação.")
