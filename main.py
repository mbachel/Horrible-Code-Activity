def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def main():
    user_input = ""
    while user_input != "off":
        print(f"Please select an option:",
              f"\n1. Add",
              f"\n2. Subtract",
              f"\n3. Multiply",
              f"\n4. Divide"
              f"\n5. Quit")
        user_input = int(input("Please select an option: "))
        if user_input == 5:
            break

        elif user_input < 1 or user_input > 4:
            print("Please select a valid option.\n")
            continue

        num1 = float(input("Please enter first number: "))
        num2 = float(input("Please enter second number: "))

        if user_input == 1:
            print(f"{num1} plus {num2} is equal to {add(num1, num2)}.\n")
            continue

        elif user_input == 2:
            print(f"{num1} minus {num2} is equal to {subtract(num1, num2)}.\n")
            continue

        elif user_input == 3:
            print(f"{num1} multiplied by {num2} is equal to {multiply(num1, num2)}.\n")
            continue

        elif user_input == 4:
            print(f"{num1} divided by {num2} is equal to {divide(num1, num2)}.\n")
            continue

if __name__ == "__main__":
    main()