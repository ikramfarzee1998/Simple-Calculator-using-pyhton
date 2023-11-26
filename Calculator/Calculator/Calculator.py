def calculator():
    operator = input("Please enter an operator (+ - * /): ")
    if operator == "+":
        num1,num2=inputnum()
        result = num1 + num2
        print(round(result, 3))
        # this is for addition operation

    elif operator == "-":
        num1,num2=inputnum()
        result = num1 - num2
        print(round(result, 3))
        # this is for subtraction operation

    elif operator == "*":
        num1,num2=inputnum()
        result = num1 * num2
        print(round(result, 3))
        # this is for multiplication operation

    elif operator == "/":
        num1,num2=inputnum()
        result = num1 / num2
        print(round(result, 3))
        # this is for division operation

    else:
        print(f"{operator} is not a valid operator")
        return
        #if input wrong operator it will end the loop

def inputnum():
    
    num1 = float(input("1st number: "))
    num2 = float(input("2nd number: "))
    return num1,num2


while True:
    calculator()

