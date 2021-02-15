#calculator new V2
import math
x = input('For Calculator type 1:\nSquare Root & Square, Type 2\nTo quit type q: ')



if x == '1':
        print("Calculator")
        if_number_is_not_float = True
        while if_number_is_not_float:
            try:
                num1 = float(input("Your first number: "))
            except ValueError:
                print("That is not a number!")
            else:
                if_number_is_not_float = False
                
        op = input("Enter a operater: +, -,/,*: ")
         
        if_number_is_not_float1 = True
        while if_number_is_not_float1:
            try:
                num2 = float(input("Your second number: "))
            except ValueError:
                print("That is not a number!")
            else:
                if_number_is_not_float1 = False
        if op == "+":
            print(num1 + num2)
        if op == "-":
            print(num1 - num2)
        if op == "/":
            print(num1 / num2)
        if op == "*":
            print(num1 * num2)
  

while (x == "q"):
    print(x)

if x == "2":
        print("Square Root & Square")
        z = float(input("Square root, type 1 ---- Square, type 2: "))
        if z == 1:
            def function3():
                print("Square root")
                this_is_a_number = True
                while this_is_a_number:
                    try:
                        f = float(input("Number: "))
                    except ValueError:
                        print("That is not a number!")
                    else:
                        this_is_a_number = False 
                    return math.sqrt(f)

            print(function3())
        if z == 2:
                print("Square")
                this_is_a_number1 = True
                while this_is_a_number1:
                    try:
                        square = float(input("1st Number: "))
                    except ValueError: 
                        print("That is not a number!")
                    else:
                        this_is_a_number1 = False

                this_is_a_number2 = True
                while this_is_a_number2:
                    try:
                        square2 = float(input("2nd Number: "))
                    except ValueError:
                        print("That is not a number!")
                    else: 
                        this_is_a_number2 = False
                print(square**square2)
