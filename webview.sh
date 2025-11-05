#!/bin/bash
# =====================================================
#  Activate Python 3.11 environment for WebView project
# =====================================================

PROJECT_DIR="$HOME/webview"
PY311="$HOME/.local/python311/bin/python3.11"
VENV_DIR="$PROJECT_DIR/venv"

# Cek apakah Python 3.11 sudah ada
if [ ! -f "$PY311" ]; then
  echo "❌ Python 3.11 belum terinstal di $PY311"
  echo "Silakan install dulu dengan:"
  echo "  cd /tmp && wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz"
  echo "  tar -xvf Python-3.11.9.tgz && cd Python-3.11.9"
  echo "  ./configure --enable-optimizations --prefix=$HOME/.local/python311"
  echo "  make -j$(nproc) && make install"
  exit 1
fi

# Buat virtual environment kalau belum ada
if [ ! -d "$VENV_DIR" ]; then
  echo "⚙️ Membuat virtual environment untuk project..."
  "$PY311" -m venv "$VENV_DIR"
fi

# Aktifkan venv
source "$VENV_DIR/bin/activate"

# Pastikan pip up-to-date
pip install --upgrade pip setuptools wheel > /dev/null

# Tampilkan versi
echo "✅ Virtual environment aktif!"
echo "Python versi: $(python --version)"
echo "Lokasi venv: $VENV_DIR"
echo
echo "Kamu sekarang siap menjalankan:"
echo "  buildozer android debug"
echo
