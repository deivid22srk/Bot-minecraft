# 📱 Guia Completo - Instalação no Termux

Este guia detalha passo a passo como instalar e executar o Bot Hailgames no Termux.

## 🔧 Pré-requisitos

- Dispositivo Android (5.0 ou superior)
- Conexão com internet
- Pelo menos 500MB de espaço livre

## 📥 Passo 1: Instalar o Termux

### Opção 1: F-Droid (Recomendado)
1. Acesse https://f-droid.org/
2. Baixe o F-Droid (aplicativo de loja)
3. Instale o F-Droid
4. Abra o F-Droid e busque por "Termux"
5. Instale o Termux

### Opção 2: GitHub
1. Acesse https://github.com/termux/termux-app/releases
2. Baixe o arquivo `termux-app_vXX.apk`
3. Instale o APK (habilite "Fontes Desconhecidas" se necessário)

⚠️ **Importante**: NÃO use o Termux da Play Store (está desatualizado)

## 🚀 Passo 2: Configurar o Termux

### Abra o Termux pela primeira vez
```bash
# O Termux vai preparar o ambiente automaticamente
# Aguarde alguns segundos
```

### Configure permissões de armazenamento
```bash
termux-setup-storage
```
> Pressione "Permitir" quando solicitado

### Atualize os pacotes
```bash
pkg update && pkg upgrade -y
```
> Este processo pode demorar alguns minutos

## 📦 Passo 3: Instalar Dependências

### Instalar Node.js
```bash
pkg install nodejs-lts -y
```

### Verificar instalação
```bash
node --version
npm --version
```
> Deve mostrar as versões instaladas

### Instalar Git
```bash
pkg install git -y
```

### Verificar instalação do Git
```bash
git --version
```

## 📂 Passo 4: Baixar o Bot

### Navegar para a pasta home
```bash
cd ~
```

### Clonar o repositório
```bash
git clone https://github.com/deivid22srk/Bot-minecraft.git
```

### Entrar na pasta do bot
```bash
cd Bot-minecraft
```

### Verificar arquivos
```bash
ls -la
```
> Você deve ver: index.js, config.json, package.json, etc.

## ⚙️ Passo 5: Configurar o Bot

### Visualizar configuração atual
```bash
cat config.json
```

### (Opcional) Editar configuração
```bash
nano config.json
```

Pressione:
- `Ctrl + O` para salvar
- `Enter` para confirmar
- `Ctrl + X` para sair

### Configurações disponíveis:

```json
{
  "botName": "bot Hailgames",           // Nome do bot no servidor
  "server": {
    "host": "FizAnal.aternos.me",      // Endereço do servidor
    "port": 45203,                      // Porta do servidor
    "version": "1.21.50"                // Versão do Minecraft
  },
  "gemini": {
    "apiKey": "SUA_API_KEY"             // API Key do Gemini
  },
  "commandPrefix": "!BOT"               // Prefixo dos comandos
}
```

## 📥 Passo 6: Instalar Dependências do Bot

### Instalar pacotes Node.js
```bash
npm install
```
> Aguarde a instalação de todas as dependências

### Verificar instalação
```bash
ls node_modules/
```
> Você deve ver as pastas: bedrock-protocol, @google, vec3, etc.

## 🎮 Passo 7: Iniciar o Bot

### Comando simples
```bash
npm start
```

### Ou comando direto
```bash
node index.js
```

### O que você deve ver:
```
🤖 Conectando ao servidor FizAnal.aternos.me:45203...
👤 Nome do bot: bot Hailgames
✅ Bot conectado e spawnou no servidor!
📍 Aguardando comandos com o prefixo: !BOT
```

## ✅ Passo 8: Testar o Bot

### No Minecraft:
1. Entre no servidor `FizAnal.aternos.me:45203`
2. No chat, digite:
```
!BOT olá
```

3. O bot deve responder!

### Exemplos de comandos:
```
!BOT venha até mim
!BOT pegue 5 madeiras
!BOT me siga
!BOT o que você pode fazer?
```

## 🔄 Manter o Bot Rodando

