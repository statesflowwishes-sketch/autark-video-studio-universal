#!/usr/bin/env python3
"""
🛠️ Software-Installer für Multimedia-Projekte
Installiert automatisch alle benötigten Tools für Audio/Video-Bearbeitung
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

class MultimediaInstaller:
    """Installer für Multimedia-Software"""
    
    def __init__(self):
        self.system = platform.system().lower()
        self.distro = self.get_linux_distro() if self.system == 'linux' else None
        
    def get_linux_distro(self):
        """Ermittelt die Linux-Distribution"""
        try:
            with open('/etc/os-release') as f:
                content = f.read().lower()
                if 'ubuntu' in content or 'debian' in content:
                    return 'debian'
                elif 'fedora' in content or 'rhel' in content or 'centos' in content:
                    return 'fedora'
                elif 'arch' in content:
                    return 'arch'
                else:
                    return 'unknown'
        except:
            return 'unknown'
    
    def run_command(self, command, description=""):
        """Führt einen Terminal-Befehl aus"""
        print(f"🔧 {description}")
        print(f"   Befehl: {command}")
        
        try:
            result = subprocess.run(command, shell=True, check=True, 
                                  capture_output=True, text=True)
            print(f"   ✅ Erfolgreich!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Fehler: {e}")
            print(f"   Output: {e.output}")
            return False
    
    def install_python_packages(self):
        """Installiert benötigte Python-Pakete"""
        print("\n📦 Python-Pakete installieren...")
        
        packages = [
            'pydub',
            'librosa',
            'soundfile',
            'numpy', 
            'matplotlib',
            'scipy',
            'jupyter',
            'ipywidgets'
        ]
        
        for package in packages:
            self.run_command(f"pip3 install {package}", f"Installiere {package}")
    
    def install_audio_tools(self):
        """Installiert Audio-Bearbeitungstools"""
        print("\n🎵 Audio-Tools installieren...")
        
        if self.system == 'linux':
            if self.distro == 'debian':
                commands = [
                    ("sudo apt update", "Package-Liste aktualisieren"),
                    ("sudo apt install -y audacity", "Audacity installieren"),
                    ("sudo apt install -y ffmpeg", "FFmpeg installieren"),
                    ("sudo apt install -y sox", "SoX Audio-Tools installieren"),
                    ("sudo apt install -y pulseaudio pavucontrol", "Audio-System installieren")
                ]
            elif self.distro == 'fedora':
                commands = [
                    ("sudo dnf update -y", "Package-Liste aktualisieren"),
                    ("sudo dnf install -y audacity", "Audacity installieren"),
                    ("sudo dnf install -y ffmpeg", "FFmpeg installieren"),
                    ("sudo dnf install -y sox", "SoX Audio-Tools installieren")
                ]
            elif self.distro == 'arch':
                commands = [
                    ("sudo pacman -Syu", "System aktualisieren"),
                    ("sudo pacman -S audacity", "Audacity installieren"),
                    ("sudo pacman -S ffmpeg", "FFmpeg installieren"),
                    ("sudo pacman -S sox", "SoX installieren")
                ]
            else:
                print("❌ Unbekannte Linux-Distribution!")
                return False
            
            for command, description in commands:
                self.run_command(command, description)
        
        elif self.system == 'darwin':  # macOS
            print("🍎 macOS erkannt - bitte installieren Sie Homebrew falls nicht vorhanden")
            commands = [
                ("brew install audacity", "Audacity installieren"),
                ("brew install ffmpeg", "FFmpeg installieren"),
                ("brew install sox", "SoX installieren")
            ]
            
            for command, description in commands:
                self.run_command(command, description)
        
        else:
            print("❌ Windows wird derzeit nicht unterstützt!")
            print("   Bitte installieren Sie manuell:")
            print("   - Audacity: https://www.audacityteam.org/")
            print("   - FFmpeg: https://ffmpeg.org/")
    
    def install_video_tools(self):
        """Installiert Video-Bearbeitungstools"""
        print("\n🎬 Video-Tools installieren...")
        
        if self.system == 'linux':
            if self.distro == 'debian':
                commands = [
                    ("sudo apt install -y blender", "Blender 3D installieren"),
                    ("sudo apt install -y kdenlive", "Kdenlive Video-Editor installieren"),
                    ("sudo apt install -y obs-studio", "OBS Studio installieren")
                ]
            elif self.distro == 'fedora':
                commands = [
                    ("sudo dnf install -y blender", "Blender installieren"),
                    ("sudo dnf install -y kdenlive", "Kdenlive installieren"),
                    ("sudo dnf install -y obs-studio", "OBS Studio installieren")
                ]
            elif self.distro == 'arch':
                commands = [
                    ("sudo pacman -S blender", "Blender installieren"),
                    ("sudo pacman -S kdenlive", "Kdenlive installieren"),
                    ("sudo pacman -S obs-studio", "OBS Studio installieren")
                ]
            else:
                print("❌ Unbekannte Linux-Distribution!")
                return False
                
            for command, description in commands:
                self.run_command(command, description)
        
        elif self.system == 'darwin':  # macOS
            commands = [
                ("brew install --cask blender", "Blender installieren"),
                ("brew install --cask obs", "OBS Studio installieren")
            ]
            
            for command, description in commands:
                self.run_command(command, description)
    
    def install_davinci_resolve(self):
        """Informationen zur DaVinci Resolve Installation"""
        print("\n🎨 DaVinci Resolve Installation:")
        print("   DaVinci Resolve muss manuell installiert werden:")
        print("   1. Besuchen Sie: https://www.blackmagicdesign.com/products/davinciresolve")
        print("   2. Laden Sie die kostenlose Version herunter")
        print("   3. Folgen Sie den Installationsanweisungen")
        print("   4. Erstellen Sie ein kostenloses Konto bei Blackmagic")
    
    def create_desktop_shortcuts(self):
        """Erstellt Desktop-Verknüpfungen"""
        print("\n🖥️ Desktop-Verknüpfungen erstellen...")
        
        if self.system == 'linux':
            desktop_path = Path.home() / "Desktop"
            desktop_path.mkdir(exist_ok=True)
            
            # Audacity Verknüpfung
            audacity_desktop = desktop_path / "Audacity.desktop"
            audacity_content = """[Desktop Entry]
