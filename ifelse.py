plus_sign = "+"
minus_sign = "-"
multiply_sign = "*"
divide_sign = "/"
percentage_sign = "%"
square_sign = "x2"
cube_sign = "x3"

num1 = int(input("Enter first Number: "))

if num1 >= 0:
    cal = input(f"Choose how you want to calculate ({plus_sign}, {minus_sign}, {multiply_sign}, {divide_sign}, {percentage_sign}, {square_sign}, {cube_sign}): ")
    
    if cal in {"+", "-", "*", "/", "%"}:
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
        elif cal == "/":
            if num2 != 0:
                result = num1 / num2
                print("Your answer is:", result)
            else:
                print("Error: Division by zero is not allowed.")
        elif cal == "%":
            result = (num1 / num2) * 100
            print(f"{num1} is {result}% of {num2}")
    
    elif cal == "x2":
        result = num1 * num1
        print("Your answer is:", result)
    elif cal == "x3":
        result = num1 * num1 * num1
        print("Your answer is:", result)
    else:
        print("Invalid operator selected.")

else:
    print("Try again and choose a number to calculate.")



