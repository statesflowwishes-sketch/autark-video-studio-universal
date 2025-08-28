# 🤖 KI-Video-Pipeline für längere Lernvideos

Basierend auf den 33+ Open-Source-KI-Tools für automatische Videogenerierung.

## 🎯 Ziel: Vollautomatische Lernvideo-Erstellung

### Workflow:
1. **Text-Skript** → 2. **TTS (Sprache)** → 3. **KI-Video** → 4. **Kombinieren** → 5. **Langes Lernvideo**

---

## 🛠️ Tool-Kategorien und Installation

### 1. **End-to-End Frameworks (für längere Videos)**
```bash
# Remotion (React-basiert, beliebig lange Videos)
npm install -g @remotion/cli
npx create-remotion-video

# MoviePy (Python, Video+Audio+Slides)
pip install moviepy

# Manim (Mathematische Lernvideos)
pip install manim
```

### 2. **Text-to-Speech (Hochwertige Sprache)**
```bash
# Coqui TTS (Multi-language, flexibel)
pip install coqui-tts

# Bark (Modernes KI-TTS, Emotionen)
pip install bark-voice

# ESPnet-TTS (Deep Learning)
pip install espnet-tts
```

### 3. **Text-to-Video KI-Modelle**
```bash
# HunyuanVideo (Tencent, sehr leistungsstark)
pip install huggingface-hub transformers torch
huggingface-cli download Tencent-Hunyuan/HunyuanVideo

# Stable Video Diffusion
pip install diffusers transformers accelerate
pip install stable-video-diffusion

# AnimateDiff (Bild-Sequenz Animation)
pip install animatediff

# CogVideo (Transformer-basiert)
pip install cogvideo
```

### 4. **Video-Processing & Orchestrierung**
```bash
# BentoML (Modell-Serving, Pipelines)
pip install bentoml

# OpenCV (Video/Bildverarbeitung)
pip install opencv-python

# PySceneDetect (Szenenerkennung)
pip install scenedetect
```

---

## 📋 Installations-Skript

Das `scripts/install_ai_tools.py` installiert automatisch alle benötigten Tools:

```python
# Siehe ai-video-tools/install_ai_tools.py
python3 ai-video-tools/install_ai_tools.py
```

---

## 🎬 Beispiel-Workflows

### **Workflow 1: Automatisches Lernvideo**
```bash
# 1. Skript schreiben
echo "Willkommen zu unserem Python-Tutorial..." > script.txt

# 2. TTS generieren
python3 ai-video-tools/text-to-speech/generate_tts.py --input script.txt --output audio.wav

# 3. Video-Segmente erstellen
python3 ai-video-tools/text-to-video/generate_video.py --prompt "Python Tutorial" --duration 30

# 4. Alles kombinieren
python3 ai-video-tools/combine_video.py --audio audio.wav --video segments/ --output final_tutorial.mp4
```

### **Workflow 2: Remotion-basiert (React)**
```bash
cd ai-video-tools/remotion-project
npm run build
npm run render
```

### **Workflow 3: Manim (Mathematik/Wissenschaft)**
```bash
cd ai-video-tools/manim-project
manim -pql scene.py MyScene
```

---

## 🔄 Pipeline-Automatisierung

### **Alles-in-einem Skript:**
```bash
# Komplette Pipeline ausführen
python3 ai-video-tools/full_pipeline.py \
  --script "stories/spannende_geschichte.md" \
  --style "futuristic" \
  --duration 300 \
  --output "exports/complete_video.mp4"
```

---

## 📊 Tool-Vergleich für längere Videos

| Tool | Länge | Qualität | Automatisierung | Lizenz |
|------|-------|----------|-----------------|--------|
| **Remotion** | ∞ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | MIT |
| **MoviePy** | ∞ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | MIT |
| **HunyuanVideo** | 10s + | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | MIT |
| **Stable Video** | 4s + | ⭐⭐⭐⭐ | ⭐⭐⭐ | MIT |
| **Manim** | ∞ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | MIT |

---

## 🎯 Speziell für Ihr PC-Motherboard Projekt

### **KI-erweiterte PC-Animation:**
```bash
# 1. Bestehende Web-Animation als Basis verwenden
# 2. Mit Stable Video Diffusion erweitern
python3 ai-video-tools/enhance_pc_animation.py \
  --input "web-animation/motherboard.html" \
  --ai-model "stable-video-diffusion" \
  --prompt "futuristic computer motherboard with glowing circuits" \
  --duration 60

# 3. Mit TTS kombinieren
python3 ai-video-tools/add_narration.py \
  --video "enhanced_pc_animation.mp4" \
  --script "stories/spannende_geschichte.md" \
  --voice "bark" \
  --output "exports/final_pc_story.mp4"
```

---

## 🚀 Nächste Schritte

1. **Tool-Installation:** `python3 ai-video-tools/install_ai_tools.py`
2. **Erste Tests:** Einzelne Tools ausprobieren
3. **Pipeline-Setup:** Vollautomatische Workflow erstellen
4. **Optimierung:** GPU-Beschleunigung, Batch-Processing
5. **Produktion:** Längere Lernvideos erstellen

---

## 💡 Erweiterte Features

- **Interaktive Elemente:** Haystack für Q&A-Module
- **Mehrsprachigkeit:** Automatische Übersetzung + TTS
- **Batch-Processing:** Mehrere Videos parallel
- **Cloud-Deployment:** BentoML für skalierbare Pipelines
- **Live-Streaming:** Real-time Video-Generation

---

**Bereit für KI-gestützte Lernvideo-Produktion!** 🎬🤖