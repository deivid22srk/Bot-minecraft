#!/data/data/com.termux/files/usr/bin/bash

echo "=========================================="
echo "  Instalador do Bot Hailgames"
echo "  Minecraft Bedrock Edition Bot"
echo "=========================================="
echo ""

echo "[1/5] Atualizando pacotes do Termux..."
pkg update -y
pkg upgrade -y

echo ""
echo "[2/5] Instalando Python e dependências..."
pkg install -y python python-pip git

echo ""
echo "[3/5] Instalando bibliotecas Python..."
pip install -r requirements.txt --no-cache-dir

echo ""
echo "[4/5] Verificando instalação..."
python --version
pip --version

echo ""
echo "[5/5] Configuração concluída!"
echo ""
echo "=========================================="
echo "  Instalação completa!"
echo "=========================================="
echo ""
echo "Para iniciar o bot, execute:"
echo "  python main.py"
echo ""
echo "Para parar o bot, pressione Ctrl+C"
echo ""
