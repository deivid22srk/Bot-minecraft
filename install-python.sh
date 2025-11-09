#!/data/data/com.termux/files/usr/bin/bash

echo "╔════════════════════════════════════════╗"
echo "║  Bot Hailgames - Instalador Python    ║"
echo "║         VERSÃO SEM RUST                ║"
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
echo "📦 Instalando dependências Python..."
echo "⚡ APENAS requests - SEM compilação!"
echo ""

# Instalar apenas requests (puro Python)
pip install requests --upgrade

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
    echo "💡 Vantagens desta versão:"
    echo "   ✅ SEM problemas de compilação (Rust, C++, etc)"
    echo "   ✅ Instalação em 30 segundos"
    echo "   ✅ Usa apenas requests (biblioteca pura Python)"
    echo "   ✅ Funciona 100% no Termux"
    echo ""
else
    echo ""
    echo "❌ Erro na instalação!"
    echo "🔧 Tente executar manualmente:"
    echo "   pkg update && pkg upgrade -y"
    echo "   pkg install python -y"
    echo "   pip install requests"
fi
