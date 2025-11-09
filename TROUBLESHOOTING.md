# 🔧 Solucionando Problemas de Instalação no Termux

Este guia aborda especificamente o erro de compilação do `raknet-native` no Termux.

## ❌ O Problema

Ao executar `npm install`, você pode ver erros como:

```
Error: Could not locate the bindings file
error: in-class initializer for static data member is not a constant expression
make: *** [all] Error 2
```

## ✅ Por que isso acontece?

O `bedrock-protocol` usa um módulo nativo em C++ (`raknet-native`) que precisa ser compilado para o seu dispositivo. No Termux (Android ARM64), a compilação pode falhar devido a:

1. Incompatibilidades com C++17
2. Problemas com node-addon-api
3. Falta de ferramentas de compilação

## 🛠️ Soluções

### Solução 1: Instalar sem módulos opcionais (RECOMENDADO)

```bash
cd Bot-minecraft
npm install --no-optional
```

Isso ignora módulos opcionais que falham na compilação.

### Solução 2: Usar o instalador automático

```bash
chmod +x install-termux.sh
./install-termux.sh
```

O script já está configurado para lidar com esses erros.

### Solução 3: Instalar dependências manualmente

```bash
# Limpar instalação anterior
rm -rf node_modules package-lock.json

# Instalar ferramentas de compilação
pkg install clang make cmake python -y

# Tentar instalar novamente
npm install --build-from-source
```

### Solução 4: Forçar instalação com legacy

```bash
npm install --legacy-peer-deps
```

## ⚠️ IMPORTANTE

**O bot funcionará MESMO SE a compilação do raknet-native falhar!**

O bedrock-protocol tem um fallback para JavaScript puro quando o módulo nativo não está disponível. A performance pode ser um pouco menor, mas todas as funcionalidades funcionarão.

## ✅ Como saber se funcionou?

Após a instalação (mesmo com erros), execute:

```bash
npm start
```

Se você ver:

```
🤖 Conectando ao servidor...
✅ Bot conectado e spawnou no servidor!
```

**Está tudo funcionando!** 🎉

## 🐛 Erros comuns e soluções

### Erro: "Cannot find module 'bedrock-protocol'"

**Solução:**
```bash
npm install bedrock-protocol --save
```

### Erro: "node: command not found"

**Solução:**
```bash
pkg install nodejs-lts
```

### Erro: "Permission denied"

**Solução:**
```bash
chmod +x *.sh
chmod +x index.js
```

### Erro: "EACCES: permission denied"

**Solução:**
```bash
npm config set unsafe-perm true
npm install
```

### Erro: "gyp ERR! stack Error: not found: make"

**Solução:**
```bash
pkg install make clang cmake python
npm install
```

## 📊 Teste rápido

Execute este comando para verificar se está tudo ok:

```bash
node -e "console.log('✅ Node.js funcionando!'); const bedrock = require('bedrock-protocol'); console.log('✅ Bedrock-protocol carregado!');"
```

Se ver as duas mensagens de sucesso, está pronto!

## 🎯 Checklist de instalação

- [ ] Termux instalado (F-Droid ou GitHub)
- [ ] `pkg update && pkg upgrade -y` executado
- [ ] Node.js instalado (`node --version`)
- [ ] Git instalado (`git --version`)
- [ ] Repositório clonado
- [ ] Permissões configuradas (`chmod +x *.sh`)
- [ ] `npm install` executado (pode ter avisos, OK!)
- [ ] `config.json` configurado
- [ ] Bot iniciado com `npm start`

## 🆘 Ainda com problemas?

### Opção 1: Instalação limpa
```bash
cd ~
rm -rf Bot-minecraft
git clone https://github.com/deivid22srk/Bot-minecraft.git
cd Bot-minecraft
chmod +x *.sh
./install-termux.sh
npm start
```

### Opção 2: Verificar logs detalhados
```bash
npm start 2>&1 | tee bot-debug.log
```

Isso salvará todos os logs em `bot-debug.log` para análise.

### Opção 3: Testar apenas o Gemini
```bash
node -e "
const { GoogleGenerativeAI } = require('@google/generative-ai');
const genAI = new GoogleGenerativeAI('SUA_API_KEY');
console.log('✅ Gemini OK!');
"
```

## 📝 Informações úteis para reportar bugs

Se precisar abrir uma issue, inclua:

```bash
# Versão do Node.js
node --version

# Versão do NPM
npm --version

# Sistema operacional
uname -a

# Arquitetura do processador
uname -m

# Logs de instalação
npm install --verbose > install.log 2>&1
```

## 💡 Dicas extras

### Use tmux para manter o bot rodando
```bash
pkg install tmux
tmux new -s bot
npm start
# Ctrl+B depois D para desanexar
```

### Monitore a memória
```bash
pkg install htop
htop
```

### Limpar cache do npm
```bash
npm cache clean --force
```

### Reinstalar Node.js
```bash
pkg uninstall nodejs-lts
pkg install nodejs-lts
```

## 🎉 Conclusão

Mesmo com erros de compilação, o bot funcionará! Os módulos nativos são opcionais e o bedrock-protocol funciona perfeitamente sem eles.

**Ignore os avisos sobre raknet-native e divirta-se com seu bot!** 🤖🎮

---

**Precisa de ajuda? Abra uma issue no GitHub!**
