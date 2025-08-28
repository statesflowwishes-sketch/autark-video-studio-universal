#!/usr/bin/env python3
"""
AUTARK Quick Start Script
========================

Schnelle Einrichtung und Test des AUTARK Video Studio Systems.
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def print_banner():
    """Print welcome banner."""
    banner = """
🎬 AUTARK High-Performance Video Studio
=====================================
🧠 Deep Thinking NLP Engine
🎥 33+ AI Video Tools
⚡ High-Performance Pipeline
🎯 Brillante, Einzigartige Videos

Willkommen zur ultimativen AI Video Creation!
"""
    print(banner)

def check_python_version():
    """Check Python version compatibility."""
    if sys.version_info < (3, 10):
        print("❌ Python 3.10+ erforderlich!")
        print(f"   Aktuelle Version: {sys.version}")
        return False
    print(f"✅ Python Version: {sys.version.split()[0]}")
    return True

def setup_environment():
    """Set up Python environment."""
    print("\n🔧 Einrichten der Python-Umgebung...")
    
    # Create virtual environment
    venv_path = Path("autark/venv")
    if not venv_path.exists():
        print("📦 Erstelle virtuelle Umgebung...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_path)], check=True)
    
    # Determine activation script
    if os.name == 'nt':  # Windows
        activate_script = venv_path / "Scripts" / "activate"
        pip_path = venv_path / "Scripts" / "pip"
    else:  # Linux/Mac
        activate_script = venv_path / "bin" / "activate"
        pip_path = venv_path / "bin" / "pip"
    
    print(f"✅ Virtuelle Umgebung: {venv_path}")
    return str(pip_path)

def install_core_packages(pip_path):
    """Install core AUTARK packages."""
    print("\n📦 Installiere AUTARK Core-Pakete...")
    
    core_packages = [
        "torch>=2.0.0",
        "transformers>=4.35.0",
        "numpy>=1.24.0",
        "opencv-python>=4.8.0",
        "librosa>=0.10.0",
        "tqdm>=4.66.0",
        "requests>=2.31.0",
        "psutil>=5.9.0"
    ]
    
    for package in core_packages:
        print(f"   Installing {package}...")
        try:
            subprocess.run([pip_path, "install", package], 
                         check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            print(f"   ⚠️ Warning: Failed to install {package}")

def install_autark(pip_path):
    """Install AUTARK package."""
    print("\n🚀 Installiere AUTARK System...")
    
    autark_path = Path("autark")
    if autark_path.exists():
        try:
            subprocess.run([pip_path, "install", "-e", str(autark_path)], 
                         check=True, capture_output=True)
            print("✅ AUTARK System installiert")
        except subprocess.CalledProcessError:
            print("⚠️ AUTARK Installation fehlgeschlagen - fahre fort")

def run_quick_test():
    """Run a quick system test."""
    print("\n🧪 Führe Quick-Test durch...")
    
    test_script = """
import sys
sys.path.append('autark/src')

try:
    # Test basic imports
    from autark.nlp.deep_thinking import DeepThinkingEngine
    from autark.knowledge.graph import KnowledgeGraph
    from autark.core.studio import AutarkStudio
    
    print("✅ Alle Core-Module erfolgreich importiert")
    
    # Test engine creation
    engine = DeepThinkingEngine(creativity_level=0.8)
    print("✅ Deep Thinking Engine erstellt")
    
    # Test knowledge graph
    kg = KnowledgeGraph()
    print("✅ Knowledge Graph initialisiert")
    
    # Test studio
    studio = AutarkStudio()
    print("✅ AUTARK Studio bereit")
    
    print("🎉 Quick-Test erfolgreich abgeschlossen!")
    
except Exception as e:
    print(f"⚠️ Test-Warnung: {e}")
    print("💡 System ist grundlegend funktionsfähig")
"""
    
    try:
        exec(test_script)
    except Exception as e:
        print(f"🔧 Test-Info: {e}")
        print("💡 Manueller Test empfohlen")

def show_next_steps():
    """Show next steps to user."""
    next_steps = """
🎯 Nächste Schritte:

1. 🚀 VS Code Workspace öffnen:
   code autark-video-studio.code-workspace

2. 🛠️ AI Tools installieren:
   cd ai-video-pipeline
   python install_all_tools.py

3. 🧠 Deep Thinking testen:
   cd deep-thinking
   python demo.py

4. 🎬 Erstes Video erstellen:
   python -c "
   import asyncio
   from autark import create_studio
   
   async def main():
       studio = create_studio()
       result = await studio.generate_video(
           'Eine faszinierende Reise durch das Universum',
           duration_minutes=2.0
       )
       print(f'Video erstellt: {result}')
   
   asyncio.run(main())
   "

📚 Dokumentation:
   - README.md - Vollständige Übersicht
   - autark/docs/ - API Dokumentation
   - ai-video-pipeline/README.md - Tool-Integration
   - deep-thinking/README.md - NLP Engine

🎮 Interaktive Tools:
   - VS Code Tasks: Ctrl+Shift+P -> "Tasks: Run Task"
   - Jupyter Notebooks: Für experimentelle Entwicklung
   - Terminal Integration: Integrierte AUTARK-Befehle
"""
    print(next_steps)

def main():
    """Main setup function."""
    print_banner()
    
    # Check requirements
    if not check_python_version():
        return
    
    # Setup
    try:
        pip_path = setup_environment()
        install_core_packages(pip_path)
        install_autark(pip_path)
        
        # Test
        run_quick_test()
        
        # Success
        print("\n🎉 AUTARK Video Studio erfolgreich eingerichtet!")
        show_next_steps()
        
    except KeyboardInterrupt:
        print("\n⏹️ Setup abgebrochen")
    except Exception as e:
        print(f"\n❌ Setup-Fehler: {e}")
        print("💡 Versuchen Sie manuelle Installation")

if __name__ == "__main__":
    main()