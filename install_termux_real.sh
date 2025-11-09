#!/data/data/com.termux/files/usr/bin/bash

echo "=========================================="
echo "  Instalador do Bot Hailgames v2.1"
echo "  Minecraft Bedrock Edition Bot"
echo "  CONEXÃO REAL AO SERVIDOR"
echo "=========================================="
echo ""

echo "[1/6] Atualizando pacotes do Termux..."
pkg update -y
pkg upgrade -y

echo ""
echo "[2/6] Instalando Python e dependências..."
pkg install -y python python-pip git

echo ""
echo "[3/6] Instalando Node.js e npm..."
pkg install -y nodejs

echo ""
echo "[4/6] Instalando bibliotecas Python..."
pip install -r requirements.txt --no-cache-dir

echo ""
echo "[5/6] Instalando bedrock-protocol (Node.js)..."
npm install

echo ""
echo "[6/6] Verificando instalação..."
echo "Python:"
python --version
echo "Node.js:"
node --version
echo "npm:"
npm --version

echo ""
echo "=========================================="
echo "  Instalação completa!"
echo "=========================================="
echo ""
echo "MODO DE USO:"
echo ""
echo "1. MODO SIMULAÇÃO (sem conexão real):"
echo "   python main.py"
echo ""
echo "2. MODO REAL (conecta ao servidor Bedrock):"
echo "   python main_real.py"
echo ""
echo "3. Testar IA Gemini:"
echo "   python test_bot_interactive.py"
echo ""
echo "4. Testar conexão:"
echo "   python test_connection.py"
echo ""
echo "Para parar o bot, pressione Ctrl+C"
echo ""
