# 🤖 KI-Video-Pipeline Demo

Vollautomatische Lernvideo-Erstellung mit 33+ Open-Source-Tools

## 🎯 Was ist das?

Ein komplettes Setup zur automatischen Erstellung von **längeren Lernvideos** aus Text-Skripten mit:
- ✅ Text-to-Speech (Sprache generieren)
- ✅ Text-to-Video (KI-Videos erstellen) 
- ✅ PC-Motherboard Animation (bereits vorhanden)
- ✅ Automatisches Kombinieren zu langen Videos
- ✅ 33+ Open-Source KI-Tools integriert

---

## 🚀 Schnellstart (5 Minuten)

### 1. **Alles installieren:**
```bash
cd ai-video-tools
python3 install_ai_tools.py
```

### 2. **Erstes Video erstellen:**
```bash
# Ihre Geschichte als Lernvideo
python3 full_pipeline.py \
  --script "../stories/spannende_geschichte.md" \
  --output "mein_erstes_ki_video" \
  --style "futuristic tutorial"
```

### 3. **Video ansehen:**
```bash
# Finales Video wird erstellt in:
# exports/mein_erstes_ki_video.mp4
```

---

## 📁 Projekt-Übersicht

```
📁 Ihr Multimedia-Projekt/
├── 🤖 ai-video-tools/          # KI-Video-Pipeline
│   ├── install_ai_tools.py     # Installiert alle 33+ Tools
│   ├── full_pipeline.py        # Komplette Video-Pipeline
│   ├── text-to-speech/         # TTS-Tools (Coqui, Bark, etc.)
│   ├── text-to-video/          # Video-KI (Stable Video, etc.)
│   └── remotion-project/       # React-basierte Videos
├── 🎭 stories/                 # Ihre Geschichten & Skripte
├── 🖥️ web-animation/           # PC-Motherboard Animation
├── 📁 exports/                 # Fertige Videos
├── 🛠️ scripts/                # Original Audio-Tools
└── 📚 templates/               # Vorlagen
```

---

## 🎬 Verwendung der 33+ KI-Tools

### **End-to-End Frameworks:**
```bash
# Remotion (React-Videos, ∞ Länge)
cd ai-video-tools/remotion-project
npx create-remotion-video

# MoviePy (Python, Video+Audio)
python3 -c "
from moviepy.editor import *
clip = VideoFileClip('input.mp4')
clip.write_videofile('output.mp4')
"

# Manim (Mathematische Animationen)
pip install manim
manim -pql scene.py MyMathScene
```

### **Text-to-Video KI-Modelle:**
```bash
# HunyuanVideo (Tencent, sehr stark)
huggingface-cli download Tencent-Hunyuan/HunyuanVideo

# Stable Video Diffusion
python3 text-to-video/stable_video_demo.py

# AnimateDiff (Bild-Sequenzen)
python3 text-to-video/animate_diff_demo.py

# CogVideo (Transformer-basiert)
python3 text-to-video/cogvideo_demo.py
```

### **Text-to-Speech:**
```bash
# Coqui TTS (Multi-language)
python3 text-to-speech/coqui_demo.py --text "Hallo Welt" --lang de

# Bark (KI-Stimmen mit Emotionen)
python3 text-to-speech/bark_demo.py --text "Spannende Geschichte!"

# ESPnet-TTS (Deep Learning)
python3 text-to-speech/espnet_demo.py
```

---

## 🎯 Workflow-Beispiele

### **Workflow 1: Automatisches Tutorial**
```bash
# 1. Schreiben Sie tutorial.txt
echo "Heute lernen wir Python. Zuerst..." > tutorial.txt

# 2. Vollautomatisch zu Video
python3 full_pipeline.py --script tutorial.txt --style "educational"

# 3. Fertig! Video in exports/
```

### **Workflow 2: Mit PC-Animation kombiniert**
```bash
# 1. Ihre Geschichte + PC-Animation
python3 full_pipeline.py \
  --script "stories/spannende_geschichte.md" \
  --style "futuristic computer tutorial" \
  --duration 15

# 2. PC-Animation separat aufnehmen (OBS Studio)
# web-animation/motherboard.html im Browser
# Mit OBS aufnehmen als pc_animation.mp4

# 3. Beide Videos kombinieren
python3 combine_with_pc_animation.py \
  --main-video "exports/video.mp4" \
  --pc-animation "pc_animation.mp4" \
  --output "final_combo.mp4"
```

