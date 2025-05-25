import pyttsx3
import speech_recognition as sr
from langdetect import detect
from gtts import gTTS
import tempfile
import os
import platform

engine = pyttsx3.init()

def speak(text):
    try:
        lang = detect(text)
        if lang == 'bn':
            speak_bangla(text)
        else:
            speak_english(text)
    except:
        speak_english(text)

def speak_english(text):
    engine.say(text)
    engine.runAndWait()

def speak_bangla(text):
    tts = gTTS(text=text, lang='bn')
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        temp_path = fp.name
        tts.save(temp_path)

    if platform.system() == "Darwin":  # macOS
        os.system(f"afplay '{temp_path}'")
    elif platform.system() == "Windows":
        os.system(f"start /min wmplayer /play /close \"{temp_path}\"")
    else:  # Linux
        os.system(f"mpg123 '{temp_path}'")

    os.remove(temp_path)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio, language="bn-BD")  # Recognize Bangla & English
            return command
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Network error."
        except sr.WaitTimeoutError:
            return "Listening timed out."