#!/data/data/com.termux/files/usr/bin/bash

echo "╔════════════════════════════════════════╗"
echo "║  Bot Hailgames - Instalador Termux   ║"
echo "╚════════════════════════════════════════╝"
echo ""

echo "📱 Verificando ambiente Termux..."
sleep 1

if ! command -v node &> /dev/null; then
    echo "❌ Node.js não encontrado!"
    echo "📦 Instalando Node.js..."
    pkg update -y
    pkg install nodejs-lts -y
    echo "✅ Node.js instalado!"
else
    echo "✅ Node.js já instalado: $(node --version)"
fi

echo ""

if ! command -v git &> /dev/null; then
    echo "❌ Git não encontrado!"
    echo "📦 Instalando Git..."
    pkg install git -y
    echo "✅ Git instalado!"
else
    echo "✅ Git já instalado: $(git --version)"
fi

echo ""
echo "📦 Instalando dependências do bot..."
echo "⚠️  NOTA: Alguns avisos sobre módulos nativos são normais e podem ser ignorados."
echo ""

npm install --no-optional

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Instalação concluída com sucesso!"
else
    echo ""
    echo "⚠️  Instalação parcial - tentando com módulos opcionais..."
    npm install --legacy-peer-deps
fi

echo ""
echo "🎮 Para iniciar o bot, execute:"
echo "   npm start"
echo ""
echo "📖 Ou use o script:"
echo "   ./start.sh"
echo ""
echo "💡 Dica: Use tmux para manter o bot rodando em background"
echo "   pkg install tmux"
echo "   tmux new -s minecraft"
echo ""
echo "📝 IMPORTANTE:"
echo "   - Verifique se o servidor está online (Aternos precisa estar ativo)"
echo "   - Edite config.json se precisar mudar as configurações"
echo "   - Use 'npm start' para iniciar o bot"
echo ""
