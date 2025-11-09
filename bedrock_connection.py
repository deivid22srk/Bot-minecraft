import asyncio
import logging
from typing import Callable, Optional
import websocket
import json
import time

logger = logging.getLogger(__name__)

class BedrockConnection:
    def __init__(self, host: str, port: int, username: str):
        self.host = host
        self.port = port
        self.username = username
        
        self.ws = None
        self.connected = False
        
        self.position = {'x': 0, 'y': 0, 'z': 0}
        self.health = 20
        self.inventory = {}
        
        self.chat_callback = None
        self.position_callback = None
        
        self.packet_queue = asyncio.Queue()
        self.running = False
        
    async def connect(self):
        try:
            from bedrock_protocol import Client
            
            self.client = Client(self.host, self.port)
            await asyncio.to_thread(self.client.authenticate, self.username)
            await asyncio.to_thread(self.client.connect)
            
            self.connected = True
            self.running = True
            
            asyncio.create_task(self._packet_handler())
            
            logger.info(f"Conectado ao servidor Bedrock como {self.username}")
            
        except ImportError:
            logger.warning("bedrock_protocol não disponível, usando implementação alternativa")
            await self._connect_alternative()
        except Exception as e:
            logger.error(f"Erro ao conectar: {e}")
            await self._connect_alternative()
    
    async def _connect_alternative(self):
        try:
            import mcstatus
            
            logger.info("Tentando conexão alternativa...")
            self.connected = True
            self.running = True
            
            asyncio.create_task(self._simulate_connection())
            
        except Exception as e:
            logger.error(f"Erro na conexão alternativa: {e}")
            logger.info("Iniciando em modo simulação...")
            self.connected = True
            self.running = True
            asyncio.create_task(self._simulate_connection())
    
    async def _simulate_connection(self):
        logger.info("Bot em modo simulação - logs de ações serão mostrados no console")
        while self.running:
            await asyncio.sleep(1)
    
    async def disconnect(self):
        self.running = False
        self.connected = False
        
        if hasattr(self, 'client'):
            try:
                await asyncio.to_thread(self.client.disconnect)
            except:
                pass
        
        logger.info("Desconectado do servidor")
    
    async def update(self):
        if not self.running:
            return
        
        await asyncio.sleep(0.05)
    
    async def _packet_handler(self):
        while self.running:
            try:
                if hasattr(self, 'client'):
                    packet = await asyncio.to_thread(self.client.read_packet)
                    await self._process_packet(packet)
            except Exception as e:
                logger.error(f"Erro ao processar pacote: {e}")
                await asyncio.sleep(0.1)
    
    async def _process_packet(self, packet):
        try:
            packet_type = packet.get('type', '')
            
            if packet_type == 'text':
                source = packet.get('source_name', '')
                message = packet.get('message', '')
                
                if self.chat_callback and source != self.username:
                    await self.chat_callback(source, message)
            
            elif packet_type == 'move_player':
                player = packet.get('player', '')
                position = packet.get('position', {})
                
                if self.position_callback:
                    await self.position_callback(player, position)
            
            elif packet_type == 'set_health':
                self.health = packet.get('health', 20)
            
            elif packet_type == 'inventory':
                self.inventory = packet.get('items', {})
                
        except Exception as e:
            logger.error(f"Erro ao processar pacote: {e}")
    
    def on_chat_message(self, callback: Callable):
        self.chat_callback = callback
    
    def on_player_position(self, callback: Callable):
        self.position_callback = callback
    
    async def send_chat(self, message: str):
        logger.info(f"[CHAT] {self.username}: {message}")
        
        if hasattr(self, 'client'):
            try:
                await asyncio.to_thread(
                    self.client.send_packet,
                    {'type': 'text', 'message': message}
                )
            except:
                pass
    
    async def send_command(self, command: str):
        logger.info(f"[COMMAND] /{command}")
        
        if hasattr(self, 'client'):
            try:
                await asyncio.to_thread(
                    self.client.send_packet,
                    {'type': 'command_request', 'command': command}
                )
            except:
                pass
    
    async def move_to(self, x: float, y: float, z: float):
        logger.info(f"[MOVE] Movendo para ({x}, {y}, {z})")
        
        self.position = {'x': x, 'y': y, 'z': z}
        
        if hasattr(self, 'client'):
            try:
                await asyncio.to_thread(
                    self.client.send_packet,
                    {'type': 'move_player', 'position': self.position}
                )
            except:
                pass
    
    async def break_block(self, x: int, y: int, z: int):
        logger.info(f"[BREAK] Quebrando bloco em ({x}, {y}, {z})")
        
        if hasattr(self, 'client'):
            try:
                await asyncio.to_thread(
                    self.client.send_packet,
                    {'type': 'player_action', 'action': 'start_break', 'position': {'x': x, 'y': y, 'z': z}}
                )
                await asyncio.sleep(0.5)
                await asyncio.to_thread(
                    self.client.send_packet,
                    {'type': 'player_action', 'action': 'finish_break', 'position': {'x': x, 'y': y, 'z': z}}
                )
            except:
                pass
    
    async def place_block(self, x: int, y: int, z: int, block_type: str):
        logger.info(f"[PLACE] Colocando {block_type} em ({x}, {y}, {z})")
        
        if hasattr(self, 'client'):
            try:
                await asyncio.to_thread(
                    self.client.send_packet,
                    {'type': 'use_item', 'block_position': {'x': x, 'y': y, 'z': z}, 'item': block_type}
                )
            except:
                pass
    
    def get_position(self):
        return self.position.copy()
