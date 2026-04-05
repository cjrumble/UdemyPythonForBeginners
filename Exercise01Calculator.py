# Create a simple calculator that takes two numbers and performs selected mathematical function.
# Ask the user to enter two numbers & assign user input to two integer variables, a & b
while True:
    try:
        a, b = map(int, input("Enter two numbers separated by a space: ").split())
        break  # Exit loop if successful
    except ValueError:
        print("Invalid input! Please enter two numbers separated by a space.")

# Takes two numbers separated by a space
operation = input("Enter operation: (+, -, *, /, %, **): ")


def add(x, y):  # addition
    return x + y


def subtract(x, y): # subtraction
    return x - y


def multiply(x, y): # multiplication
    return x * y


def divide(x, y): # division
    return x / y


def modulus(x, y): # modulus
    return x % y


def power(x, y): # power
    return x ** y


if operation == "+":
    print(add(a, b))
elif operation == "-":
    print(subtract(a, b))
elif operation == "*":
    print(multiply(a, b))
elif operation == "/":
    print(divide(a, b))
elif operation == "%":
    print(modulus(a, b))
elif operation == "**":
    print(power(a, b))
else:
    print("Invalid operation")
