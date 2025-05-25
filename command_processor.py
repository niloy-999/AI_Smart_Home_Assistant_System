from device_controller import toggle_device, device_status
from assistant_features import get_weather, add_reminder, list_reminders
from traffic import get_traffic_route
from langdetect import detect


def process_command(command):
    command = command.lower().strip()
    lang = detect(command)


    if lang == "bn":
        if "আবহাওয়া" in command:
            return get_weather("Dhaka")  # default city
        elif "লাইট" in command and ("চালু" in command or "বন্ধ" in command):
            return toggle_device("light")
        elif "ফ্যান" in command and ("চালু" in command or "বন্ধ" in command):
            return toggle_device("fan")
        elif "এসি" in command and ("চালু" in command or "বন্ধ" in command):
            return toggle_device("ac")
        elif "স্ট্যাটাস" in command:
            if "লাইট" in command:
                return device_status("light")
            elif "ফ্যান" in command:
                return device_status("fan")
            elif "এসি" in command:
                return device_status("ac")
        elif "রিমাইন্ডার" in command or "মনে করিয়ে দাও" in command:
            return "রিমাইন্ডার ফিচারটি এখনো সম্পূর্ণ নয়।"
        elif "ট্রাফিক" in command:
            return "ট্রাফিক তথ্য এখনও বাংলায় সমর্থিত নয়।"
        else:
            return "দুঃখিত, আমি এই বাংলা কমান্ডটি এখনো বুঝি না।"


    else:
        if "turn on" in command or "turn off" in command:
            for device in ["light", "fan", "ac"]:
                if device in command:
                    return toggle_device(device)

        elif "status" in command:
            for device in ["light", "fan", "ac"]:
                if device in command:
                    return device_status(device)

        elif "weather" in command:
            words = command.split()
            for i, word in enumerate(words):
                if word == "in" and i + 1 < len(words):
                    city = words[i + 1]
                    return get_weather(city)
            return get_weather()

        elif "remind me" in command:
            text = command.replace("remind me", "").strip()
            return add_reminder(text)

        elif "list reminders" in command:
            return list_reminders()

        elif "traffic" in command and "to" in command:
            return get_traffic_route(command)

        else:
            return "Sorry, I don't understand that yet."
