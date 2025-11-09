import asyncio
import logging
from typing import Callable, Optional
import json
import time

logger = logging.getLogger(__name__)

class BedrockConnection:
    def __init__(self, host: str, port: int, username: str):
        self.host = host
        self.port = port
        self.username = username
        
        self.connected = False
        
        self.position = {'x': 0, 'y': 64, 'z': 0}
        self.health = 20
        self.inventory = {}
        
        self.chat_callback = None
        self.position_callback = None
        
        self.running = False
        self.simulate_mode = True
        
    async def connect(self):
        try:
            logger.info(f"Tentando conectar a {self.host}:{self.port}...")
            
            try:
                import websocket
                
                ws_url = f"ws://{self.host}:{self.port}"
                logger.info(f"Conectando via WebSocket: {ws_url}")
                
                self.ws = await asyncio.to_thread(
                    websocket.create_connection,
                    ws_url,
                    timeout=5
                )
                
                self.simulate_mode = False
                self.connected = True
                logger.info(f"✓ Conectado ao servidor via WebSocket!")
                
            except Exception as e:
                logger.warning(f"WebSocket não disponível: {e}")
                logger.info("Iniciando em modo simulação...")
                self.simulate_mode = True
                self.connected = True
            
            self.running = True
            
            if self.simulate_mode:
                asyncio.create_task(self._simulate_connection())
                logger.info(f"✓ Bot {self.username} iniciado em modo simulação")
                logger.info("  Todos os comandos serão logados no console")
            else:
                asyncio.create_task(self._packet_handler())
            
        except Exception as e:
            logger.error(f"Erro ao conectar: {e}")
            logger.info("Iniciando em modo simulação...")
            self.simulate_mode = True
            self.connected = True
            self.running = True
            asyncio.create_task(self._simulate_connection())
    
    async def _simulate_connection(self):
        logger.info("=" * 60)
        logger.info("BOT EM MODO SIMULAÇÃO")
        logger.info("=" * 60)
        logger.info("")
        logger.info("O bot está funcionando, mas não conectado ao servidor real.")
        logger.info("Todas as ações serão mostradas aqui no console.")
        logger.info("")
        logger.info("Para conectar ao servidor real, instale bibliotecas adicionais:")
        logger.info("  pip install bedrock-protocol")
        logger.info("")
        logger.info("=" * 60)
        
        while self.running:
            await asyncio.sleep(1)
    
    async def disconnect(self):
        self.running = False
        self.connected = False
        
        if hasattr(self, 'ws') and self.ws:
            try:
                await asyncio.to_thread(self.ws.close)
            except:
                pass
        
        logger.info("✓ Desconectado do servidor")
    
    async def update(self):
        if not self.running:
            return
        
        await asyncio.sleep(0.05)
    
    async def _packet_handler(self):
        while self.running:
            try:
                if hasattr(self, 'ws') and self.ws:
                    data = await asyncio.to_thread(self.ws.recv)
                    packet = json.loads(data)
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
        timestamp = time.strftime("%H:%M:%S")
        logger.info(f"[{timestamp}] [{self.username}] {message}")
        
        if not self.simulate_mode and hasattr(self, 'ws') and self.ws:
            try:
                packet = {
                    'type': 'text',
                    'message': message
                }
                await asyncio.to_thread(
                    self.ws.send,
                    json.dumps(packet)
                )
            except Exception as e:
                logger.error(f"Erro ao enviar chat: {e}")
    
    async def send_command(self, command: str):
        timestamp = time.strftime("%H:%M:%S")
        logger.info(f"[{timestamp}] [COMANDO] /{command}")
        
        if not self.simulate_mode and hasattr(self, 'ws') and self.ws:
            try:
                packet = {
                    'type': 'command_request',
                    'command': command
                }
                await asyncio.to_thread(
                    self.ws.send,
                    json.dumps(packet)
                )
            except Exception as e:
                logger.error(f"Erro ao enviar comando: {e}")
    
    async def move_to(self, x: float, y: float, z: float):
        timestamp = time.strftime("%H:%M:%S")
        logger.info(f"[{timestamp}] [MOVIMENTO] → ({x:.1f}, {y:.1f}, {z:.1f})")
        
        self.position = {'x': x, 'y': y, 'z': z}
        
        if not self.simulate_mode and hasattr(self, 'ws') and self.ws:
            try:
                packet = {
                    'type': 'move_player',
                    'position': self.position
                }
                await asyncio.to_thread(
                    self.ws.send,
                    json.dumps(packet)
                )
            except Exception as e:
                logger.error(f"Erro ao mover: {e}")
    
    async def break_block(self, x: int, y: int, z: int):
        timestamp = time.strftime("%H:%M:%S")
        logger.info(f"[{timestamp}] [QUEBRAR] Bloco em ({x}, {y}, {z})")
        
        if not self.simulate_mode and hasattr(self, 'ws') and self.ws:
            try:
                packet = {
                    'type': 'player_action',
                    'action': 'break',
                    'position': {'x': x, 'y': y, 'z': z}
                }
                await asyncio.to_thread(
                    self.ws.send,
                    json.dumps(packet)
                )
            except Exception as e:
                logger.error(f"Erro ao quebrar bloco: {e}")
    
    async def place_block(self, x: int, y: int, z: int, block_type: str):
        timestamp = time.strftime("%H:%M:%S")
        logger.info(f"[{timestamp}] [COLOCAR] {block_type} em ({x}, {y}, {z})")
        
        if not self.simulate_mode and hasattr(self, 'ws') and self.ws:
            try:
                packet = {
                    'type': 'use_item',
                    'block_position': {'x': x, 'y': y, 'z': z},
                    'item': block_type
                }
                await asyncio.to_thread(
                    self.ws.send,
                    json.dumps(packet)
                )
            except Exception as e:
                logger.error(f"Erro ao colocar bloco: {e}")
    
    def get_position(self):
        return self.position.copy()
