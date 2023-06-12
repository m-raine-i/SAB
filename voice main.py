import tkinter as tk
from tkinter import messagebox
import subprocess

def eng():
    subprocess.call(["python", "test/voice english"])

def fil():
    subprocess.call(["python", "test/voice tagalog"])

def choose_language():
    root = tk.Tk()
    root.title("Student Assistant Bot")
    root.geometry("300x230")
    root.configure(bg='Maroon')

    def on_eng_selected():
        messagebox.showinfo("Selected Language", "English selected")
        root.destroy()
        eng()

    def on_fil_selected():
        messagebox.showinfo("Selected Language", "Filipino selected")
        root.destroy()
        fil()

    def on_exit():
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            root.destroy()

    label = tk.Label(root, text="Choose your preferred language \n (Mamili ng iyong gustong wika)", bg='lightgray', font=("Consolas", 12))
    label.pack(pady=10)

    english_button = tk.Button(root, text="English", width=20, height=2, command=on_eng_selected)
    english_button.pack(pady=5)

    filipino_button = tk.Button(root, text="Filipino", width=20, height=2, command=on_fil_selected)
    filipino_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", width=20, height=2, command=on_exit)
    exit_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    choose_language()
