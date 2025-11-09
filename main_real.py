import asyncio
import json
import logging
import os
import subprocess
import signal
import time
from pathlib import Path
from gemini_handler import GeminiHandler

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BotHailgamesReal:
    def __init__(self):
        self.config = self.load_config()
        self.gemini = GeminiHandler(self.config['gemini_api_key'])
        self.bedrock_process = None
        self.running = False
        self.command_file = Path('command_input.json')
        self.action_file = Path('action_output.json')
        
    def load_config(self):
        with open('config.json', 'r') as f:
            return json.load(f)
    
    async def start(self):
        logger.info("=" * 60)
        logger.info(f"Iniciando {self.config['bot_name']} - MODO REAL")
        logger.info("=" * 60)
        logger.info(f"Servidor: {self.config['server']['host']}:{self.config['server']['port']}")
        logger.info("")
        
        if not self.check_nodejs():
            logger.error("Node.js não encontrado! Execute: pkg install nodejs")
            return
        
        if not self.check_bedrock_protocol():
            logger.info("Instalando bedrock-protocol...")
            await self.install_bedrock_protocol()
        
        logger.info("Iniciando cliente Bedrock (Node.js)...")
        logger.info("")
        
        try:
            self.bedrock_process = subprocess.Popen(
                ['node', 'bedrock_client.js'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1
            )
            
            self.running = True
            
            asyncio.create_task(self.read_bedrock_output())
            asyncio.create_task(self.process_commands())
            
            logger.info("✓ Bot iniciado com sucesso!")
            logger.info("✓ Cliente Bedrock rodando")
            logger.info("✓ IA Gemini ativa")
            logger.info("")
            logger.info("=" * 60)
            logger.info("Aguardando comandos dos jogadores...")
            logger.info("=" * 60)
            logger.info("")
            
            while self.running:
                await asyncio.sleep(1)
                
        except Exception as e:
            logger.error(f"Erro ao iniciar bot: {e}")
            raise
    
    def check_nodejs(self):
        try:
            result = subprocess.run(['node', '--version'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                logger.info(f"✓ Node.js encontrado: {result.stdout.strip()}")
                return True
        except FileNotFoundError:
            pass
        return False
    
    def check_bedrock_protocol(self):
        return Path('node_modules/bedrock-protocol').exists()
    
    async def install_bedrock_protocol(self):
        try:
            logger.info("Instalando dependências Node.js...")
            process = await asyncio.create_subprocess_exec(
                'npm', 'install',
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            
            await process.wait()
            
            if process.returncode == 0:
                logger.info("✓ bedrock-protocol instalado com sucesso!")
            else:
                logger.error("✗ Erro ao instalar bedrock-protocol")
                
        except Exception as e:
            logger.error(f"Erro ao instalar dependências: {e}")
    
    async def read_bedrock_output(self):
        while self.running and self.bedrock_process:
            try:
                line = self.bedrock_process.stdout.readline()
                if line:
                    print(line.strip())
                else:
                    await asyncio.sleep(0.1)
            except Exception as e:
                logger.error(f"Erro ao ler output do Bedrock: {e}")
                await asyncio.sleep(0.5)
    
    async def process_commands(self):
        logger.info("[PYTHON] Processador de comandos ativo")
        
        while self.running:
            try:
                if self.command_file.exists():
                    with open(self.command_file, 'r') as f:
                        command_data = json.load(f)
                    
                    self.command_file.unlink()
                    
                    player = command_data['player']
                    command = command_data['command']
                    
                    logger.info(f"[GEMINI] Processando comando de {player}: {command}")
                    
                    action_data = await self.gemini.process_command(player, command)
                    
                    logger.info(f"[GEMINI] Ação identificada: {action_data.get('action')}")
                    
                    with open(self.action_file, 'w') as f:
                        json.dump(action_data, f, indent=2)
                    
                await asyncio.sleep(0.1)
                
            except json.JSONDecodeError:
                await asyncio.sleep(0.1)
            except Exception as e:
                logger.error(f"Erro ao processar comando: {e}")
                await asyncio.sleep(0.5)
    
    async def stop(self):
        logger.info("Encerrando bot...")
        self.running = False
        
        if self.bedrock_process:
            self.bedrock_process.send_signal(signal.SIGINT)
            try:
                self.bedrock_process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.bedrock_process.kill()
        
        if self.command_file.exists():
            self.command_file.unlink()
        if self.action_file.exists():
            self.action_file.unlink()
        
        logger.info("Bot encerrado")

async def main():
    bot = BotHailgamesReal()
    
    try:
        await bot.start()
    except KeyboardInterrupt:
        logger.info("\nBot interrompido pelo usuário")
    except Exception as e:
        logger.error(f"Erro: {e}")
    finally:
        await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())
