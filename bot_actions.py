import asyncio
import logging
import math
from typing import Dict, Tuple

logger = logging.getLogger(__name__)

class BotActions:
    def __init__(self, connection):
        self.connection = connection
        self.current_task = None
        self.following = None
        
        self.block_types = {
            'wood': ['oak_log', 'birch_log', 'spruce_log', 'jungle_log'],
            'madeira': ['oak_log', 'birch_log', 'spruce_log', 'jungle_log'],
            'stone': ['stone', 'cobblestone'],
            'pedra': ['stone', 'cobblestone'],
            'dirt': ['dirt'],
            'terra': ['dirt']
        }
    
    async def goto_player(self, player_name: str):
        logger.info(f"Indo até o jogador {player_name}")
        
        if self.current_task:
            self.current_task.cancel()
        
        self.current_task = asyncio.create_task(self._goto_player_task(player_name))
        await self.current_task
    
    async def _goto_player_task(self, player_name: str):
        try:
            for _ in range(100):
                bot_pos = self.connection.get_position()
                
                target_pos = await self._find_player_position(player_name)
                
                if not target_pos:
                    await asyncio.sleep(0.5)
                    continue
                
                distance = self._calculate_distance(bot_pos, target_pos)
                
                if distance < 2.0:
                    logger.info(f"Chegou ao jogador {player_name}")
                    await self.connection.send_chat(f"Cheguei até você, {player_name}!")
                    break
                
                next_pos = self._calculate_next_position(bot_pos, target_pos)
                await self.connection.move_to(next_pos['x'], next_pos['y'], next_pos['z'])
                
                await asyncio.sleep(0.2)
            
        except asyncio.CancelledError:
            logger.info("Tarefa de movimento cancelada")
        except Exception as e:
            logger.error(f"Erro ao ir até jogador: {e}")
    
    async def follow_player(self, player_name: str):
        logger.info(f"Seguindo jogador {player_name}")
        
        if self.current_task:
            self.current_task.cancel()
        
        self.following = player_name
        self.current_task = asyncio.create_task(self._follow_player_task(player_name))
    
    async def _follow_player_task(self, player_name: str):
        try:
            while self.following == player_name:
                bot_pos = self.connection.get_position()
                target_pos = await self._find_player_position(player_name)
                
                if not target_pos:
                    await asyncio.sleep(0.5)
                    continue
                
                distance = self._calculate_distance(bot_pos, target_pos)
                
                if distance > 3.0:
                    next_pos = self._calculate_next_position(bot_pos, target_pos)
                    await self.connection.move_to(next_pos['x'], next_pos['y'], next_pos['z'])
                
                await asyncio.sleep(0.3)
                
        except asyncio.CancelledError:
            logger.info("Tarefa de seguir cancelada")
        except Exception as e:
            logger.error(f"Erro ao seguir jogador: {e}")
    
    async def collect_blocks(self, block_type: str, quantity: int):
        logger.info(f"Coletando {quantity} {block_type}")
        
        if self.current_task:
            self.current_task.cancel()
        
        self.current_task = asyncio.create_task(self._collect_blocks_task(block_type, quantity))
        await self.current_task
    
    async def _collect_blocks_task(self, block_type: str, quantity: int):
        try:
            blocks_to_find = self.block_types.get(block_type.lower(), [block_type])
            
            await self.connection.send_chat(f"Procurando {block_type}...")
            
            collected = 0
            search_radius = 50
            
            bot_pos = self.connection.get_position()
            
            for x_offset in range(-search_radius, search_radius, 5):
                for z_offset in range(-search_radius, search_radius, 5):
                    if collected >= quantity:
                        break
                    
                    target_x = bot_pos['x'] + x_offset
                    target_z = bot_pos['z'] + z_offset
                    target_y = bot_pos['y']
                    
                    await self.connection.move_to(target_x, target_y, target_z)
                    await asyncio.sleep(0.3)
                    
                    for y_offset in range(-2, 3):
                        block_x = int(target_x)
                        block_y = int(target_y + y_offset)
                        block_z = int(target_z)
                        
                        await self.connection.break_block(block_x, block_y, block_z)
                        collected += 1
                        
                        if collected >= quantity:
                            break
                        
                        await asyncio.sleep(0.1)
                
                if collected >= quantity:
                    break
            
            logger.info(f"Coletou {collected} blocos de {block_type}")
            await self.connection.send_chat(f"Coletei {collected} {block_type}!")
            
        except asyncio.CancelledError:
            logger.info("Tarefa de coleta cancelada")
        except Exception as e:
            logger.error(f"Erro ao coletar blocos: {e}")
    
    async def give_items(self, player_name: str, item_type: str, quantity: int):
        logger.info(f"Entregando {quantity} {item_type} para {player_name}")
        
        await self.connection.send_command(f"give {player_name} {item_type} {quantity}")
        
        await asyncio.sleep(0.5)
    
    async def stop_all(self):
        logger.info("Parando todas as ações")
        
        self.following = None
        
        if self.current_task:
            self.current_task.cancel()
            self.current_task = None
        
        await self.connection.send_chat("Parei todas as ações!")
    
    async def _find_player_position(self, player_name: str) -> Dict:
        positions = {
            player_name: {
                'x': self.connection.position['x'] + 10,
                'y': self.connection.position['y'],
                'z': self.connection.position['z'] + 10
            }
        }
        
        return positions.get(player_name)
    
    def _calculate_distance(self, pos1: Dict, pos2: Dict) -> float:
        dx = pos2['x'] - pos1['x']
        dy = pos2['y'] - pos1['y']
        dz = pos2['z'] - pos1['z']
        
        return math.sqrt(dx*dx + dy*dy + dz*dz)
    
    def _calculate_next_position(self, current: Dict, target: Dict, speed: float = 1.0) -> Dict:
        dx = target['x'] - current['x']
        dy = target['y'] - current['y']
        dz = target['z'] - current['z']
        
        distance = math.sqrt(dx*dx + dy*dy + dz*dz)
        
        if distance < speed:
            return target
        
        ratio = speed / distance
        
        return {
            'x': current['x'] + dx * ratio,
            'y': current['y'] + dy * ratio,
            'z': current['z'] + dz * ratio
        }
