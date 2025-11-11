#!/bin/bash

# AWS Cloud Troubleshooting Assistant - Setup Script
# This script sets up the development environment for the free student version

set -e  # Exit on error

echo "🚀 AWS Cloud Troubleshooting Assistant - Setup"
echo "=============================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check Python version
echo "📦 Checking Python version..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo -e "${GREEN}✓${NC} Python $PYTHON_VERSION found"
    
    # Check if version is 3.11 or higher
    REQUIRED_VERSION="3.11"
    if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then 
        echo -e "${RED}✗${NC} Python 3.11+ required. Please upgrade."
        exit 1
    fi
else
    echo -e "${RED}✗${NC} Python 3 not found. Please install Python 3.11+"
    exit 1
fi

# Check if Ollama is installed
echo ""
echo "🤖 Checking Ollama installation..."
if command -v ollama &> /dev/null; then
    echo -e "${GREEN}✓${NC} Ollama is installed"
else
    echo -e "${YELLOW}!${NC} Ollama not found. Installing..."
    
    # Detect OS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "Detected macOS. Downloading Ollama..."
        curl -fsSL https://ollama.com/install.sh | sh
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "Detected Linux. Downloading Ollama..."
        curl -fsSL https://ollama.com/install.sh | sh
    else
        echo -e "${RED}✗${NC} Unsupported OS. Please install Ollama manually from https://ollama.com/download"
        exit 1
    fi
fi

# Download Llama 3.1 model
echo ""
echo "🦙 Downloading Llama 3.1 model (this may take a few minutes)..."
if ollama list | grep -q "llama3.1"; then
    echo -e "${GREEN}✓${NC} Llama 3.1 already downloaded"
else
    echo "Downloading Llama 3.1 (~4.7GB)..."
    ollama pull llama3.1
    echo -e "${GREEN}✓${NC} Llama 3.1 downloaded successfully"
fi

# Create virtual environment
echo ""
echo "🐍 Creating Python virtual environment..."
if [ -d "venv" ]; then
    echo -e "${YELLOW}!${NC} Virtual environment already exists. Skipping..."
else
    python3 -m venv venv
    echo -e "${GREEN}✓${NC} Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "📦 Installing Python dependencies..."
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip --quiet

# Install requirements
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt --quiet
    echo -e "${GREEN}✓${NC} Dependencies installed"
else
    echo -e "${RED}✗${NC} requirements.txt not found"
    exit 1
fi

# Create project structure
echo ""
echo "📁 Creating project directories..."

mkdir -p data/raw/{metrics,logs,incidents}
mkdir -p data/processed
mkdir -p src/{agents,data_generation,data_access,llm,utils,knowledge_base}
mkdir -p knowledge_base/{common_issues,embeddings}
mkdir -p notebooks
mkdir -p outputs/{reports,visualizations}
mkdir -p tests
mkdir -p logs

echo -e "${GREEN}✓${NC} Project structure created"

# Create __init__.py files
touch src/__init__.py
touch src/agents/__init__.py
touch src/data_generation/__init__.py
touch src/data_access/__init__.py
touch src/llm/__init__.py
touch src/utils/__init__.py
touch src/knowledge_base/__init__.py
touch tests/__init__.py

# Copy config example if config doesn't exist
if [ ! -f "config.yaml" ]; then
    if [ -f "config.yaml.example" ]; then
        cp config.yaml.example config.yaml
        echo -e "${GREEN}✓${NC} config.yaml created from example"
    fi
fi

# Pull embedding model for RAG
echo ""
echo "📚 Downloading embedding model for knowledge base..."
if ollama list | grep -q "nomic-embed-text"; then
    echo -e "${GREEN}✓${NC} Embedding model already downloaded"
else
    ollama pull nomic-embed-text
    echo -e "${GREEN}✓${NC} Embedding model downloaded"
fi

# Test Ollama
echo ""
echo "🧪 Testing Ollama..."
if ollama run llama3.1 "Say 'Setup successful!' and nothing else" 2>/dev/null | grep -q "successful"; then
    echo -e "${GREEN}✓${NC} Ollama is working correctly"
else
    echo -e "${YELLOW}!${NC} Ollama test inconclusive, but setup complete"
fi

# Print next steps
echo ""
echo "=============================================="
echo -e "${GREEN}✅ Setup Complete!${NC}"
echo "=============================================="
echo ""
echo "📚 Next steps:"
echo ""
echo "  1. Activate the virtual environment:"
echo "     source venv/bin/activate"
echo ""
echo "  2. Start Jupyter Notebook:"
echo "     jupyter notebook"
echo ""
echo "  3. Open notebooks/01_data_generation.ipynb to begin"
echo ""
echo "  4. Read PROJECT_SPEC.md for detailed instructions"
echo ""
echo "🎓 Happy learning!"
echo ""





