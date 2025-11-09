#!/usr/bin/env python3

import asyncio
import socket
import json

async def test_server_connection():
    print("=" * 60)
    print("TESTE DE CONEXÃO - BOT HAILGAMES")
    print("=" * 60)
    print()
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    host = config['server']['host']
    port = config['server']['port']
    
    print(f"Servidor: {host}")
    print(f"Porta: {port}")
    print()
    
    print("Testando conexão TCP...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"✓ Servidor ONLINE e acessível!")
            print(f"✓ Porta {port} está aberta")
            sock.close()
            return True
        else:
            print(f"✗ Não foi possível conectar")
            print(f"✗ Código de erro: {result}")
            sock.close()
            return False
            
    except socket.gaierror:
        print(f"✗ Erro ao resolver nome do host: {host}")
        print(f"✗ Verifique se o endereço está correto")
        print(f"✗ Verifique sua conexão com internet")
        return False
    except socket.timeout:
        print(f"✗ Timeout ao conectar")
        print(f"✗ O servidor pode estar offline")
        return False
    except Exception as e:
        print(f"✗ Erro: {e}")
        return False
    finally:
        print()
        print("=" * 60)
        print()
        print("DICAS:")
        print("- Para servidores Aternos, inicie o servidor ANTES de rodar o bot")
        print("- Verifique se a porta está correta no config.json")
        print("- Verifique sua conexão com internet")
        print()
        print("=" * 60)

if __name__ == "__main__":
    asyncio.run(test_server_connection())
