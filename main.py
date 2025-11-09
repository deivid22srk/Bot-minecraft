#!/usr/bin/env python3

import asyncio
import json
import logging
from bot_client import MinecraftBot
from gemini_handler import GeminiHandler

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

async def main():
    config = load_config()
    
    logger.info(f"Iniciando {config['bot_name']}...")
    logger.info(f"Servidor: {config['server']['host']}:{config['server']['port']}")
    
    gemini = GeminiHandler(config['gemini_api_key'])
    bot = MinecraftBot(config, gemini)
    
    try:
        await bot.start()
    except KeyboardInterrupt:
        logger.info("Bot interrompido pelo usuário")
    except Exception as e:
        logger.error(f"Erro ao executar bot: {e}")
        raise
    finally:
        await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())
