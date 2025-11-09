#!/usr/bin/env python3

import asyncio
import json
from gemini_handler import GeminiHandler

async def main():
    print("=" * 60)
    print("MODO TESTE INTERATIVO - BOT HAILGAMES")
    print("=" * 60)
    print()
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    print(f"Bot: {config['bot_name']}")
    print(f"Prefixo de comando: {config['command_prefix']}")
    print()
    print("Este modo permite testar a IA Gemini sem conectar ao servidor.")
    print()
    print("Digite comandos como se estivesse no jogo:")
    print(f"  {config['command_prefix']} venha até mim")
    print(f"  {config['command_prefix']} pegue madeira")
    print(f"  {config['command_prefix']} me siga")
    print()
    print("Digite 'sair' para encerrar")
    print("=" * 60)
    print()
    
    gemini = GeminiHandler(config['gemini_api_key'])
    player_name = "TestPlayer"
    prefix = config['command_prefix']
    
    while True:
        try:
            user_input = input(f"{player_name}: ")
            
            if user_input.lower() in ['sair', 'exit', 'quit']:
                print("\nEncerrando teste...")
                break
            
            if not user_input.strip():
                continue
            
            if not user_input.startswith(prefix):
                print(f"(Mensagem ignorada - não começa com {prefix})")
                print()
                continue
            
            command = user_input[len(prefix):].strip()
            
            if not command:
                print("(Comando vazio)")
                print()
                continue
            
            print(f"\n[BOT] Processando comando...")
            
            action_data = await gemini.process_command(player_name, command)
            
            print(f"[BOT] Ação identificada: {action_data.get('action')}")
            print(f"[BOT] {action_data.get('response')}")
            
            if action_data.get('block_type'):
                print(f"[BOT] Tipo de bloco: {action_data.get('block_type')}")
            if action_data.get('quantity'):
                print(f"[BOT] Quantidade: {action_data.get('quantity')}")
            
            print()
            
        except KeyboardInterrupt:
            print("\n\nEncerrando teste...")
            break
        except Exception as e:
            print(f"\nErro: {e}")
            print()

if __name__ == "__main__":
    asyncio.run(main())
