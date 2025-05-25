
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
```

### 2️⃣ Set Google API Key

Create an `.env` file or directly set your `GOOGLE_API_KEY` in `traffic.py`:

```python
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
```

### 3️⃣ Run the App

```bash
python gui.py
```

---

## 🧪 Sample Commands

### 💬 English

- `Turn on the light`
- `What's the weather in Dhaka`
- `Traffic from Dhaka to Kushtia`
- `Remind me to buy milk`

### 💬 Bangla

- `আজকের আবহাওয়া কেমন`
- `লাইট অন করো`
- `ঢাকা থেকে কুষ্টিয়া ট্রাফিক`

---

## 📁 File Overview

| File | Description |
|------|-------------|
| `gui.py` | Main application GUI |
| `voice_interface.py` | Handles speech I/O |
| `processor.py` | Command parsing and routing |
| `device_controller.py` | Simulated device management |
| `assistant_features.py` | Weather and reminders |
| `traffic.py` | Google Maps API integration |

---

## ⚙️ Future Enhancements

- Add Smart Device Simulation (GUI buttons + state indicators)
- Home automation hardware support (e.g., Arduino or Raspberry Pi)
- Wake word activation
- NLP improvement with Transformer-based models

---

## 🤖 Made With AI and ❤️

This project was built for learning and exploring the intersection of voice interfaces, bilingual AI, and smart home control.
