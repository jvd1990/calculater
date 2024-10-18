#calculator
name = input("what is your name: ")
order = int(input(f"how many digits do you want to calculate {name}. 2 or 3 digits: "))
if order == 2:
    num1 = int(input(f"enter your first number {name}: "))
    fun1 = input(f"{name} enter your first math operation (+, -, *, /): ")
    num2 = int(input(f"enter your second number {name}: "))
    if fun1 == '+':
        result = num1 + num2
    elif fun1 == '-':
        result = num1 - num2
    elif fun1 == '*':
        result = num1 * num2
    elif fun1 == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation."

    print(f"The result of {num1} {fun1} {num2} is = {result}")

elif order == 3:
    num1 = int(input(f"enter your first number, {name}: "))
    fun1 = input(f"{name} enter your first math operation (+, -, *, /): ")
    num2 = int(input(f"enter your second number, {name}: "))
    fun2 = input(f"{name} enter your second math operation (+, -, *, /): ")
    num3 = int(input(f"enter your third number, {name}: "))

    if fun1 == '+':
        first_result = num1 + num2
    elif fun1 == '-':
        first_result = num1 - num2
    elif fun1 == '*':
        first_result = num1 * num2
    elif fun1 == '/':
        if num2 != 0:
            first_result = num1 / num2
        else:
            first_result = "Error! Division by zero."
    
    if isinstance(first_result, (int, float)):
        if fun2 == '+':
            result = first_result + num3
        elif fun2 == '-':
            result = first_result - num3
        elif fun2 == '*':
            result = first_result * num3
        elif fun2 == '/':
            if num3 != 0:
                result = first_result / num3
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operation."
    else:
        result = first_result

    print(f"The result of {num1} {fun1} {num2} {fun2} {num3} is = {result}")
else:
    print(f"Invalid choice, {name}. Please choose 2 or 3 digits.")
