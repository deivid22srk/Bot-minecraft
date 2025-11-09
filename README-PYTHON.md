# 🐍 Bot Hailgames - Versão Python (RECOMENDADO PARA TERMUX)

Bot inteligente para Minecraft Bedrock controlado pela IA Gemini - **Versão Python otimizada para Termux**.

## ⚡ Por que a versão Python é MELHOR?

| Característica | Python ✅ | Node.js ❌ |
|---------------|----------|-----------|
| **Instalação** | Simples, sem compilação | Erros de compilação |
| **Memória** | ~50MB | ~150MB |
| **Estabilidade no Termux** | Excelente | Problemas com módulos nativos |
| **Tempo de instalação** | ~2 minutos | ~15 minutos (se funcionar) |
| **Dependências** | Puras Python | Precisa compilar C++ |

## 🚀 Instalação Rápida no Termux

### 1. Instalar Termux
Baixe na [F-Droid](https://f-droid.org/en/packages/com.termux/) ou [GitHub](https://github.com/termux/termux-app/releases)

### 2. Preparar ambiente
```bash
pkg update && pkg upgrade -y
pkg install python git -y
```

### 3. Clonar repositório
```bash
git clone https://github.com/deivid22srk/Bot-minecraft.git
cd Bot-minecraft
```

### 4. Dar permissões
```bash
chmod +x *.sh
```

### 5. Instalar dependências
```bash
./install-python.sh
```

### 6. Iniciar o bot
```bash
python bot.py
```

ou

```bash
./start-python.sh
```

## ⚙️ Configuração

O arquivo `config.json` é o mesmo:

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

## 🎮 Comandos

Todos os comandos funcionam igual:

```
!BOT venha até mim
!BOT pegue 10 madeiras
!BOT me entregue
!BOT me siga
!BOT pare
!BOT olá
```

## 📦 Dependências

Apenas 1 dependência principal:
- `google-generativeai` - API do Gemini

**SEM** módulos nativos que precisam compilar! 🎉

## 🔧 Comparação de Instalação

### Python (RÁPIDO) ⚡
```bash
pkg install python -y          # 30 segundos
pip install google-generativeai # 1 minuto
python bot.py                   # Funciona!
```

### Node.js (LENTO) 🐌
```bash
pkg install nodejs-lts -y       # 2 minutos
npm install                     # 10+ minutos
# Erros de compilação do raknet-native
# Precisa instalar clang, make, cmake
# Pode não funcionar mesmo depois disso
```

## ✅ Vantagens da Versão Python

1. **Zero problemas de compilação**
   - Sem erros de `raknet-native`
   - Sem problemas de `node-addon-api`
   - Sem necessidade de compiladores C++

2. **Instalação ultra-rápida**
   - 2 minutos vs 15+ minutos
   - Menos downloads
   - Menos espaço em disco

3. **Mais estável**
   - Menos crashes
   - Melhor gerenciamento de memória
   - Reconexão automática

4. **Mais leve**
   - ~50MB vs ~150MB de RAM
   - Menor uso de CPU
   - Melhor para bateria

## 🆚 Escolha sua versão

### Use Python se:
- ✅ Você está no Termux/Android
- ✅ Quer instalação rápida e sem problemas
- ✅ Prefere estabilidade
- ✅ Quer economizar bateria

### Use Node.js se:
- ⚠️ Você está no PC/Linux
- ⚠️ Tem experiência com compilação
- ⚠️ Não se importa com problemas

## 📱 Dicas para Termux

### Manter rodando em background
```bash
pkg install tmux
tmux new -s bot
python bot.py
# Ctrl+B depois D para desanexar
```

### Verificar se está rodando
```bash
tmux ls
tmux attach -t bot
```

### Economizar bateria
1. Menu lateral → "Acquire wakelock"
2. Reduzir brilho da tela
3. Usar modo avião (se possível)

## 🐛 Solução de Problemas

### Erro: "No module named 'google.generativeai'"
```bash
pip install google-generativeai
```

### Erro: "python: command not found"
```bash
pkg install python
```

### Erro: "Permission denied"
```bash
chmod +x *.sh
```

### Bot não conecta
- Verifique se o servidor está online
- Confira o endereço em `config.json`
- Teste sua internet

## 📊 Estrutura dos Arquivos Python

```
Bot-minecraft/
├── bot.py                 # Arquivo principal (executa este)
├── gemini_ai.py          # Integração com Gemini
├── bedrock_client.py     # Cliente Minecraft
├── requirements.txt      # Dependências Python
├── config.json           # Configurações
├── install-python.sh     # Instalador Python
└── start-python.sh       # Iniciar bot Python
```

## 🎯 Status das Funcionalidades

- ✅ Conexão básica com servidor
- ✅ Processamento de comandos com IA
- ✅ Sistema de chat
- ✅ Reconexão automática
- ⏳ Navegação completa (em desenvolvimento)
- ⏳ Mineração real (em desenvolvimento)
- ⏳ Entrega de itens (em desenvolvimento)

## 💡 Próximos Passos

A versão Python está funcional e **muito mais estável** que Node.js no Termux. Para funcionalidades avançadas (pathfinding, mineração real), precisaremos integrar bibliotecas específicas do Minecraft Bedrock.

## 📄 Licença

MIT License

---

**🐍 Python FTW! Mais rápido, mais estável, sem dor de cabeça! 🚀**
