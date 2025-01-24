# Get input equation
equation = input("Enter the equation (e.g., 6 * 3): ")

try:
    # Parse the input
    #parts = equation.split('=')
    left = equation.strip()
    # z = float(parts[1].strip())

    if '*' in left:
        x, y = map(int, left.split('*'))
        result = x * y
    elif '/' in left:
        x, y = map(int, left.split('/'))
        result = x / y if y != 0 else None
    elif '-' in left:
        x, y = map(int, left.split('-'))
        result = x - y
    elif '+' in left:
        x, y = map(int, left.split('+'))
        result = x + y
    else:
        result = None
        print("Invalid operation.")

    # Check if the equation holds
    if result is not None :
        print(result)
    else:
        print("Unable to evaluate the equation.")

except Exception as e:
    print(f"Error parsing the equation: {e}")
