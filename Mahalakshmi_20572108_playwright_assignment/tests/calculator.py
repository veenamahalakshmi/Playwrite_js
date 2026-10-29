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
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Choose an operation (1-4): ").strip()
    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice. Please choose a number from 1 to 4.")
        return

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    operations = {
        "1": ("Sum", add),
        "2": ("Difference", subtract),
        "3": ("Product", multiply),
        "4": ("Quotient", divide),
    }
    label, operation = operations[choice]
    print(f"{label}: {operation(first_number, second_number)}")


if __name__ == "__main__":
    main()
