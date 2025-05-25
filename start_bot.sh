#!/bin/bash

echo "🧹 Limpiando caché de Python (__pycache__)..."
find . -type d -name "__pycache__" -exec rm -r {} + 2>/dev/null

echo "📦 Activando entorno virtual..."
source venv/bin/activate

echo "🚀 Iniciando bot de Telegram..."
python3 -m bot_telegram.bot
echo "✅ Bot iniciado con éxito."
echo "🛑 Para detener el bot, presiona Ctrl+C."