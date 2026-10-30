# Day 5 Task 3 Mahalakshmi -20572108

import tkinter as tk


def main():
    window = tk.Tk()
    window.title("Greeting App")

    tk.Label(window, text="Enter your name:").pack(pady=5)

    name_entry = tk.Entry(window)
    name_entry.pack(pady=5)

    greeting_label = tk.Label(window, text="")
    greeting_label.pack(pady=5)

    def say_hello():
        name = name_entry.get()
        greeting_label.config(text=f"Hello, {name}! Welcome to Python")

    tk.Button(window, text="Say Hello", command=say_hello).pack(pady=5)
    window.mainloop()


if __name__ == "__main__":
    main()
