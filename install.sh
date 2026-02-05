#!/data/data/com.termux/files/usr/bin/bash
# Orange Loop - Full Automated Installer
# Zero-One Alternating Intelligence Architecture
set -e

echo "🍊 ORANGE LOOP FULL INSTALLER"
echo "============================="
echo ""

# Check Termux
if [ ! -d "/data/data/com.termux" ]; then
 echo "❌ This installer is designed for Termux on Android"
 exit 1
fi

# Install dependencies
echo "📦 Installing dependencies..."
pkg update -y
pkg install -y python python-pip git wget proot-distro clang cmake ninja

# Install Python packages
echo "🐍 Installing Python packages..."
pip install --upgrade pip
pip install pyyaml psutil requests

# Create directory structure
LOOP_HOME="$HOME/orange-loop"
mkdir -p "$LOOP_HOME"/{models,cache,logs,config}

# Download models script
cat > "$LOOP_HOME/download-models.sh" << 'EOF'
#!/data/data/com.termux/files/usr/bin/bash
mkdir -p ~/orange-loop/models
cd ~/orange-loop/models
echo "📥 Downloading models..."
# Example download (replace with actual URLs)
# wget https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/qwen2.5-0.5b-instruct-q4_k_m.gguf
EOF
chmod +x "$LOOP_HOME/download-models.sh"

echo ""
echo "📁 Orange Loop installed to: $LOOP_HOME"
echo "✅ Installation complete!"
echo ""
echo "Next steps:"
echo "1. cd $LOOP_HOME"
echo "2. ./download-models.sh"
echo "3. python orange-loop.py"
