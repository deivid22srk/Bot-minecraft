#!/data/data/com.termux/files/usr/bin/bash

echo "🤖 Iniciando Bot Hailgames (Python)..."
echo ""

if [ ! -f "requirements.txt" ]; then
    echo "❌ Erro: requirements.txt não encontrado!"
    exit 1
fi

if [ ! -f "config.json" ]; then
    echo "❌ Erro: config.json não encontrado!"
    echo "📝 Crie o arquivo config.json com as configurações do servidor."
    exit 1
fi

# Verificar se dependências estão instaladas
if ! python -c "import google.generativeai" &> /dev/null; then
    echo "📦 Instalando dependências..."
    pip install -r requirements.txt
    echo ""
fi

echo "🚀 Conectando ao servidor..."
echo ""

python bot.py
