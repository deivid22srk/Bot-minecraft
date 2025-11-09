# Bot Hailgames - Minecraft Bedrock Edition

Bot inteligente para Minecraft Bedrock Edition 1.21.120.4, controlado pela IA Gemini do Google.

## 🎮 Características

- **IA Avançada**: Controlado pela API Gemini para processamento natural de comandos
- **Comandos Inteligentes**: Responde apenas quando você usa o prefixo `!BOT`
- **CONEXÃO REAL**: Agora conecta de verdade ao servidor Bedrock via bedrock-protocol!
- **Dois Modos de Operação**:
  - **Modo Real**: Conecta ao servidor e executa ações reais no mundo
  - **Modo Simulação**: Funciona localmente para testes (sem servidor)
- **Ações Autônomas no Mundo**: 
  - Ir até jogadores (movimento real)
  - Coletar blocos (quebra blocos no mundo)
  - Entregar itens (via comando /give)
  - Seguir jogadores (movimento contínuo)
  - Conversar no chat (mensagens reais)
- **Arquitetura Híbrida**: Python (IA Gemini) + Node.js (Bedrock Protocol)
- **Leve e Otimizado**: Funciona perfeitamente no Termux

## 📋 Requisitos

- Termux (Android)
- Python 3.10+ (testado com Python 3.12)
- Conexão com internet
- Servidor Minecraft Bedrock (opcional - funciona em modo simulação)

## 🚀 Instalação no Termux

### 1. Instalar Termux
Baixe o Termux da F-Droid ou Google Play Store.

### 2. Clonar/Extrair o projeto
```bash
cd storage/downloads
unzip bot-hailgames.zip
cd bot-hailgames
```

### 3. Escolher modo de instalação

#### OPÇÃO A: Modo Real (Recomendado - Conexão Real ao Servidor)
```bash
chmod +x install_termux_real.sh
./install_termux_real.sh
```
Instala Python + Node.js + bedrock-protocol

#### OPÇÃO B: Modo Simulação (Apenas Python, sem Node.js)
```bash
chmod +x install_termux.sh
./install_termux.sh
```
Instala apenas Python (modo simulação)

### 4. Testar instalação (opcional)

#### Testar conexão Bedrock (só modo real)
```bash
node test_bedrock.js
```

#### Testar conexão TCP
```bash
python test_connection.py
```

#### Testar IA Gemini
```bash
python test_bot_interactive.py
```

### 5. Iniciar o bot

#### MODO REAL (conecta ao servidor de verdade)
```bash
python main_real.py
```
Ou use o script:
```bash
chmod +x start_real.sh
./start_real.sh
```

#### MODO SIMULAÇÃO (testes locais)
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

## 🎯 Dois Modos de Operação

### 🌐 MODO REAL (Recomendado)

**Arquivo**: `main_real.py`

Conecta **DE VERDADE** ao servidor Minecraft Bedrock usando bedrock-protocol!

**Características**:
- ✓ Conexão real via protocolo Bedrock
- ✓ Bot aparece no servidor como jogador
- ✓ Executa ações REAIS no mundo:
  - Se move de verdade
  - Quebra blocos reais
  - Envia mensagens no chat
  - Interage com jogadores
- ✓ Usa Python (IA Gemini) + Node.js (bedrock-protocol)
- ✓ Arquitetura híbrida otimizada

**Como usar**:
```bash
python main_real.py
```

**Requisitos**:
- Node.js instalado
- bedrock-protocol (npm install)
- Servidor Bedrock online

---

### 🧪 MODO SIMULAÇÃO

**Arquivo**: `main.py`

Funciona localmente sem conexão ao servidor. Útil para:
- Testar a IA Gemini
- Desenvolver novos comandos
- Ver como o bot funciona antes de conectar

**Características**:
- ✓ IA Gemini processa comandos normalmente
- ✓ Todas as ações são logadas no console
- ✓ Você pode testar todos os comandos
- ✓ Não precisa de servidor online
- ✗ Sem conexão real com Minecraft
- ✗ Ações apenas simuladas

**Como usar**:
```bash
python main.py
```

**Teste interativo da IA**:
```bash
python test_bot_interactive.py
```

## 🔧 Solução de Problemas

### Bot não conecta ao servidor
- Verifique se o servidor está online (Aternos precisa estar ativo)
- Confirme o endereço e porta no `config.json`
- Verifique sua conexão com internet
- Use `python test_connection.py` para testar a conexão
- **NOTA**: O bot funciona em modo simulação mesmo sem conexão real

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

## 🏗️ Arquitetura Híbrida (Modo Real)

```
┌─────────────────────────────────────────────────────────┐
│                    JOGADOR NO MINECRAFT                  │
│         Envia: "!BOT pegue madeira pra mim"             │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              BEDROCK CLIENT (Node.js)                    │
│                  bedrock_client.js                       │
│  • Conecta ao servidor Bedrock                          │
│  • Recebe mensagens do chat                             │
│  • Salva comando em: command_input.json                 │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              PYTHON BRIDGE (main_real.py)               │
│  • Lê command_input.json                                │
│  • Envia comando para Gemini AI                         │
│  • Recebe ação estruturada                              │
│  • Salva em: action_output.json                         │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              GEMINI AI (gemini_handler.py)              │
│  • Processa linguagem natural                           │
│  • Identifica ação: "collect_and_give"                  │
│  • Retorna JSON estruturado                             │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│              BEDROCK CLIENT (Node.js)                    │
│  • Lê action_output.json                                │
│  • Executa ações no servidor:                           │
│    - Coleta blocos (quebra)                             │
│    - Move até jogador                                   │
│    - Entrega itens (/give)                              │
│  • Envia mensagens no chat                              │
└────────────────────────┬────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────┐
│                    SERVIDOR MINECRAFT                    │
│            Bot executa ações no mundo real               │
└─────────────────────────────────────────────────────────┘
```

**Por que arquitetura híbrida?**
- ✓ Python é melhor para IA e processamento de dados
- ✓ Node.js tem bedrock-protocol estável e funcional
- ✓ Comunicação via arquivos JSON é simples e confiável
- ✓ Cada tecnologia faz o que faz de melhor

## 📚 Tecnologias Utilizadas

### Python (IA e Lógica)
- **Python 3.10+**: Linguagem principal (compatível com Python 3.12)
- **Google Gemini API REST**: Processamento de linguagem natural
- **Requests**: Cliente HTTP para API Gemini
- **Async/Await**: Operações assíncronas

### Node.js (Conexão Bedrock)
- **Node.js 14+**: Runtime JavaScript
- **bedrock-protocol**: Protocolo Minecraft Bedrock
- **npm**: Gerenciador de pacotes

## ✨ Otimizações para Termux

Esta versão foi otimizada especialmente para rodar no Termux:
- ✓ Apenas 2 dependências leves (requests, websocket-client)
- ✓ Sem dependências que precisam compilação (Rust, C++)
- ✓ API Gemini via REST (sem google-generativeai pesado)
- ✓ Compatível com Python 3.12
- ✓ Modo simulação para testes sem servidor
- ✓ Scripts de instalação automática
- ✓ Logs detalhados e coloridos

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
