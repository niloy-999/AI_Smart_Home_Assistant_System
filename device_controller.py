devices = {
    "light": False,
    "fan": False,
    "ac": False
}

def toggle_device(device_name):
    if device_name in devices:
        devices[device_name] = not devices[device_name]
        state = "on" if devices[device_name] else "off"
        return f"{device_name.capitalize()} turned {state}."
    else:
        return f"Device '{device_name}' not found."

def device_status(device_name):
    if device_name in devices:
        state = "on" if devices[device_name] else "off"
        return f"{device_name.capitalize()} is currently {state}."
    else:
        return f"No status available for '{device_name}'."
