# Bot Hailgames - Minecraft Bedrock Edition

Bot inteligente para Minecraft Bedrock Edition 1.21.120.4, controlado pela IA Gemini do Google.

## 🎮 Características

- **IA Avançada**: Controlado pela API Gemini para processamento natural de comandos
- **Comandos Inteligentes**: Responde apenas quando você usa o prefixo `!BOT`
- **Ações Autônomas**: 
  - Ir até jogadores
  - Coletar blocos (madeira, pedra, etc)
  - Entregar itens
  - Seguir jogadores
  - Conversar no chat

## 📋 Requisitos

- Termux (Android)
- Python 3.10+
- Conexão com internet
- Servidor Minecraft Bedrock

## 🚀 Instalação no Termux

### 1. Instalar Termux
Baixe o Termux da F-Droid ou Google Play Store.

### 2. Clonar/Extrair o projeto
```bash
cd storage/downloads
unzip bot-hailgames.zip
cd bot-hailgames
```

### 3. Executar instalador
```bash
chmod +x install_termux.sh
./install_termux.sh
```

### 4. Iniciar o bot
```bash
python main.py
```

Ou use o script:
```bash
chmod +x start.sh
./start.sh
```

## ⚙️ Configuração

Edite o arquivo `config.json` para personalizar:

```json
{
    "bot_name": "bot Hailgames",
    "server": {
        "host": "FizAnal.aternos.me",
        "port": 45203
    },
    "gemini_api_key": "SUA_API_KEY_AQUI",
    "command_prefix": "!BOT",
    "bot_version": "1.21.120.4"
}
```

## 🎯 Como Usar

### Comandos Básicos

Todos os comandos devem começar com `!BOT`:

#### Navegação
```
!BOT venha até mim
!BOT me siga
!BOT pare
```

#### Coleta e Entrega
```
!BOT pegue madeira pra mim e me entregue
!BOT colete 20 pedras e traga para mim
!BOT busque terra
```

#### Interação
```
!BOT olá
!BOT o que você pode fazer?
```

### Exemplos Práticos

**Exemplo 1: Buscar recursos**
```
Jogador: !BOT pegue madeira pra mim e me entregue
Bot: Vou coletar madeira e entregar para você!
Bot: Procurando madeira...
Bot: Coletei 10 madeira!
Bot: Indo até você!
Bot: Entreguei 10 madeira para você!
```

**Exemplo 2: Seguir jogador**
```
Jogador: !BOT me siga
Bot: Vou seguir você!
[Bot começa a seguir o jogador]
```

**Exemplo 3: Ir até jogador**
```
Jogador: !BOT venha ate min
Bot: Indo até você!
Bot: Cheguei até você!
```

## 🤖 Funcionalidades da IA

O bot usa a IA Gemini para entender comandos naturais. Você não precisa usar comandos exatos, a IA entende variações como:

- "venha aqui" = "vem até mim" = "vem pra cá"
- "pegue madeira" = "colete wood" = "busque árvores"
- "me siga" = "siga-me" = "vem comigo"

## 📁 Estrutura do Projeto

```
bot-hailgames/
├── main.py                  # Arquivo principal
├── bot_client.py           # Cliente do bot
├── bedrock_connection.py   # Conexão com servidor Bedrock
├── bot_actions.py          # Ações do bot (movimento, coleta, etc)
├── gemini_handler.py       # Integração com Gemini AI
├── config.json             # Configurações
├── requirements.txt        # Dependências Python
├── install_termux.sh       # Script de instalação
├── start.sh               # Script para iniciar
└── README.md              # Este arquivo
```

## 🔧 Solução de Problemas

### Bot não conecta ao servidor
- Verifique se o servidor está online (Aternos precisa estar ativo)
- Confirme o endereço e porta no `config.json`
- Verifique sua conexão com internet

### Erro na API do Gemini
- Confirme se a API key está correta no `config.json`
- Verifique se você tem quota disponível na API do Gemini
- Acesse: https://makersuite.google.com/app/apikey

### Bot não responde aos comandos
- Certifique-se de usar o prefixo `!BOT` antes do comando
- Verifique se o bot está online no servidor
- Veja os logs no console para mais detalhes

### Problemas no Termux
```bash
# Atualizar pacotes
pkg update && pkg upgrade

# Reinstalar Python
pkg install python -y

# Reinstalar dependências
pip install -r requirements.txt --force-reinstall
```

## 🌐 Informações do Servidor

**Servidor Padrão:**
- Endereço: FizAnal.aternos.me
- Porta: 45203
- Versão: Bedrock 1.21.120.4

> ⚠️ **Nota**: Servidores Aternos desligam automaticamente após inatividade. Certifique-se de que o servidor está online antes de iniciar o bot.

## 📝 Logs

O bot gera logs detalhados no console:
- `INFO`: Informações gerais
- `WARNING`: Avisos
- `ERROR`: Erros

Exemplo:
```
2024-11-09 10:30:15 - bot_client - INFO - Conectando ao servidor...
2024-11-09 10:30:16 - bedrock_connection - INFO - Conectado ao servidor Bedrock
2024-11-09 10:30:17 - bot_client - INFO - bot Hailgames conectado com sucesso!
```

## 🛡️ Segurança

- **API Key**: Mantenha sua chave do Gemini em segredo
- **Servidor**: Use apenas em servidores onde você tem permissão
- **Comandos**: O bot só executa comandos de jogadores no servidor

## 📚 Tecnologias Utilizadas

- **Python 3.10+**: Linguagem principal
- **Google Gemini AI**: Processamento de linguagem natural
- **Async/Await**: Operações assíncronas
- **WebSocket**: Comunicação em tempo real
- **Minecraft Bedrock Protocol**: Protocolo de comunicação

## 🤝 Contribuindo

Para melhorar o bot:
1. Modifique os arquivos necessários
2. Teste as mudanças
3. Documente as alterações

## 📄 Licença

Este projeto é de uso pessoal e educacional.

## 👨‍💻 Desenvolvedor

Desenvolvido para o servidor Hailgames.

---

## 🆘 Suporte

Se encontrar problemas:
1. Verifique os logs no console
2. Revise a seção de Solução de Problemas
3. Confirme que todas as dependências estão instaladas
4. Verifique a conexão com o servidor

**Bom jogo! 🎮**
