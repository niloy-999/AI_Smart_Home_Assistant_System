from io import BytesIO
from PIL import Image
import requests

STATIC_MAP_API = "https://maps.googleapis.com/maps/api/staticmap"
DIRECTIONS_API = "https://maps.googleapis.com/maps/api/directions/json"

GOOGLE_API_KEY = "Find Your Own"  
DEFAULT_HOME = "Dhaka"


def get_traffic_route(text_command):
    try:
        command = text_command.lower().strip()

        if " to " not in command:
            return "Please include a destination. Example: 'Traffic to Chittagong'", None, None, None

        parts = command.split(" to ")
        if len(parts) == 2:
            if "from" in parts[0]:
                origin = parts[0].split("from")[1].strip()
            else:
                origin = DEFAULT_HOME
            destination = parts[1].strip()
        else:
            return "Couldn't understand your route. Use: 'Traffic from [place] to [place]'", None, None, None

        params = {
            "origin": origin,
            "destination": destination,
            "departure_time": "now",
            "key": GOOGLE_API_KEY
        }

        response = requests.get(DIRECTIONS_API, params=params)
        data = response.json()

        if data["status"] != "OK":
            return f"Could not get traffic data: {data['status']}", None, None, None

        leg = data["routes"][0]["legs"][0]
        duration = leg["duration_in_traffic"]["text"]
        distance = leg["distance"]["text"]

        info = f"🚗 From {origin.title()} to {destination.title()}:\nTime: {duration}\nDistance: {distance}"
        return info + "\nDo you want to see the map?", "ask_map", origin, destination

    except Exception as e:
        return f"Error getting traffic data: {e}", None, None, None


def get_route_map(origin, destination):
    try:
        params = {
            "size": "600x400",
            "markers": f"color:green|label:S|{origin}|color:red|label:E|{destination}",
            "path": f"color:0x0000ff|weight:5|{origin}|{destination}",
            "visible": f"{origin}|{destination}",  # Auto-zoom to fit
            "key": GOOGLE_API_KEY
        }

        response = requests.get(STATIC_MAP_API, params=params)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            return image
        else:
            print(f"Map request failed: {response.status_code}")
            return None
    except Exception as e:
        print(f"Map error: {e}")
        return None
