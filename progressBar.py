import tkinter as tk
from tkinter import ttk
import time

def main():
    # Your main code here
    for i in range(101):
        time.sleep(0.05)  # Simulating some task
        update_progress(i)
        update_label("Loading... {}%".format(i))
    root.after(1000, root.destroy)  # Close the splash screen after a delay

def update_progress(progress):
    progress_var.set(progress)
    progress_bar.update()

def update_label(text):
    label_var.set(text)

# Create the main Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

# Create a Toplevel window for the splash screen
splash_screen = tk.Toplevel()
splash_screen.title("Splash Screen")
splash_screen.geometry("300x120")

# Center the splash screen on the screen
window_width = splash_screen.winfo_reqwidth()
window_height = splash_screen.winfo_reqheight()
position_right = int(splash_screen.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(splash_screen.winfo_screenheight() / 2 - window_height / 2)
splash_screen.geometry("+{}+{}".format(position_right, position_down))

# Progress bar
progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(splash_screen, mode="determinate", variable=progress_var)
progress_bar.pack(pady=10)

# Label with dynamic text
label_var = tk.StringVar()
label = tk.Label(splash_screen, textvariable=label_var)
label.pack()

# Run the main code after a short delay to allow the splash screen to be displayed
root.after(100, main)

# Run the Tkinter event loop
root.mainloop()
