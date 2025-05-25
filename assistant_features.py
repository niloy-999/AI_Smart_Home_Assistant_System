import datetime
import requests

reminders = []



API_KEY = "Find Your Own" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city="Dhaka"):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["cod"] != 200:
            return f"Could not fetch weather: {data['message']}"

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        return (
            f"Weather in {city}:\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {description.capitalize()}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} m/s"
        )
    except Exception as e:
        return f"Error fetching weather: {e}"


def add_reminder(text, time=None):
    if time is None:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    reminders.append((text, time))
    return f"Reminder added: '{text}' at {time}."

def list_reminders():
    if not reminders:
        return "No reminders set."
    return "\n".join([f"{text} at {time}" for text, time in reminders])
