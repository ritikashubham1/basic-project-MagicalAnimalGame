import random
import tkinter as tk

# Child-friendly bright colors and emojis
ANIMALS = {
    "Lion": {"emoji": "🦁", "sound": "ROAARRR!", "color": "#f39c12"},
    "Frog": {"emoji": "🐸", "sound": "RIBBIT! RIBBIT!", "color": "#2ecc71"},
    "Cat": {"emoji": "🐱", "sound": "MEOWWW~", "color": "#f1c40f"},
    "Cow": {"emoji": "🐮", "sound": "MOOOOO!", "color": "#95a5a6"},
    "Duck": {"emoji": "🦆", "sound": "QUACK! QUACK!", "color": "#3498db"}
}

current_target = ""

def play_sound(animal_name):
    """Displays the massive animal sound on screen with a color flash!"""
    animal_data = ANIMALS[animal_name]
    
    # Update display
    main_display.config(text=animal_data["sound"], fg=animal_data["color"])
    
    # Check if this was the correct answer for the quiz game
    global current_target
    if current_target and animal_name == current_target:
        main_display.config(text=f"🎉 CORRECT!\nThe {animal_name} says {animal_data['sound']}", fg="#2ecc71")
        current_target = "" # Reset quiz
        root.after(2000, ask_question) # Ask a new question after 2 seconds

def ask_question():
    """Starts a mini guessing game loop."""
    global current_target
    current_target = random.choice(list(ANIMALS.keys()))
    sound_to_guess = ANIMALS[current_target]["sound"]
    main_display.config(text=f"Can you find who says...\n\"{sound_to_guess}\"?", fg="#e74c3c")

# --- Setup the App Window ---
root = tk.Tk()
root.title("🌈 Magical Animal Kingdom 🌈")
root.geometry("500x550")
root.config(bg="#f5f6fa") # Clean, light child-friendly background

# Title Banner
title_label = tk.Label(root, text="✨ Tap an Animal! ✨", font=("Arial", 24, "bold"), bg="#f5f6fa", fg="#8e44ad")
title_label.pack(pady=15)

# Main Animated Text Screen (Big and bold for kids)
main_display = tk.Label(
    root, 
    text="Welcome to the Safari!\nClick an animal below!", 
    font=("Arial", 22, "bold"), 
    bg="#ffffff", 
    fg="#34495e",
    width=25,
    height=4,
    bd=3,
    relief="ridge"
)
main_display.pack(pady=20, padx=20)

# Grid Frame for Big Animal Buttons
button_frame = tk.Frame(root, bg="#f5f6fa")
button_frame.pack(pady=10)

# Generate big grid buttons dynamically for each animal
for i, name in enumerate(ANIMALS.keys()):
    emoji = ANIMALS[name]["emoji"]
    bg_color = ANIMALS[name]["color"]
    
    # Create big chunky button perfect for small hands to tap
    btn = tk.Button(
        button_frame,
        text=f"{emoji}\n{name}",
        font=("Arial", 16, "bold"),
        width=10,
        height=3,
        bg=bg_color,
        fg="white",
        activebackground="#34495e",
        activeforeground="white",
        command=lambda n=name: play_sound(n)
    )
    
    # Layout buttons cleanly in rows of 2
    row = i // 2
    col = i % 2
    btn.grid(row=row, column=col, padx=15, pady=15)

# "Start Quiz Game" Button at the bottom
quiz_btn = tk.Button(
    root, 
    text="🎮 Play Guessing Game! 🎮", 
    font=("Arial", 14, "bold"), 
    bg="#9b59b6", 
    fg="white",
    command=ask_question,
    bd=4,
    relief="raised"
)
quiz_btn.pack(pady=15)

root.mainloop()
