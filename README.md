# 🏠 AI Smart Home Assistant (Bilingual Voice & GUI-based)

A Python-based smart assistant for home control that responds to both **voice** and **text** commands in **English** and **Bangla**. Supports control of lights, fan, and AC, weather queries, reminders, and live traffic info with map display.

---

## 🌟 Features

### 🔊 Voice Recognition
- English and Bangla language support
- Command processing and intent detection
- Dynamic speech output using pyttsx3 (English) and gTTS (Bangla)

### 🧠 Core Functionalities
- ✅ Toggle devices: light, fan, AC
- ✅ Device status queries
- ✅ Weather updates by city
- ✅ Add and list reminders
- ✅ Get traffic info and map from Google Maps API

### 🖼 GUI
- Tkinter-based responsive interface
- Output box for assistant response
- Static map display for traffic queries
- Voice command button

---

## 💻 Technologies Used

| Type         | Tools/Libraries                          |
|--------------|-------------------------------------------|
| Language     | Python 3.x                                |
| Voice Input  | `speech_recognition`                      |
| Voice Output | `pyttsx3` (English), `gTTS` (Bangla)      |
| GUI          | `Tkinter`                                 |
| API Services | Google Maps Directions & Static Map APIs  |
| Language Detection | `langdetect`                       |

---

## 🔧 Setup Instructions

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt

