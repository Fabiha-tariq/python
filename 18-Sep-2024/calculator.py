plus_sign = "+"
minus_sign = "-"
multiply_sign = "*"
divide_sign = "/"
modulas_sign = "%"

num1 = int(input("Enter first Number: "))

if num1 >= 0:
    cal = input(f"Choose how you want to calculate ({plus_sign}, {minus_sign}, {multiply_sign}, {divide_sign} , {modulas_sign}): ")
else:
    print("Try again and choose a number to calculate")
num2 = int(input("Enter second Number: "))

if cal == "+":
    result = num1 + num2
    print("Your answer is:", result)
elif cal == "-":
    result = num1 - num2
    print("Your answer is:", result)
elif cal == "*":
    result = num1 * num2
    print("Your answer is:", result)
elif cal == "%":
    result = num1 / num2 * 100
    print("Your Answer is:", result)
elif cal == "/":
    if num2 != 0:
        result = num1 / num2
        print("Your answer is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator selected.")
