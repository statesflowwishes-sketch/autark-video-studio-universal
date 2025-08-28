#!/usr/bin/env python3
"""
🎵 Audio Processor für Voice-Over Projekte
Kombiniert Voice-Over mit Hintergrundmusik und fügt Effekte hinzu.
"""

import os
import sys
import numpy as np
from pathlib import Path

# Installationscheck für benötigte Bibliotheken
def check_dependencies():
    """Überprüft und installiert benötigte Python-Bibliotheken"""
    required_packages = [
        'pydub',
        'librosa', 
        'soundfile',
        'numpy',
        'matplotlib'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} ist installiert")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package} fehlt")
    
    if missing_packages:
        print(f"\n📦 Installiere fehlende Pakete:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    return True

# Audio-Processing Klasse
class AudioProcessor:
    """Hauptklasse für Audio-Bearbeitung"""
    
    def __init__(self, project_path="."):
        self.project_path = Path(project_path)
        self.audio_path = self.project_path / "audio"
        self.output_path = self.project_path / "output"
        
        # Ordner erstellen falls nicht vorhanden
        self.audio_path.mkdir(exist_ok=True)
        self.output_path.mkdir(exist_ok=True)
    
    def combine_voice_and_music(self, voice_file, music_file, output_file, 
                               music_volume=0.3, fade_in=2, fade_out=3):
        """
        Kombiniert Voice-Over mit Hintergrundmusik
        
        Args:
            voice_file: Pfad zur Voice-Over Datei
            music_file: Pfad zur Hintergrundmusik
            output_file: Pfad für die fertige Datei
            music_volume: Lautstärke der Musik (0.0-1.0)
            fade_in: Fade-In Dauer in Sekunden
            fade_out: Fade-Out Dauer in Sekunden
        """
        try:
            from pydub import AudioSegment
            
            # Audio-Dateien laden
            voice = AudioSegment.from_file(voice_file)
            music = AudioSegment.from_file(music_file)
            
            # Musik an Voice-Over Länge anpassen
            if len(music) < len(voice):
                # Musik wiederholen falls zu kurz
                repetitions = (len(voice) // len(music)) + 1
                music = music * repetitions
            
            # Musik auf Voice-Over Länge zuschneiden
            music = music[:len(voice)]
            
            # Musik-Lautstärke reduzieren
            music = music - (20 - int(music_volume * 20))  # dB Reduktion
            
            # Fade-Effekte hinzufügen
            music = music.fade_in(fade_in * 1000).fade_out(fade_out * 1000)
            
            # Voice-Over und Musik kombinieren
            final_audio = voice.overlay(music)
            
            # Datei exportieren
            output_path = self.output_path / output_file
            final_audio.export(output_path, format="mp3")
            
            print(f"✅ Audio erfolgreich kombiniert: {output_path}")
            return str(output_path)
            
        except ImportError:
            print("❌ pydub nicht installiert. Bitte installieren Sie: pip install pydub")
            return None
        except Exception as e:
            print(f"❌ Fehler beim Kombinieren: {e}")
            return None
    
    def add_silence_pauses(self, audio_file, pause_positions, pause_duration=2):
        """
        Fügt Pausen an bestimmten Positionen hinzu
        
        Args:
            audio_file: Pfad zur Audio-Datei
            pause_positions: Liste von Zeitpositionen (in Sekunden)
            pause_duration: Dauer der Pausen in Sekunden
        """
        try:
            from pydub import AudioSegment
            
            audio = AudioSegment.from_file(audio_file)
            silence = AudioSegment.silent(duration=pause_duration * 1000)
            
            # Sortiere Positionen rückwärts für korrekte Insertion
            positions = sorted(pause_positions, reverse=True)
            
            for pos in positions:
                pos_ms = pos * 1000
                if pos_ms <= len(audio):
                    audio = audio[:pos_ms] + silence + audio[pos_ms:]
            
            output_file = self.output_path / f"paused_{Path(audio_file).name}"
            audio.export(output_file, format="mp3")
            
            print(f"✅ Pausen hinzugefügt: {output_file}")
            return str(output_file)
            
        except Exception as e:
            print(f"❌ Fehler beim Hinzufügen von Pausen: {e}")
            return None
    
    def analyze_audio(self, audio_file):
        """
        Analysiert Audio-Datei und zeigt Informationen an
        """
        try:
            import librosa
            import matplotlib.pyplot as plt
            
            # Audio laden
            y, sr = librosa.load(audio_file)
            duration = len(y) / sr
            
            print(f"\n📊 Audio-Analyse für: {Path(audio_file).name}")
            print(f"   Dauer: {duration:.2f} Sekunden")
            print(f"   Sample Rate: {sr} Hz")
            print(f"   Samples: {len(y)}")
            
            # Visualisierung erstellen
            plt.figure(figsize=(12, 6))
            
            # Waveform
            plt.subplot(2, 1, 1)
            time = np.linspace(0, duration, len(y))
            plt.plot(time, y)
            plt.title('Waveform')
            plt.xlabel('Zeit (s)')
            plt.ylabel('Amplitude')
            
            # Spektrogramm
            plt.subplot(2, 1, 2)
            D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
            librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='hz')
            plt.colorbar(format='%+2.0f dB')
            plt.title('Spektrogramm')
            
            plt.tight_layout()
            
            # Analyse speichern
            analysis_file = self.output_path / f"analysis_{Path(audio_file).stem}.png"
            plt.savefig(analysis_file)
            print(f"   Analyse gespeichert: {analysis_file}")
            
            return {
                'duration': duration,
                'sample_rate': sr,
                'samples': len(y),
                'analysis_image': str(analysis_file)
            }
            
        except ImportError:
            print("❌ librosa oder matplotlib nicht installiert")
            print("   Installieren Sie: pip install librosa matplotlib")
            return None
        except Exception as e:
            print(f"❌ Fehler bei der Analyse: {e}")
            return None

def main():
    """Hauptfunktion für Kommandozeilen-Nutzung"""
    print("🎵 Audio Processor für Voice-Over Projekte")
    print("=" * 50)
    
    # Dependencies checken
    if not check_dependencies():
        print("\n❌ Bitte installieren Sie zuerst die fehlenden Pakete!")
        return
    
    # Audio Processor initialisieren
    processor = AudioProcessor()
    
    # Beispiel-Workflow
    print("\n📋 Verfügbare Funktionen:")
    print("1. Voice-Over mit Musik kombinieren")
    print("2. Pausen hinzufügen")
    print("3. Audio analysieren")
    print("4. Beispiel-Workflow ausführen")
    
    choice = input("\nWählen Sie eine Option (1-4): ")
    
    if choice == "1":
        voice_file = input("Pfad zur Voice-Over Datei: ")
        music_file = input("Pfad zur Musik-Datei: ")
        output_name = input("Name der Ausgabe-Datei: ")
        
        if os.path.exists(voice_file) and os.path.exists(music_file):
            processor.combine_voice_and_music(voice_file, music_file, output_name)
        else:
            print("❌ Eine der Dateien existiert nicht!")
    
    elif choice == "2":
        audio_file = input("Pfad zur Audio-Datei: ")
        if os.path.exists(audio_file):
            # Beispiel-Pausen bei 10, 25, 40 Sekunden
            processor.add_silence_pauses(audio_file, [10, 25, 40])
        else:
            print("❌ Datei existiert nicht!")
    
    elif choice == "3":
        audio_file = input("Pfad zur Audio-Datei: ")
        if os.path.exists(audio_file):
            processor.analyze_audio(audio_file)
        else:
            print("❌ Datei existiert nicht!")
    
    elif choice == "4":
        print("\n🚀 Beispiel-Workflow wird ausgeführt...")
        print("   Legen Sie Ihre Audio-Dateien in den 'audio' Ordner")
        print("   Die fertigen Dateien finden Sie im 'output' Ordner")
        
        # Liste verfügbare Audio-Dateien
        audio_files = list(processor.audio_path.glob("*.mp3")) + \
                     list(processor.audio_path.glob("*.wav"))
        
        if audio_files:
            print(f"\n📁 Gefundene Audio-Dateien:")
            for i, file in enumerate(audio_files):
                print(f"   {i+1}. {file.name}")
        else:
            print("❌ Keine Audio-Dateien im 'audio' Ordner gefunden!")

if __name__ == "__main__":
    main()