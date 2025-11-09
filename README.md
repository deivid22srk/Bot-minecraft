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

### 6. Instalar dependências
```bash
npm install
```

### 7. Configurar (opcional)
Edite o arquivo `config.json` se quiser mudar configurações:
```bash
nano config.json
```

### 8. Iniciar o bot
```bash
npm start
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

## 🧠 Como Funciona

1. **Detecção**: O bot monitora o chat do servidor
2. **Ativação**: Quando detecta `!BOT`, captura o comando
3. **Processamento IA**: Envia o comando para o Gemini
4. **Análise**: O Gemini entende a intenção e retorna uma ação
5. **Execução**: O bot executa a ação no jogo
6. **Resposta**: Informa o jogador sobre o progresso

## 📁 Estrutura do Projeto

```
Bot-minecraft/
├── index.js           # Arquivo principal do bot
├── geminiAI.js        # Integração com Google Gemini
├── pathfinding.js     # Sistema de navegação
├── botActions.js      # Ações do bot (minerar, entregar, etc)
├── config.json        # Configurações
├── package.json       # Dependências do Node.js
└── README.md          # Este arquivo
```

## 🔧 Dependências

- **bedrock-protocol**: Conexão com servidores Minecraft Bedrock
- **@google/generative-ai**: API do Google Gemini
- **vec3**: Manipulação de vetores 3D

## 🐛 Solução de Problemas

### Bot não conecta ao servidor
- Verifique se o servidor está online (Aternos precisa estar ativo)
- Confirme o endereço e porta em `config.json`
- Verifique sua conexão com a internet

### Bot não responde aos comandos
- Certifique-se de usar o prefixo `!BOT`
- Verifique se a API Key do Gemini está correta
- Veja os logs no console para mais detalhes

### Erro de instalação no Termux
- Execute `pkg update && pkg upgrade` novamente
- Tente `pkg install nodejs` se nodejs-lts não funcionar
- Dê permissão de armazenamento: `termux-setup-storage`

### Erro "API Key inválida"
- Verifique se a API Key do Gemini está correta em `config.json`
- Obtenha uma nova key em: https://makersuite.google.com/app/apikey

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
- Use o plugin Wake Lock do Termux
- Reduza o brilho da tela
- Desative conexões desnecessárias

### Auto-iniciar bot
Crie um script `start.sh`:
```bash
#!/data/data/com.termux/files/usr/bin/bash
cd ~/Bot-minecraft
npm start
```

Dê permissão:
```bash
chmod +x start.sh
```

Execute:
```bash
./start.sh
```

## 🎯 Funcionalidades Futuras

- [ ] Sistema de crafting
- [ ] Construção automática
- [ ] Farming automático
- [ ] Combate e defesa
- [ ] Exploração de cavernas
- [ ] Backup de inventário

## 📄 Licença

MIT License - Sinta-se livre para modificar e usar!

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas features
- Enviar pull requests

## 📞 Suporte

Se tiver problemas ou dúvidas:
1. Verifique a seção de solução de problemas
2. Veja os logs do console
3. Abra uma issue no GitHub

---

**Desenvolvido com ❤️ para a comunidade Minecraft**
