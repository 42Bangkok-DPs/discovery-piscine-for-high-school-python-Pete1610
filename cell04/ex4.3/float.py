number = input("Give me a number: ")

# Check if the input can be an integer
try:
    int_number = int(number)
    if '.' in number or 'e' in number.lower():  # Check for decimal or scientific notation
        print("This number is a decimal.")
    else:
        print("This number is an integer.")
except ValueError:
    try:
        float_number = float(number)
        print("This number is a decimal.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

