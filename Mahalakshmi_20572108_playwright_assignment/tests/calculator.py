
# Day 5 Task 4 Mahalakshmi -20572108
import tkinter as tk


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: cannot divide by zero."
    return a / b


def main():
    window = tk.Tk()
    window.title("Simple Calculator")
    window.resizable(False, False)

    tk.Label(window, text="First number:").grid(
        row=0, column=0, padx=10, pady=(10, 5), sticky="w"
    )
    first_entry = tk.Entry(window)
    first_entry.grid(row=0, column=1, padx=10, pady=(10, 5))

    tk.Label(window, text="Second number:").grid(
        row=1, column=0, padx=10, pady=5, sticky="w"
    )
    second_entry = tk.Entry(window)
    second_entry.grid(row=1, column=1, padx=10, pady=5)

    result_label = tk.Label(window, text="Result: ")
    result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=(5, 10))

    def calculate(operation):
        try:
            first_number = float(first_entry.get())
            second_number = float(second_entry.get())
        except ValueError:
            result_label.config(text="Please enter valid numbers.")
            return

        result = operation(first_number, second_number)
        if isinstance(result, str):
            result_label.config(text=result)
        else:
            result_label.config(text=f"Result: {result}")

    operations = (
        ("Add", add),
        ("Subtract", subtract),
        ("Multiply", multiply),
        ("Divide", divide),
    )
    for index, (label, operation) in enumerate(operations):
        tk.Button(
            window,
            text=label,
            command=lambda selected_operation=operation: calculate(
                selected_operation
            ),
        ).grid(row=2, column=index % 2, padx=10, pady=5, sticky="ew")

    window.mainloop()


if __name__ == "__main__":
    main()
