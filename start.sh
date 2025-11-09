#!/data/data/com.termux/files/usr/bin/bash

echo "🤖 Iniciando Bot Hailgames..."
echo ""

if [ ! -d "node_modules" ]; then
    echo "📦 Instalando dependências..."
    npm install
    echo ""
fi

if [ ! -f "config.json" ]; then
    echo "❌ Erro: arquivo config.json não encontrado!"
    echo "📝 Crie o arquivo config.json com as configurações do servidor."
    exit 1
fi

echo "🚀 Conectando ao servidor..."
echo ""

node index.js