### Problema: Termux fecha quando você sai
**Solução**: Use o Wake Lock do Termux

1. Abra o Termux
2. Arraste do lado esquerdo da tela
3. Clique em "Acquire wakelock"

### Usar Tmux (Sessões persistentes)

#### Instalar Tmux
```bash
pkg install tmux -y
```

#### Criar nova sessão
```bash
tmux new -s minecraft
```

#### Iniciar o bot
```bash
cd ~/Bot-minecraft
npm start
```

#### Desanexar da sessão
Pressione: `Ctrl + B`, depois `D`

#### Reanexar à sessão
```bash
tmux attach -t minecraft
```

#### Listar sessões
```bash
tmux ls
```

#### Matar sessão
```bash
tmux kill-session -t minecraft
```

## 🔧 Solução de Problemas

### Problema: "Permission denied"
```bash
chmod +x index.js
```

### Problema: "Cannot find module"
```bash
rm -rf node_modules package-lock.json
npm install
```

### Problema: "Network error"
- Verifique sua internet
- Verifique se o servidor está online
- Tente usar dados móveis em vez de Wi-Fi

### Problema: "API Key invalid"
1. Verifique a API Key em `config.json`
2. Obtenha uma nova: https://makersuite.google.com/app/apikey
3. Edite o arquivo:
```bash
nano config.json
```

### Problema: Bot não responde
1. Verifique os logs no console
2. Certifique-se de usar `!BOT` antes do comando
3. Tente reconectar o bot

### Problema: "Command not found"
```bash
# Atualizar PATH
export PATH=$PATH:$PREFIX/bin
```

## 🔄 Atualizar o Bot

### Baixar atualizações
```bash
cd ~/Bot-minecraft
git pull
npm install
```

### Reiniciar o bot
```bash
npm start
```

## 📊 Monitorar Performance

### Ver uso de CPU/RAM
```bash
pkg install htop
htop
```

### Ver logs em tempo real
```bash
npm start | tee bot.log
```

### Ver últimas 50 linhas do log
```bash
tail -50 bot.log
```

## 🔐 Segurança

### Proteger API Key

#### Criar arquivo .env
```bash
pkg install nano
nano .env
```

#### Adicionar:
```
GEMINI_API_KEY=sua_key_aqui
```

#### Salvar: `Ctrl+O`, `Enter`, `Ctrl+X`

### Adicionar .gitignore
```bash
echo ".env" >> .gitignore
echo "node_modules/" >> .gitignore
```

## 💡 Dicas Úteis

### Atalhos do Termux
- `Ctrl + C` - Parar programa
- `Ctrl + D` - Sair do Termux
- `Ctrl + L` - Limpar tela
- `Volume Up + C` - Copiar
- `Volume Up + V` - Colar
- `Volume Up + Q` - Mostrar teclas extras

### Economizar Bateria
1. Reduza o brilho da tela ao mínimo
2. Use Wake Lock
3. Feche outros aplicativos
4. Use modo avião (se não precisar de internet móvel)

### Comandos Úteis do Termux
```bash
# Limpar cache
pkg clean

# Ver espaço em disco
df -h

# Ver processos
ps aux

# Matar processo
pkill -f node

# Ver uso de rede
pkg install nethogs
nethogs
```

## 🆘 Comandos de Emergência

### Se algo der errado:

#### Parar o bot
```bash
pkill -f node
```

#### Resetar instalação
```bash
cd ~
rm -rf Bot-minecraft
rm -rf node_modules
```

#### Reinstalar tudo
```bash
pkg update && pkg upgrade -y
pkg install nodejs-lts git -y
cd ~
git clone https://github.com/deivid22srk/Bot-minecraft.git
cd Bot-minecraft
npm install
npm start
```

## 📞 Precisa de Ajuda?

1. ✅ Leia este guia completamente
2. ✅ Verifique os logs de erro
3. ✅ Tente as soluções de problemas
4. ✅ Abra uma issue no GitHub com:
   - Descrição do problema
   - Logs de erro
   - Versão do Android
   - Versão do Node.js (`node --version`)

---

**Boa sorte e divirta-se com seu bot! 🎮🤖**
