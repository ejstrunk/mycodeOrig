#!/usr/bin/python3

def addition(calc1, calc2):
    print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))

def subtraction(calc1, calc2):
    print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))

def multiplication(calc1, calc2):
    print("\n" + str(calc1) + " * " + str(calc2) + " = " + str(calc1 * calc2))

def division(calc1, calc2):
    print("\n" + str(calc1) + " / " + str(calc2) + " = " + str(calc1 / calc2))

calc1 = 0.0
calc2 = 0.0
operation = ""
def calculator(calc1, calc2):
    while (calc1 != "q"):
        print("\nWhat is the first operator? Or, enter q to quit: ")
        calc1 = input()
        if calc1.lower() == "q":
            break
        try:
            calc1 = float(calc1)
        except:
            print("I'm sorry, that is not a valid number. Restarting...")
            continue
        print("\nWhat is the second operator? Or, enter q to quit: ")
        calc2 = input()
        if calc2.lower == "q":
            break
        try:
            calc2 = float(calc2)
        except:
            print("I'm sorry, that is not a valid number. Restarting...")
            continue
        print("Enter an operation to perform on the two operators (+, -, *, /): ")
        operation = input()
        if operation == "+":
            addition(calc1, calc2)
        elif operation == "-":
            subtraction(calc1, calc2)
        elif operation == "*":
            multiplication(calc1, calc2)
        elif operation == "/":
            try:
                division(calc1, calc2)
            except:
                print("Cannot divide by zero. Restarting...")
                continue
        else:
            print("\nNot a valid entry. Restarting...")
calculator(calc1, calc2)
