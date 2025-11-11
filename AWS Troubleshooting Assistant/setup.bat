@echo off
REM AWS Cloud Troubleshooting Assistant - Windows Setup Script

echo.
echo ================================
echo AWS Cloud Troubleshooting Setup
echo ================================
echo.

REM Check Python
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.11+ from python.org
    pause
    exit /b 1
)

python --version
echo [OK] Python found

REM Check Ollama
echo.
echo Checking Ollama installation...
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [WARNING] Ollama not found
    echo Please install Ollama from: https://ollama.com/download
    echo After installation, run this script again.
    pause
    exit /b 1
)

echo [OK] Ollama found

REM Download Llama model
echo.
echo Downloading Llama 3.1 model (this may take a few minutes)...
ollama pull llama3.1
if %errorlevel% neq 0 (
    echo [ERROR] Failed to download Llama 3.1
    pause
    exit /b 1
)
echo [OK] Llama 3.1 downloaded

REM Create virtual environment
echo.
echo Creating Python virtual environment...
if exist venv (
    echo [INFO] Virtual environment already exists
) else (
    python -m venv venv
    echo [OK] Virtual environment created
)

REM Activate and install dependencies
echo.
echo Installing Python dependencies...
call venv\Scripts\activate.bat
python -m pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
echo [OK] Dependencies installed

REM Create directories
echo.
echo Creating project structure...
mkdir data\raw\metrics 2>nul
mkdir data\raw\logs 2>nul
mkdir data\raw\incidents 2>nul
mkdir data\processed 2>nul
mkdir src\agents 2>nul
mkdir src\data_generation 2>nul
mkdir src\data_access 2>nul
mkdir src\llm 2>nul
mkdir src\utils 2>nul
mkdir src\knowledge_base 2>nul
mkdir knowledge_base\common_issues 2>nul
mkdir knowledge_base\embeddings 2>nul
mkdir notebooks 2>nul
mkdir outputs\reports 2>nul
mkdir outputs\visualizations 2>nul
mkdir tests 2>nul
mkdir logs 2>nul
echo [OK] Directories created

REM Create __init__.py files
echo. > src\__init__.py
echo. > src\agents\__init__.py
echo. > src\data_generation\__init__.py
echo. > src\data_access\__init__.py
echo. > src\llm\__init__.py
echo. > src\utils\__init__.py
echo. > src\knowledge_base\__init__.py
echo. > tests\__init__.py

REM Copy config
if not exist config.yaml (
    if exist config.yaml.example (
        copy config.yaml.example config.yaml >nul
        echo [OK] config.yaml created
    )
)

REM Download embedding model
echo.
echo Downloading embedding model...
ollama pull nomic-embed-text
echo [OK] Embedding model downloaded

REM Final message
echo.
echo ================================
echo Setup Complete!
echo ================================
echo.
echo Next steps:
echo.
echo 1. Activate virtual environment:
echo    venv\Scripts\activate
echo.
echo 2. Start Jupyter Notebook:
echo    jupyter notebook
echo.
echo 3. Open notebooks/01_data_generation.ipynb
echo.
echo 4. Read PROJECT_SPEC.md for details
echo.
echo Happy learning!
echo.
pause





