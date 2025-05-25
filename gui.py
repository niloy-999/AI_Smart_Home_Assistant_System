import tkinter as tk
from tkinter import scrolledtext
from voice_interface import speak, listen
from command_processor import process_command
from traffic import get_route_map
from PIL import ImageTk, Image

# Conversation state for handling map confirmation
conversation_state = {
    "awaiting_map_confirmation": False,
    "origin": None,
    "destination": None
}

def start_gui():
    window = tk.Tk()
    window.title("AI Smart Home Assistant")
    window.geometry("600x700")  # Increased height for map display

    output_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=15, font=("Arial", 12))
    output_box.pack(pady=10)

    input_entry = tk.Entry(window, width=50, font=("Arial", 12))
    input_entry.pack(pady=5)

    map_label = tk.Label(window)  # Label for map image
    map_label.pack(pady=5)

    def handle_text_command():
        user_input = input_entry.get().strip()
        output_box.insert(tk.END, f"You: {user_input}\n")
        input_entry.delete(0, tk.END)


        if conversation_state["awaiting_map_confirmation"]:
            if user_input.lower() in ["yes", "y", "show", "sure"]:
                origin = conversation_state["origin"]
                destination = conversation_state["destination"]
                map_img = get_route_map(origin, destination)
                if map_img:
                    map_img = map_img.resize((400, 250))
                    img_tk = ImageTk.PhotoImage(map_img)
                    map_label.config(image=img_tk)
                    map_label.image = img_tk  # Prevent garbage collection
                    output_box.insert(tk.END, "Assistant: Showing map.\n")
                else:
                    output_box.insert(tk.END, "Assistant: Couldn't load map.\n")
            else:
                output_box.insert(tk.END, "Assistant: Okay, not showing the map.\n")
            conversation_state["awaiting_map_confirmation"] = False
            return


        response = process_command(user_input)

        if isinstance(response, tuple):
            message, intent, origin, destination = response
            if intent == "ask_map":
                conversation_state["awaiting_map_confirmation"] = True
                conversation_state["origin"] = origin
                conversation_state["destination"] = destination
            output_box.insert(tk.END, f"Assistant: {message}\n")
            speak(message)
        else:
            output_box.insert(tk.END, f"Assistant: {response}\n")
            speak(response)

    def handle_voice_command():
        output_box.insert(tk.END, "Listening...\n")
        voice_input = listen()
        output_box.insert(tk.END, f"You (voice): {voice_input}\n")


        if conversation_state["awaiting_map_confirmation"]:
            if voice_input.lower() in ["yes", "y", "show", "sure"]:
                origin = conversation_state["origin"]
                destination = conversation_state["destination"]
                map_img = get_route_map(origin, destination)
                if map_img:
                    map_img = map_img.resize((400, 250))
                    img_tk = ImageTk.PhotoImage(map_img)
                    map_label.config(image=img_tk)
                    map_label.image = img_tk
                    output_box.insert(tk.END, "Assistant: Showing map.\n")
                else:
                    output_box.insert(tk.END, "Assistant: Couldn't load map.\n")
            else:
                output_box.insert(tk.END, "Assistant: Okay, not showing the map.\n")
            conversation_state["awaiting_map_confirmation"] = False
            return

        response = process_command(voice_input)

        if isinstance(response, tuple):
            message, intent, origin, destination = response
            if intent == "ask_map":
                conversation_state["awaiting_map_confirmation"] = True
                conversation_state["origin"] = origin
                conversation_state["destination"] = destination
            output_box.insert(tk.END, f"Assistant: {message}\n")
            speak(message)
        else:
            output_box.insert(tk.END, f"Assistant: {response}\n")
            speak(response)

    # Buttons
    tk.Button(window, text="Send", command=handle_text_command).pack(pady=5)
    tk.Button(window, text="🎤 Voice Command", command=handle_voice_command).pack(pady=5)
    
    

    window.mainloop()
