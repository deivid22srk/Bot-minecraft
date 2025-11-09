#!/data/data/com.termux/files/usr/bin/bash

echo "╔════════════════════════════════════════╗"
echo "║  Bot Hailgames - Instalador Python    ║"
echo "╚════════════════════════════════════════╝"
echo ""

echo "📱 Verificando ambiente Termux..."
sleep 1

# Instalar Python
if ! command -v python &> /dev/null; then
    echo "❌ Python não encontrado!"
    echo "📦 Instalando Python..."
    pkg update -y
    pkg install python -y
    echo "✅ Python instalado!"
else
    echo "✅ Python já instalado: $(python --version)"
fi

echo ""

# Instalar pip
echo "📦 Verificando pip..."
if ! command -v pip &> /dev/null; then
    echo "Instalando pip..."
    pkg install python-pip -y
fi

echo ""
echo "📦 Instalando dependências Python..."
echo "⚡ Isso é MUITO MAIS RÁPIDO que Node.js!"
echo ""

pip install -r requirements.txt --upgrade

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Instalação concluída com sucesso!"
    echo ""
    echo "🎮 Para iniciar o bot, execute:"
    echo "   python bot.py"
    echo ""
    echo "📖 Ou use o script:"
    echo "   ./start-python.sh"
    echo ""
    echo "💡 Vantagens da versão Python:"
    echo "   ✅ SEM problemas de compilação"
    echo "   ✅ Instalação rápida e simples"
    echo "   ✅ Usa menos memória"
    echo "   ✅ Mais estável no Termux"
    echo ""
else
    echo ""
    echo "❌ Erro na instalação!"
    echo "🔧 Tente executar manualmente:"
    echo "   pkg update && pkg upgrade -y"
    echo "   pkg install python python-pip -y"
    echo "   pip install google-generativeai aiohttp"
fi
