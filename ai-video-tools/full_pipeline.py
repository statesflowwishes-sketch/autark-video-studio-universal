#!/usr/bin/env python3
"""
🎬 Complete AI Video Pipeline
Erstellt automatisch längere Lernvideos aus Text-Skripten
"""

import os
import sys
import json
import subprocess
from pathlib import Path
import argparse
from typing import Optional, List

class AIVideoPipeline:
    """Komplette Pipeline für KI-Video-Erstellung"""
    
    def __init__(self, config_file: str = "configs/default.json"):
        self.config = self.load_config(config_file)
        self.project_root = Path.cwd()
        self.temp_dir = self.project_root / "temp-files"
        self.output_dir = self.project_root / "exports"
        
        # Ordner erstellen
        self.temp_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True)
    
    def load_config(self, config_file: str) -> dict:
        """Lädt Konfiguration"""
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"⚠️ Konfiguration {config_file} nicht gefunden, verwende Defaults")
            return {
                "video_settings": {"resolution": "1920x1080", "fps": 30},
                "ai_models": {
                    "text_to_speech": "coqui-tts",
                    "text_to_video": "stable-video-diffusion"
                }
            }
    
    def read_script(self, script_file: str) -> str:
        """Liest Text-Skript"""
        try:
            with open(script_file, 'r', encoding='utf-8') as f:
                content = f.read()
            print(f"📜 Skript geladen: {script_file}")
            return content
        except FileNotFoundError:
            print(f"❌ Skript-Datei nicht gefunden: {script_file}")
            sys.exit(1)
    
    def split_script_into_segments(self, script: str, max_length: int = 200) -> List[str]:
        """Teilt Skript in Segmente für bessere Verarbeitung"""
        # Einfache Segmentierung nach Absätzen oder Sätzen
        paragraphs = script.split('\n\n')
        segments = []
        
        for paragraph in paragraphs:
            if len(paragraph) <= max_length:
                segments.append(paragraph.strip())
            else:
                # Lange Absätze nach Sätzen aufteilen
                sentences = paragraph.split('. ')
                current_segment = ""
                
                for sentence in sentences:
                    if len(current_segment + sentence) <= max_length:
                        current_segment += sentence + ". "
                    else:
                        if current_segment:
                            segments.append(current_segment.strip())
                        current_segment = sentence + ". "
                
                if current_segment:
                    segments.append(current_segment.strip())
        
        print(f"📝 Skript in {len(segments)} Segmente aufgeteilt")
        return [seg for seg in segments if seg.strip()]
    
    def generate_speech(self, text: str, output_file: str) -> bool:
        """Generiert Sprache aus Text"""
        print(f"🗣️ Generiere Sprache: {output_file}")
        
        try:
            # Versuche Coqui TTS
            import tts
            from TTS.api import TTS
            
            # Deutsche Stimme verwenden
            model_name = "tts_models/de/thorsten/tacotron2-DDC"
            tts = TTS(model_name)
            tts.tts_to_file(text=text, file_path=output_file)
            
            print(f"   ✅ Sprache generiert mit Coqui TTS")
            return True
            
        except ImportError:
            print("   ⚠️ Coqui TTS nicht verfügbar, verwende Alternative")
            
            try:
                # Fallback: gTTS (Google TTS)
                from gtts import gTTS
                tts = gTTS(text=text, lang='de')
                tts.save(output_file)
                print(f"   ✅ Sprache generiert mit Google TTS")
                return True
                
            except ImportError:
                print("   ❌ Keine TTS-Engine verfügbar!")
                return False
    
    def generate_video_segment(self, prompt: str, output_file: str, duration: int = 10) -> bool:
        """Generiert Video-Segment aus Text-Prompt"""
        print(f"🎬 Generiere Video-Segment: {prompt[:50]}...")
        
        try:
            # Placeholder für KI-Video-Generation
            # In der Praxis würden hier Stable Video Diffusion o.ä. verwendet
            
            # Für Demo: Erstelle einfaches Video mit Text-Overlay
            import cv2
            import numpy as np
            
            # Video-Parameter
            fps = self.config["video_settings"]["fps"]
            width, height = 1920, 1080
            frames = duration * fps
            
            # Video-Writer erstellen
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
            
            for frame_num in range(frames):
                # Einfacher Hintergrund mit Farbverlauf
                frame = np.zeros((height, width, 3), dtype=np.uint8)
                
                # Animierter Hintergrund
                color_intensity = int(127 + 127 * np.sin(frame_num * 0.1))
                frame[:, :] = [color_intensity // 3, color_intensity // 2, color_intensity]
                
                # Text hinzufügen
                font = cv2.FONT_HERSHEY_SIMPLEX
                text_lines = self.wrap_text(prompt, 60)
                
                y_start = height // 2 - len(text_lines) * 25
                for i, line in enumerate(text_lines):
                    y = y_start + i * 50
                    cv2.putText(frame, line, (50, y), font, 1, (255, 255, 255), 2)
                
                out.write(frame)
            
            out.release()
            print(f"   ✅ Video-Segment erstellt (Demo-Version)")
            return True
            
        except Exception as e:
            print(f"   ❌ Fehler bei Video-Generierung: {e}")
            return False
    
    def wrap_text(self, text: str, width: int) -> List[str]:
        """Bricht Text in Zeilen um"""
        words = text.split()
        lines = []
        current_line = ""
        
        for word in words:
            if len(current_line + " " + word) <= width:
                current_line += " " + word if current_line else word
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        
        if current_line:
            lines.append(current_line)
        
        return lines
    
    def combine_segments(self, audio_files: List[str], video_files: List[str], 
                        output_file: str) -> bool:
        """Kombiniert Audio- und Video-Segmente zu einem Video"""
        print(f"🔗 Kombiniere {len(audio_files)} Segmente zu finalem Video...")
        
        try:
            # Verwende moviepy für die Kombination
            from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
            
            clips = []
            
            for i, (video_file, audio_file) in enumerate(zip(video_files, audio_files)):
                if os.path.exists(video_file) and os.path.exists(audio_file):
                    print(f"   Verarbeite Segment {i+1}/{len(video_files)}")
                    
                    # Video und Audio laden
                    video_clip = VideoFileClip(video_file)
                    audio_clip = AudioFileClip(audio_file)
                    
                    # Audio zur Video-Länge anpassen oder umgekehrt
                    if audio_clip.duration > video_clip.duration:
                        video_clip = video_clip.loop(duration=audio_clip.duration)
                    else:
                        audio_clip = audio_clip.loop(duration=video_clip.duration)
                    
                    # Audio zu Video hinzufügen
                    final_clip = video_clip.set_audio(audio_clip)
                    clips.append(final_clip)
                    
                else:
                    print(f"   ⚠️ Segment {i+1} übersprungen (Dateien fehlen)")
            
            if clips:
                # Alle Clips zusammenfügen
                final_video = concatenate_videoclips(clips)
                final_video.write_videofile(output_file, codec='libx264', audio_codec='aac')
                
                # Aufräumen
                for clip in clips:
                    clip.close()
                final_video.close()
                
                print(f"   ✅ Finales Video erstellt: {output_file}")
                return True
            else:
                print("   ❌ Keine Clips zum Kombinieren gefunden!")
                return False
                
        except ImportError:
            print("   ❌ moviepy nicht verfügbar! Installieren Sie: pip install moviepy")
            return False
        except Exception as e:
            print(f"   ❌ Fehler beim Kombinieren: {e}")
            return False
    
    def enhance_with_pc_animation(self, video_file: str, output_file: str) -> bool:
        """Erweitert Video mit PC-Animation aus dem web-animation Ordner"""
        print("🖥️ Erweitere Video mit PC-Animation...")
        
        try:
            # Prüfe ob Motherboard-Animation existiert
            animation_file = self.project_root / "web-animation" / "motherboard.html"
            
            if animation_file.exists():
                print("   💡 Tipp: Nehmen Sie die PC-Animation mit OBS Studio auf")
                print("   💡 Dann können Sie sie mit diesem Video kombinieren")
                
                # Für Demo: Kopiere das Original-Video
                import shutil
                shutil.copy2(video_file, output_file)
                
                print(f"   ✅ Video bereit für manuelle PC-Animation-Integration")
                return True
            else:
                print("   ⚠️ PC-Animation nicht gefunden, kopiere Original")
                import shutil
                shutil.copy2(video_file, output_file)
                return True
                
        except Exception as e:
            print(f"   ❌ Fehler bei PC-Animation-Integration: {e}")
            return False
    
    def run_pipeline(self, script_file: str, output_name: str, 
                    style: str = "educational", duration_per_segment: int = 10) -> str:
        """Führt komplette Pipeline aus"""
        print(f"🚀 Starte KI-Video-Pipeline für: {script_file}")
        print("=" * 60)
        
        # 1. Skript laden und segmentieren
        script = self.read_script(script_file)
        segments = self.split_script_into_segments(script)
        
        if not segments:
            print("❌ Keine Segmente zum Verarbeiten!")
            return ""
        
        # 2. Audio und Video für jedes Segment generieren
        audio_files = []
        video_files = []
        
        for i, segment in enumerate(segments):
            print(f"\n📹 Verarbeite Segment {i+1}/{len(segments)}")
            
            # Audio generieren
            audio_file = self.temp_dir / f"audio_segment_{i+1:03d}.wav"
            if self.generate_speech(segment, str(audio_file)):
                audio_files.append(str(audio_file))
            
            # Video generieren
            video_file = self.temp_dir / f"video_segment_{i+1:03d}.mp4"
            video_prompt = f"{style} video: {segment[:100]}..."
            if self.generate_video_segment(video_prompt, str(video_file), duration_per_segment):
                video_files.append(str(video_file))
        
        # 3. Segmente kombinieren
        if audio_files and video_files:
            combined_file = self.temp_dir / f"combined_{output_name}.mp4"
            if self.combine_segments(audio_files, video_files, str(combined_file)):
                
                # 4. Mit PC-Animation erweitern (optional)
                final_file = self.output_dir / f"{output_name}.mp4"
                if self.enhance_with_pc_animation(str(combined_file), str(final_file)):
                    print(f"\n🎉 Pipeline abgeschlossen!")
                    print(f"📁 Finales Video: {final_file}")
                    return str(final_file)
        
        print("\n❌ Pipeline fehlgeschlagen!")
        return ""
    
    def cleanup_temp_files(self):
        """Löscht temporäre Dateien"""
        import shutil
        try:
            if self.temp_dir.exists():
                shutil.rmtree(self.temp_dir)
                self.temp_dir.mkdir()
            print("🧹 Temporäre Dateien gelöscht")
        except Exception as e:
            print(f"⚠️ Cleanup-Warnung: {e}")

def main():
    """Hauptfunktion"""
    parser = argparse.ArgumentParser(description="KI-Video-Pipeline")
    parser.add_argument("--script", required=True, help="Pfad zum Text-Skript")
    parser.add_argument("--output", default="ai_generated_video", help="Name des Ausgabe-Videos")
    parser.add_argument("--style", default="educational", help="Video-Stil")
    parser.add_argument("--duration", type=int, default=10, help="Dauer pro Segment (Sekunden)")
    parser.add_argument("--config", default="configs/default.json", help="Konfigurationsdatei")
    parser.add_argument("--cleanup", action="store_true", help="Temporäre Dateien nach Verarbeitung löschen")
    
    args = parser.parse_args()
    
    # Pipeline initialisieren und ausführen
    pipeline = AIVideoPipeline(args.config)
    
    result = pipeline.run_pipeline(
        script_file=args.script,
        output_name=args.output,
        style=args.style,
        duration_per_segment=args.duration
    )
    
    if result:
        print(f"\n✅ Erfolgreich erstellt: {result}")
        
        # Zusätzliche Informationen
        print("\n💡 Nächste Schritte:")
        print("1. Video in einem Player ansehen")
        print("2. Bei Bedarf mit Video-Editor nachbearbeiten")
        print("3. PC-Animation aus web-animation/motherboard.html aufnehmen")
        print("4. Beides in einem Video-Editor kombinieren")
        
        if args.cleanup:
            pipeline.cleanup_temp_files()
    else:
        print("\n❌ Video-Erstellung fehlgeschlagen!")
        sys.exit(1)

if __name__ == "__main__":
    main()