Version=1.0
Type=Application
Name=Audacity
Comment=Audio-Editor für Voice-Over
Exec=audacity
Icon=audacity
Terminal=false
Categories=AudioVideo;Audio;
"""
            with open(audacity_desktop, 'w') as f:
                f.write(audacity_content)
            
            # Blender Verknüpfung
            blender_desktop = desktop_path / "Blender.desktop"
            blender_content = """[Desktop Entry]
Version=1.0
Type=Application
Name=Blender
Comment=3D-Software für Animationen
Exec=blender
Icon=blender
Terminal=false
Categories=Graphics;3DGraphics;
"""
            with open(blender_desktop, 'w') as f:
                f.write(blender_content)
            
            # Ausführbar machen
            os.chmod(audacity_desktop, 0o755)
            os.chmod(blender_desktop, 0o755)
            
            print("   ✅ Desktop-Verknüpfungen erstellt!")
    
    def setup_project_environment(self):
        """Richtet die Projektumgebung ein"""
        print("\n📁 Projektumgebung einrichten...")
        
        # Workspace-Pfad ermitteln
        current_dir = Path.cwd()
        
        # Zusätzliche Ordner erstellen
        folders = [
            'templates',
            'exports',
            'resources',
            'documentation'
        ]
        
        for folder in folders:
            folder_path = current_dir / folder
            folder_path.mkdir(exist_ok=True)
            print(f"   ✅ Ordner erstellt: {folder}")
        
        # Beispiel-Dateien erstellen
        examples_path = current_dir / "resources"
        
        # Audio-Beispiel Info
        audio_info = examples_path / "audio_info.txt"
        with open(audio_info, 'w') as f:
            f.write("""🎵 Audio-Beispiele

Unterstützte Formate:
- MP3 (für finale Ausgabe)
- WAV (für Bearbeitung)
- FLAC (verlustfrei)
- M4A (Apple)

Empfohlene Einstellungen:
- Sample Rate: 44.1 kHz oder 48 kHz
- Bit Depth: 16-bit oder 24-bit
- Mono für Voice-Over
- Stereo für Musik

Voice-Over Tipps:
- Ruhige Umgebung
- Gutes Mikrofon (USB oder XLR)
- Pop-Filter verwenden
- Gleichmäßiger Abstand zum Mikrofon
""")
        
        print("   ✅ Beispiel-Dateien erstellt!")
    
    def show_next_steps(self):
        """Zeigt nächste Schritte an"""
        print("\n🎯 Nächste Schritte:")
        print("=" * 50)
        print("1. 🎵 Audio-Projekt:")
        print("   - Legen Sie Ihre MP3-Datei in den 'audio' Ordner")
        print("   - Öffnen Sie scripts/audio_processor.py")
        print("   - Folgen Sie den Anweisungen im Skript")
        print()
        print("2. 🎬 Animation:")
        print("   - Öffnen Sie web-animation/motherboard.html im Browser")
        print("   - Für Video: Verwenden Sie OBS Studio zum Aufnehmen")
        print("   - Für 3D: Öffnen Sie Blender für erweiterte Animationen")
        print()
        print("3. 📝 Story:")
        print("   - Lesen Sie stories/spannende_geschichte.md")
        print("   - Üben Sie das Voice-Over mit Audacity")
        print("   - Kombinieren Sie Audio mit dem Python-Skript")
        print()
        print("4. 🚀 Produktion:")
        print("   - Nehmen Sie Voice-Over in Audacity auf")
        print("   - Verwenden Sie scripts/audio_processor.py zum Kombinieren")
        print("   - Nehmen Sie die Animation mit OBS auf")
        print("   - Bearbeiten Sie das finale Video in Kdenlive/DaVinci")

def main():
    """Hauptfunktion"""
    print("🛠️ Multimedia-Software Installer")
    print("=" * 50)
    print(f"System: {platform.system()} {platform.release()}")
    
    installer = MultimediaInstaller()
    
    print("\nWas möchten Sie installieren?")
    print("1. Alles (empfohlen)")
    print("2. Nur Python-Pakete")
    print("3. Nur Audio-Tools")
    print("4. Nur Video-Tools")
    print("5. Nur Projektumgebung einrichten")
    
    choice = input("\nWählen Sie eine Option (1-5): ").strip()
    
    if choice == "1":
        installer.install_python_packages()
        installer.install_audio_tools()
        installer.install_video_tools()
        installer.install_davinci_resolve()
        installer.create_desktop_shortcuts()
        installer.setup_project_environment()
        installer.show_next_steps()
        
    elif choice == "2":
        installer.install_python_packages()
        
    elif choice == "3":
        installer.install_audio_tools()
        
    elif choice == "4":
        installer.install_video_tools()
        installer.install_davinci_resolve()
        
    elif choice == "5":
        installer.setup_project_environment()
        installer.show_next_steps()
        
    else:
        print("❌ Ungültige Auswahl!")
        return
    
    print("\n🎉 Installation abgeschlossen!")
    print("   Öffnen Sie die README.md für weitere Informationen")

if __name__ == "__main__":
    main()