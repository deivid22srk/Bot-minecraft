# 🤖 Bot Hailgames - Minecraft Bedrock

Bot inteligente para Minecraft Bedrock 1.21.x controlado pela IA Gemini do Google. O bot executa comandos em linguagem natural e pode realizar diversas ações no jogo.

## 📋 Características

- 🧠 **Controlado por IA**: Usa Google Gemini para entender comandos em português
- 🎮 **Minecraft Bedrock**: Compatível com versão 1.21.x
- 📱 **Funciona no Termux**: Roda perfeitamente em dispositivos Android
- 🗣️ **Comandos Naturais**: Use linguagem natural após o prefixo `!BOT`
- 🎯 **Ações Inteligentes**: Navegação, mineração, entrega de itens e mais

## 🚀 Instalação no Termux

### 1. Instalar o Termux
Baixe o Termux na [F-Droid](https://f-droid.org/en/packages/com.termux/) ou [GitHub](https://github.com/termux/termux-app/releases)

⚠️ **IMPORTANTE**: NÃO use o Termux da Play Store (está desatualizado)

### 2. Atualizar pacotes do Termux
```bash
pkg update && pkg upgrade -y
```

### 3. Instalar Node.js
```bash
pkg install nodejs-lts -y
```

### 4. Instalar Git
```bash
pkg install git -y
```

### 5. Clonar o repositório
```bash
git clone https://github.com/deivid22srk/Bot-minecraft.git
cd Bot-minecraft
```

### 6. Dar permissão aos scripts
```bash
chmod +x *.sh
```

### 7. Instalar dependências
```bash
./install-termux.sh
```

⚠️ **NOTA**: Você pode ver avisos sobre módulos nativos (`raknet-native`). Isso é normal! O bot funcionará mesmo com esses avisos.

### 8. Iniciar o bot
```bash
npm start
```

ou

```bash
./start.sh
```

## ⚙️ Configuração

Arquivo `config.json`:
```json
{
  "botName": "bot Hailgames",
  "server": {
    "host": "FizAnal.aternos.me",
    "port": 45203,
    "version": "1.21.50"
  },
  "gemini": {
    "apiKey": "SUA_API_KEY_AQUI"
  },
  "commandPrefix": "!BOT"
}
```

## 🎮 Como Usar

### Comandos Disponíveis

O bot responde apenas a mensagens que começam com `!BOT`. Exemplos:

#### 🚶 Navegação
```
!BOT venha até mim
!BOT venha aqui
!BOT vem cá
```

#### ⛏️ Mineração
```
!BOT pegue 10 madeiras
!BOT mine pedra para mim
!BOT colete carvão
```

#### 🎁 Entrega de Itens
```
!BOT me entregue a madeira
!BOT traga os itens
!BOT dê os recursos para mim
```

#### 👥 Seguir Jogador
```
!BOT me siga
!BOT pare de seguir
```

#### 💬 Conversa
```
!BOT olá
!BOT como você está?
!BOT o que você pode fazer?
```

## 🐛 Solução de Problemas

### Erro de compilação do raknet-native

**Sintoma**: Erros durante `npm install` relacionados a `raknet-native` ou `node-addon-api`

**Solução**:
```bash
# Use a instalação sem módulos opcionais
npm install --no-optional
```

ou

```bash
# Use o instalador fornecido
./install-termux.sh
```

Esses erros são normais no Termux e o bot funcionará mesmo assim! 

### Bot não conecta ao servidor
- ✅ Verifique se o servidor está online (Aternos precisa estar ativo)
- ✅ Confirme o endereço e porta em `config.json`
- ✅ Verifique sua conexão com a internet

### Bot não responde aos comandos
- ✅ Certifique-se de usar o prefixo `!BOT`
- ✅ Verifique se a API Key do Gemini está correta
- ✅ Veja os logs no console para mais detalhes

### Erro "API Key inválida"
- ✅ Verifique se a API Key do Gemini está correta em `config.json`
- ✅ Obtenha uma nova key em: https://makersuite.google.com/app/apikey

## 📱 Dicas para Termux

### Manter bot rodando em background
```bash
# Instalar tmux
pkg install tmux

# Criar sessão
tmux new -s minecraft-bot

# Iniciar bot
npm start

# Desanexar: Ctrl+B e depois D
# Reanexar: tmux attach -t minecraft-bot
```

### Economizar bateria
1. Abra o menu lateral do Termux
2. Ative "Acquire wakelock"
3. Reduza o brilho da tela
4. Desative conexões desnecessárias

### Atalhos do Termux
- `Volume Up + Q` - Mostrar teclas extras
- `Volume Up + C` - Copiar
- `Volume Up + V` - Colar
- `Ctrl + C` - Parar programa
- `Ctrl + L` - Limpar tela

## 📁 Estrutura do Projeto

```
Bot-minecraft/
├── index.js              # Arquivo principal do bot
├── geminiAI.js           # Integração com Google Gemini
├── pathfinding.js        # Sistema de navegação
├── botActions.js         # Ações do bot (minerar, entregar, etc)
├── config.json           # Configurações
├── package.json          # Dependências do Node.js
├── install-termux.sh     # Script de instalação
├── start.sh              # Script para iniciar
├── README.md             # Este arquivo
├── TERMUX_GUIDE.md       # Guia detalhado do Termux
└── EXAMPLES.md           # Exemplos de comandos
```

## 🔧 Dependências

- **bedrock-protocol**: Conexão com servidores Minecraft Bedrock
- **@google/generative-ai**: API do Google Gemini
- **prismarine-physics**: Física do Minecraft
- **minecraft-protocol**: Protocolo alternativo

## 🎯 Funcionalidades

- ✅ Conexão com servidor Bedrock
- ✅ Processamento de comandos com IA
- ✅ Navegação inteligente
- ✅ Sistema de chat
- ✅ Detecção de jogadores
- ⏳ Mineração (em desenvolvimento)
- ⏳ Entrega de itens (em desenvolvimento)
- ⏳ Crafting (planejado)
- ⏳ Combate (planejado)

## 📄 Licença

MIT License - Sinta-se livre para modificar e usar!

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas features
- Enviar pull requests

## 📞 Suporte

Se tiver problemas ou dúvidas:
1. ✅ Leia a seção de solução de problemas
2. ✅ Verifique TERMUX_GUIDE.md para guia detalhado
3. ✅ Veja os logs do console
4. ✅ Abra uma issue no GitHub

---

**Desenvolvido com ❤️ para a comunidade Minecraft**
