# 🤖 Bot Hailgames - Escolha Sua Versão

Este pacote contém **DUAS versões** do bot. Escolha a melhor para você!

## 📦 O que está incluído?

### ✅ Versão Python (RECOMENDADO para Termux)
- `bot.py` - Bot em Python
- `gemini_ai.py` - IA Gemini
- `bedrock_client.py` - Cliente Minecraft
- `requirements.txt` - Dependências
- `install-python.sh` - Instalador Python
- `start-python.sh` - Iniciar versão Python

### ⚠️ Versão Node.js (Alternativa)
- `index.js` - Bot em Node.js
- `geminiAI.js` - IA Gemini
- `pathfinding.js` - Navegação
- `botActions.js` - Ações do bot
- `package.json` - Dependências
- `install-termux.sh` - Instalador Node.js
- `start.sh` - Iniciar versão Node.js

### 📚 Documentação
- `README-PYTHON.md` - Guia da versão Python
- `README.md` - Guia da versão Node.js
- `EXAMPLES.md` - Exemplos de comandos
- `TERMUX_GUIDE.md` - Guia completo Termux
- `TROUBLESHOOTING.md` - Solução de problemas
- `config.json` - Configurações

---

## 🚀 INSTALAÇÃO RÁPIDA

### Opção 1: Python (RECOMENDADO) ⚡

```bash
# 1. Extrair ZIP
cd Bot-minecraft

# 2. Instalar
pkg install python git -y
chmod +x *.sh
./install-python.sh

# 3. Iniciar
python bot.py
```

**Tempo total: ~3 minutos**
**Sem erros de compilação!** ✅

---

### Opção 2: Node.js (Alternativa) 🐌

```bash
# 1. Extrair ZIP
cd Bot-minecraft

# 2. Instalar
pkg install nodejs-lts git -y
chmod +x *.sh
./install-termux.sh

# 3. Iniciar
npm start
```

**Tempo total: ~15 minutos**
**Pode ter erros de compilação** ⚠️

---

## 🆚 Comparação

| Critério | Python ✅ | Node.js ❌ |
|----------|----------|-----------|
| **Facilidade** | Muito fácil | Complicado |
| **Velocidade** | 3 minutos | 15+ minutos |
| **Erros** | Zero | Vários possíveis |
| **Memória** | ~50MB | ~150MB |
| **Estabilidade** | Excelente | Regular |
| **Compilação** | Não precisa | Precisa C++ |
| **Bateria** | Menos consumo | Mais consumo |

---

## 💡 Qual escolher?

### Use Python se:
- ✅ Você está no **Termux/Android**
- ✅ Quer **instalação rápida**
- ✅ Quer **zero problemas**
- ✅ Primeira vez fazendo isso

### Use Node.js se:
- ⚠️ Você já tentou Python e não funcionou
- ⚠️ Você **precisa** usar Node.js por algum motivo
- ⚠️ Você tem experiência com compilação

---

## 📋 Configuração (Ambas versões)

Edite o `config.json`:

```json
{
  "botName": "bot Hailgames",
  "server": {
    "host": "SEU_SERVIDOR.aternos.me",
    "port": 12345,
    "version": "1.21.50"
  },
  "gemini": {
    "apiKey": "SUA_API_KEY_AQUI"
  },
  "commandPrefix": "!BOT"
}
```

**Como obter API Key do Gemini:**
1. Acesse: https://makersuite.google.com/app/apikey
2. Clique em "Create API Key"
3. Copie e cole em `config.json`

---

## 🎮 Comandos (Ambas versões)

```
!BOT olá
!BOT venha até mim
!BOT pegue 10 madeiras
!BOT me entregue
!BOT me siga
!BOT pare
```

Veja `EXAMPLES.md` para mais exemplos!

---

## 🐛 Problemas?

### Python não conecta
```bash
pip install google-generativeai --upgrade
python bot.py
```

### Node.js não instala
```bash
npm install --no-optional
npm start
```

### Ainda com problemas?
Leia `TROUBLESHOOTING.md` para solução completa!

---

## 📱 Dicas Termux

### Manter rodando em background
```bash
pkg install tmux
tmux new -s bot

# Python
python bot.py

# OU Node.js
npm start

# Desanexar: Ctrl+B depois D
# Voltar: tmux attach -t bot
```

### Economizar bateria
1. Menu Termux → "Acquire wakelock"
2. Reduzir brilho
3. Fechar outros apps

---

## 📞 Suporte

1. **Leia a documentação** - Tudo está explicado!
2. **Veja TROUBLESHOOTING.md** - Soluções para erros comuns
3. **Abra issue no GitHub** - Se nada funcionar

---

## 🎯 Recomendação Final

**Use a versão Python!** 🐍

É mais rápida, mais estável, e funciona de primeira no Termux.
A versão Node.js está incluída apenas como alternativa.

---

**Boa sorte e divirta-se! 🎮🤖**
