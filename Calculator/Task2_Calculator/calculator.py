import math

print("===== Smart Calculator =====")

while True:
    print("\nChoose Operation")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '7':
        print("Calculator Closed!")
        break

    if choice == '6':
        number = float(input("Enter number: "))
        print("Square Root =", math.sqrt(number))
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result =", num1 + num2)

    elif choice == '2':
        print("Result =", num1 - num2)

    elif choice == '3':
        print("Result =", num1 * num2)

    elif choice == '4':
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot divide by zero")

    elif choice == '5':
        print("Result =", num1 ** num2)

    else:
        print("Invalid choice")