### **Workflow 3: Längeres Lernvideo (10+ Minuten)**
```bash
# 1. Großes Skript in Kapitel aufteilen
python3 split_long_script.py --input "long_tutorial.md" --chapters 5

# 2. Jedes Kapitel einzeln verarbeiten
for i in {1..5}; do
  python3 full_pipeline.py --script "chapter_$i.txt" --output "part_$i"
done

# 3. Alle Teile kombinieren
python3 combine_chapters.py --parts "part_*.mp4" --output "complete_course.mp4"
```

---

## 🛠️ Tool-Details

### **33+ Tools nach Kategorien:**

#### **1. Video-Frameworks (für lange Videos):**
- **Remotion** - React-basiert, ∞ Länge ⭐⭐⭐⭐⭐
- **MoviePy** - Python, sehr flexibel ⭐⭐⭐⭐⭐
- **Manim** - Mathematik/Wissenschaft ⭐⭐⭐⭐
- **OpenShot** - GUI + Scripting ⭐⭐⭐

#### **2. KI Text-to-Video:**
- **HunyuanVideo** - Tencent, top Qualität ⭐⭐⭐⭐⭐
- **Stable Video Diffusion** - Stability AI ⭐⭐⭐⭐
- **CogVideo** - Transformer-basiert ⭐⭐⭐⭐
- **AnimateDiff** - Bild-Animation ⭐⭐⭐⭐
- **VideoCrafter2** - Diffusion ⭐⭐⭐
- **Pika Labs** - Multi-Modal ⭐⭐⭐
- **Mochi-1** - Kompakt ⭐⭐⭐
- **SkyReels-V1** - Open Source ⭐⭐⭐

#### **3. Text-to-Speech:**
- **Coqui TTS** - Multi-language ⭐⭐⭐⭐⭐
- **Bark** - Emotionale Stimmen ⭐⭐⭐⭐
- **ESPnet-TTS** - Deep Learning ⭐⭐⭐⭐

#### **4. Orchestrierung:**
- **BentoML** - Model Serving ⭐⭐⭐⭐
- **Haystack** - Q&A Integration ⭐⭐⭐
- **DeepLake** - Data Management ⭐⭐⭐

---

## 💡 Performance-Tipps

### **GPU-Beschleunigung:**
```bash
# Prüfen Sie GPU-Verfügbarkeit
nvidia-smi

# CUDA für PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Modelle auf GPU laden
export CUDA_VISIBLE_DEVICES=0
```

### **Memory-Optimierung:**
```bash
# Große Modelle in Segmenten verarbeiten
python3 full_pipeline.py --batch-size 1 --max-length 100

# Temp-Files regelmäßig löschen
python3 full_pipeline.py --cleanup
```

### **Qualitäts-Einstellungen:**
```json
// configs/high_quality.json
{
  "video_settings": {
    "resolution": "1920x1080",
    "fps": 30,
    "bitrate": "5M",
    "codec": "h264"
  },
  "ai_models": {
    "text_to_video": "hunyuan-video",
    "text_to_speech": "coqui-tts-high",
    "quality_level": "high"
  }
}
```

---

## 🎯 Für Ihr PC-Motherboard Projekt

### **Erweiterte PC-Animation:**
```bash
# 1. Bestehende Animation erweitern
python3 enhance_pc_animation.py \
  --input "web-animation/motherboard.html" \
  --ai-enhancement "stable-video-diffusion" \
  --style "cyberpunk futuristic computer" \
  --duration 60

# 2. Mit Ihrer Geschichte kombinieren
python3 full_pipeline.py \
  --script "stories/spannende_geschichte.md" \
  --background-animation "enhanced_pc.mp4" \
  --style "tech narrative"

# 3. Audio aus Downloads hinzufügen
python3 add_background_music.py \
  --video "exports/tech_story.mp4" \
  --music "/home/holythreekingstreescrowns/Downloads/Unbenannter Song.mp3" \
  --mix-level 0.3
```

---

## 🚀 Live-Demo starten

```bash
# Sofort verfügbare Demo:
python3 full_pipeline.py \
  --script "../stories/spannende_geschichte.md" \
  --output "demo_video" \
  --style "futuristic tutorial" \
  --duration 10

# Ergebnis: exports/demo_video.mp4
```

---

**🎉 Ready für professionelle KI-Lernvideo-Produktion!**