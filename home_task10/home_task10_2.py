def calculate_squared_division():
    try:
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))

        result = (a ** 2) / b
        return result
    except ValueError:
        print("Error: Both inputs should be valid numbers.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

result = calculate_squared_division()
if result is not None:
    print("Result:", result)
