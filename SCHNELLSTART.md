# 🚀 Schnellstart-Anleitung

## 1. 🎵 Ihr Audio-Projekt mit der Hintergrundmusik

### Schritt 1: Audio-Datei kopieren
```bash
# Kopieren Sie Ihre MP3-Datei in den audio Ordner:
cp "/home/holythreekingstreescrowns/Downloads/Unbenannter Song.mp3" audio/
```

### Schritt 2: Software installieren (einmalig)
```bash
# Führen Sie den Installer aus:
python3 scripts/install_software.py
```

### Schritt 3: Voice-Over aufnehmen
1. Öffnen Sie **Audacity**
2. Nehmen Sie Ihre Stimme auf (basierend auf `stories/spannende_geschichte.md`)
3. Speichern Sie als `voice_over.wav` im `audio` Ordner

### Schritt 4: Audio kombinieren
```bash
# Führen Sie den Audio-Processor aus:
python3 scripts/audio_processor.py
```

## 2. 🖥️ PC-Animation ansehen

### Sofort starten:
Öffnen Sie `web-animation/motherboard.html` in Ihrem Browser!

### Features der Animation:
- ✨ Leuchtende CPU, RAM und GPU Module
- 🔄 Sich bewegende Datenströme
- 💡 Pulsierende LED-Effekte
- 📊 Live System-Status
- 🖱️ Interaktive Elemente (hover über CPU)
- 🔍 Vollbild mit Doppelklick

## 3. 🎬 Video aufnehmen

### Mit OBS Studio:
1. Starten Sie OBS Studio
2. Fügen Sie "Browser-Quelle" hinzu
3. URL: `file:///pfad/zu/ihrem/projekt/web-animation/motherboard.html`
4. Audio-Quelle: Ihr kombiniertes Audio
5. Aufnahme starten!

### Alternativen:
- **SimpleScreenRecorder** (Linux)
- **Kazam** (Ubuntu)
- **Browser-Extension** für Chrome/Firefox

## 4. 📝 Story-Timing

Die Geschichte in `stories/spannende_geschichte.md` ist perfekt auf **4:30 Minuten** abgestimmt:

| Kapitel | Dauer | Stil |
|---------|-------|------|
| Prolog | 30s | Mysteriös |
| Kapitel 1 | 45s | Spannend |
| Kapitel 2 | 40s | Dramatisch |
| Kapitel 3 | 50s | Abenteuerlich |
| Kapitel 4 | 45s | Kämpferisch |
| Epilog | 35s | Hoffnungsvoll |

## 5. ⚡ Blitz-Workflow

```bash
# 1. Alles auf einmal installieren
python3 scripts/install_software.py

# 2. Animation im Browser öffnen
firefox web-animation/motherboard.html

# 3. Audio bearbeiten
audacity audio/Unbenannter\ Song.mp3

# 4. Voice-Over hinzufügen
python3 scripts/audio_processor.py
```

## 6. 🎯 Finale Produktion

1. **Voice-Over**: Nehmen Sie die Geschichte mit Audacity auf
2. **Audio-Mix**: Kombinieren Sie mit dem Python-Skript
3. **Video**: Nehmen Sie die Animation mit OBS auf
4. **Editing**: Kombinieren Sie alles in Kdenlive oder DaVinci Resolve

## 7. 💡 Profi-Tipps

### Audio-Qualität:
- Ruhige Umgebung
- Gutes Mikrofon
- Pop-Filter verwenden
- Gleichmäßiger Abstand

### Animation-Timing:
- Synchronisieren Sie mit Musik-Beats
- Nutzen Sie Pausen für Spannung
- Variieren Sie die Intensität

### Video-Export:
- 1080p oder 4K Resolution
- 30fps für smooth animation
- H.264 für beste Kompatibilität

---

## 🚨 Troubleshooting

### Python-Fehler:
```bash
pip3 install --upgrade pip
pip3 install pydub librosa soundfile numpy matplotlib
```

### Audio-Probleme:
```bash
sudo apt install ffmpeg sox pulseaudio
```

### Browser-Animation lädt nicht:
- Verwenden Sie Firefox oder Chrome
- Öffnen Sie mit `file://` URL
- Prüfen Sie JavaScript-Konsole (F12)

---

**🎉 Viel Erfolg mit Ihrem Multimedia-Projekt!**