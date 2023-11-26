def calculator():
    operator = input("Please enter an operator (+ - * /): ")
    num1 = float(input("1st number: "))
    num2 = float(input("2nd number: "))

    if operator == "+":
        result = num1 + num2
        print(round(result, 3))
        # this is for addition operation

    elif operator == "-":
        result = num1 - num2
        print(round(result, 3))
        # this is for subtraction operation

    elif operator == "*":
        result = num1 * num2
        print(round(result, 3))
        # this is for multiplication operation

    elif operator == "/":
        result = num1 / num2
        print(round(result, 3))
        # this is for division operation

    else:
        print(f"{operator} is not a valid operator")
        return  


calculator()

