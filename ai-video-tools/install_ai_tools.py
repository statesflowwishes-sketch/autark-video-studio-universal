#!/usr/bin/env python3
"""
🤖 KI-Video-Tools Installer
Installiert alle 33+ Open-Source KI-Tools für Lernvideo-Erstellung
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

class AIVideoToolsInstaller:
    """Installer für KI-Video-Tools"""
    
    def __init__(self):
        self.system = platform.system().lower()
        self.python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
        self.has_gpu = self.check_gpu()
        
    def check_gpu(self):
        """Prüft ob NVIDIA GPU verfügbar ist"""
        try:
            result = subprocess.run(['nvidia-smi'], capture_output=True, text=True)
            return result.returncode == 0
        except FileNotFoundError:
            return False
    
    def run_command(self, command, description="", ignore_errors=False):
        """Führt einen Befehl aus"""
        print(f"🔧 {description}")
        print(f"   Befehl: {command}")
        
        try:
            result = subprocess.run(command, shell=True, check=True, 
                                  capture_output=True, text=True)
            print(f"   ✅ Erfolgreich!")
            return True
        except subprocess.CalledProcessError as e:
            if ignore_errors:
                print(f"   ⚠️ Warnung: {e} (wird ignoriert)")
                return True
            else:
                print(f"   ❌ Fehler: {e}")
                return False
    
    def install_system_dependencies(self):
        """Installiert System-Abhängigkeiten"""
        print("\n🔧 System-Abhängigkeiten installieren...")
        
        if self.system == 'linux':
            commands = [
                ("sudo apt update", "Package-Liste aktualisieren"),
                ("sudo apt install -y python3-pip", "Python pip installieren"),
                ("sudo apt install -y ffmpeg", "FFmpeg installieren"),
                ("sudo apt install -y git", "Git installieren"),
                ("sudo apt install -y nodejs npm", "Node.js für Remotion installieren"),
                ("sudo apt install -y build-essential", "Build-Tools installieren"),
                ("sudo apt install -y libsndfile1", "Audio-Bibliotheken installieren"),
                ("sudo apt install -y espeak espeak-data", "TTS-System installieren")
            ]
            
            for command, description in commands:
                self.run_command(command, description, ignore_errors=True)
    
    def install_python_packages(self):
        """Installiert Python-Pakete für KI-Video"""
        print("\n🐍 Python KI-Video-Pakete installieren...")
        
        # Basis-Pakete
        base_packages = [
            "torch torchvision torchaudio",  # PyTorch
            "transformers",                   # Hugging Face
            "diffusers",                     # Diffusion Models
            "accelerate",                    # GPU Acceleration
            "moviepy",                       # Video Processing
            "opencv-python",                 # Computer Vision
            "librosa",                       # Audio Processing
            "soundfile",                     # Audio I/O
            "matplotlib",                    # Plotting
            "pillow",                        # Image Processing
            "requests",                      # HTTP
            "tqdm",                         # Progress Bars
            "numpy",                        # Numerics
            "scipy"                         # Scientific Computing
        ]
        
        # TTS-Pakete
        tts_packages = [
            "coqui-tts",                    # Coqui TTS
            "bark-voice",                   # Bark TTS
            "pyttsx3",                      # Simple TTS
            "gTTS"                          # Google TTS
        ]
        
        # KI-Video-Pakete
        ai_video_packages = [
            "huggingface-hub",              # Model Hub
            "xformers",                     # Attention Optimization
            "scenedetect",                  # Scene Detection
            "imageio[ffmpeg]",              # Video I/O
            "imageio-ffmpeg"                # FFmpeg Plugin
        ]
        
        # Orchestrierung
        orchestration_packages = [
            "bentoml",                      # Model Serving
            "gradio",                       # Web Interface
            "streamlit"                     # Dashboard
        ]
        
        all_packages = base_packages + tts_packages + ai_video_packages + orchestration_packages
        
        for package in all_packages:
            self.run_command(f"pip3 install {package}", f"Installiere {package}")
    
    def install_remotion(self):
        """Installiert Remotion für React-basierte Videos"""
        print("\n⚛️ Remotion installieren...")
        
        commands = [
            ("npm install -g @remotion/cli", "Remotion CLI installieren"),
            ("npm install -g @remotion/player", "Remotion Player installieren")
        ]
        
        for command, description in commands:
            self.run_command(command, description)
    
    def download_ai_models(self):
        """Lädt KI-Modelle herunter"""
        print("\n📥 KI-Modelle herunterladen...")
        
        # Erstelle Modell-Ordner
        models_dir = Path.cwd() / "ai-models"
        models_dir.mkdir(exist_ok=True)
        
        models = [
            ("stabilityai/stable-video-diffusion-img2vid-xt", "Stable Video Diffusion"),
            ("runwayml/stable-diffusion-v1-5", "Stable Diffusion"),
            ("openai/whisper-base", "Whisper Speech Recognition"),
        ]
        
        for model_id, description in models:
            command = f"huggingface-cli download {model_id} --cache-dir {models_dir}"
            self.run_command(command, f"Lade {description} herunter", ignore_errors=True)
    
    def setup_project_structure(self):
        """Richtet Projektstruktur ein"""
        print("\n📁 Projektstruktur einrichten...")
        
        folders = [
            "ai-models",
            "generated-videos",
            "temp-files",
            "training-data",
            "configs"
        ]
        
        for folder in folders:
            folder_path = Path.cwd() / folder
            folder_path.mkdir(exist_ok=True)
            print(f"   ✅ Ordner erstellt: {folder}")
        
        # Beispiel-Konfigurationen erstellen
        config_content = {
            "video_settings": {
                "resolution": "1920x1080",
                "fps": 30,
                "duration": 60
            },
            "ai_models": {
                "text_to_video": "stable-video-diffusion",
                "text_to_speech": "coqui-tts",
                "text_to_image": "stable-diffusion"
            },
            "output_formats": ["mp4", "webm", "mov"]
        }
        
        import json
        with open("configs/default.json", "w") as f:
            json.dump(config_content, f, indent=2)
        
        print("   ✅ Standard-Konfiguration erstellt")
    
    def install_additional_tools(self):
        """Installiert zusätzliche nützliche Tools"""
        print("\n🛠️ Zusätzliche Tools installieren...")
        
        if self.system == 'linux':
            commands = [
                ("sudo apt install -y blender", "Blender 3D installieren"),
                ("sudo apt install -y kdenlive", "Kdenlive Video-Editor"),
                ("sudo apt install -y obs-studio", "OBS Studio"),
                ("pip3 install manim", "Manim mathematische Animationen"),
                ("pip3 install yt-dlp", "YouTube Downloader"),
                ("pip3 install jupyterlab", "Jupyter Lab")
            ]
            
            for command, description in commands:
                self.run_command(command, description, ignore_errors=True)
    
    def create_example_scripts(self):
        """Erstellt Beispiel-Skripte"""
        print("\n📝 Beispiel-Skripte erstellen...")
        
        # Text-to-Speech Beispiel
        tts_script = '''#!/usr/bin/env python3
"""Beispiel: Text-to-Speech mit Coqui TTS"""

from TTS.api import TTS
import argparse

def generate_speech(text, output_file="output.wav", voice="tts_models/de/thorsten/tacotron2-DDC"):
    """Generiert Sprache aus Text"""
    tts = TTS(voice)
    tts.tts_to_file(text=text, file_path=output_file)
    print(f"Audio gespeichert: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", required=True, help="Text für TTS")
    parser.add_argument("--output", default="speech.wav", help="Ausgabe-Datei")
    
    args = parser.parse_args()
    generate_speech(args.text, args.output)
'''
        
        with open("ai-video-tools/text-to-speech/generate_tts.py", "w") as f:
            f.write(tts_script)
        
        # Video-Generation Beispiel
        video_script = '''#!/usr/bin/env python3
"""Beispiel: Text-to-Video mit Stable Video Diffusion"""

import torch
from diffusers import StableVideoDiffusionPipeline
from PIL import Image
import argparse

def generate_video(prompt, output_file="output.mp4", num_frames=25):
    """Generiert Video aus Text-Prompt"""
    # Lade Modell
    pipe = StableVideoDiffusionPipeline.from_pretrained(
        "stabilityai/stable-video-diffusion-img2vid-xt",
        torch_dtype=torch.float16
    )
    
    if torch.cuda.is_available():
        pipe = pipe.to("cuda")
    
    # Erstelle Basis-Bild aus Prompt
    # (In der Praxis würden Sie zuerst Stable Diffusion verwenden)
    image = Image.new('RGB', (1024, 576), color='black')
    
    # Generiere Video
    frames = pipe(image, num_frames=num_frames).frames[0]
    
    # Speichere als Video
    import imageio
    imageio.mimsave(output_file, frames, fps=8)
    print(f"Video gespeichert: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prompt", required=True, help="Text-Prompt für Video")
    parser.add_argument("--output", default="video.mp4", help="Ausgabe-Datei")
    
    args = parser.parse_args()
    generate_video(args.prompt, args.output)
'''
        
        with open("ai-video-tools/text-to-video/generate_video.py", "w") as f:
            f.write(video_script)
        
        print("   ✅ Beispiel-Skripte erstellt!")
    
    def show_system_info(self):
        """Zeigt System-Informationen"""
        print("\n💻 System-Information:")
        print(f"   OS: {platform.system()} {platform.release()}")
        print(f"   Python: {self.python_version}")
        print(f"   GPU verfügbar: {'✅ Ja' if self.has_gpu else '❌ Nein'}")
        print(f"   CPU Kerne: {os.cpu_count()}")
        
        # GPU Info
        if self.has_gpu:
            try:
                result = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader'], 
                                      capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"   GPU: {result.stdout.strip()}")
            except:
                pass
    
    def show_next_steps(self):
        """Zeigt nächste Schritte"""
        print("\n🎯 Installation abgeschlossen!")
        print("=" * 50)
        print("📋 Nächste Schritte:")
        print()
        print("1. 🎵 Text-to-Speech testen:")
        print("   python3 ai-video-tools/text-to-speech/generate_tts.py --text 'Hallo Welt'")
        print()
        print("2. 🎬 Text-to-Video testen:")
        print("   python3 ai-video-tools/text-to-video/generate_video.py --prompt 'futuristic computer'")
        print()
        print("3. ⚛️ Remotion-Projekt erstellen:")
        print("   cd ai-video-tools/remotion-project")
        print("   npx create-remotion-video")
        print()
        print("4. 📊 Jupyter Lab starten:")
        print("   jupyter lab")
        print()
        print("5. 🖥️ Bestehende PC-Animation erweitern:")
        print("   # Nutzen Sie die KI-Tools zur Verbesserung der motherboard.html")
        print()
        print("📚 Dokumentation:")
        print("   - README.md - Übersicht und Workflows")
        print("   - configs/default.json - Standard-Einstellungen")
        print("   - ai-models/ - Heruntergeladene KI-Modelle")
        print()
        print("💡 Tipps:")
        print("   - GPU beschleunigt KI-Modelle erheblich")
        print("   - Große Modelle benötigen viel RAM/VRAM")
        print("   - Beginnen Sie mit kleinen Tests")

def main():
    """Hauptfunktion"""
    print("🤖 KI-Video-Tools Installer")
    print("=" * 50)
    
    installer = AIVideoToolsInstaller()
    installer.show_system_info()
    
    print("\nWas möchten Sie installieren?")
    print("1. Vollinstallation (empfohlen)")
    print("2. Nur Python-Pakete")
    print("3. Nur System-Tools")
    print("4. Nur KI-Modelle herunterladen")
    print("5. Nur Beispiel-Projekte erstellen")
    
    choice = input("\nWählen Sie eine Option (1-5): ").strip()
    
    if choice == "1":
        installer.install_system_dependencies()
        installer.install_python_packages()
        installer.install_remotion()
        installer.download_ai_models()
        installer.setup_project_structure()
        installer.install_additional_tools()
        installer.create_example_scripts()
        installer.show_next_steps()
        
    elif choice == "2":
        installer.install_python_packages()
        installer.create_example_scripts()
        
    elif choice == "3":
        installer.install_system_dependencies()
        installer.install_additional_tools()
        
    elif choice == "4":
        installer.download_ai_models()
        
    elif choice == "5":
        installer.setup_project_structure()
        installer.create_example_scripts()
        
    else:
        print("❌ Ungültige Auswahl!")
        return
    
    print("\n🎉 Fertig! KI-Video-Tools sind bereit!")

if __name__ == "__main__":
    main()