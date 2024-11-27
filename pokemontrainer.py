import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO  # for working with image data from the internet

# Create the main window
window = tk.Tk()
window.title("Pokémon Training Program")
window.geometry("600x400")
window.config(bg="lightblue")

# URL of the Pokémon image (use any public URL for the image)
image_url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"  # URL for Pikachu image

# Fetch the image from the URL
response = requests.get(image_url)
img_data = BytesIO(response.content)

# Open the image using PIL
img = Image.open(img_data)
img = img.resize((200, 200), Image.Resampling.LANCZOS)  # Resize the image
pokemon_img = ImageTk.PhotoImage(img)

# Create the header label
header_label = tk.Label(window, text="Pokémon Power Training", font=("Helvetica", 24, "bold"), bg="lightblue", fg="green")
header_label.pack(pady=20)

# Display Pokémon logo
logo_label = tk.Label(window, image=pokemon_img, bg="lightblue")
logo_label.pack()

# Label for entering powers
instruction_label = tk.Label(window, text="Enter Pokémon powers (comma separated):", font=("Helvetica", 12), bg="lightblue")
instruction_label.pack(pady=10)

# Entry field for powers input
powers_entry = tk.Entry(window, font=("Helvetica", 14), width=25)
powers_entry.pack()

# Create a function to calculate the min and max power
def calculate_powers():
    try:
        # Get the input from the user and convert it into a list of integers
        powers_input = powers_entry.get()
        powers = list(map(int, powers_input.split(",")))

        mini, maxi = powers[0], powers[0]  # initialize with the first value

        result_text = "Min and Max Powers:\n"
        for power in powers:
            mini = min(mini, power)
            maxi = max(maxi, power)
            result_text += f"Current Min: {mini}, Current Max: {maxi}\n"

        # Display the result in the output label
        result_label.config(text=result_text)
    except ValueError:
        # Show an error message if the input is invalid
        messagebox.showerror("Invalid Input", "Please enter valid integers, separated by commas.")

# Button to trigger the calculation
calculate_button = tk.Button(window, text="Train Pokémon", font=("Helvetica", 14, "bold"), bg="yellow", fg="red", command=calculate_powers)
calculate_button.pack(pady=20)

# Label to show the result (min/max powers)
result_label = tk.Label(window, text="Min and Max Powers:\n", font=("Helvetica", 12), bg="lightblue", fg="black")
result_label.pack()

# Run the main loop to display the GUI
window.mainloop()
