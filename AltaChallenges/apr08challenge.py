#!/usr/bin/python3
# A program that propts a user for two operators and operation (plus or minus)
# The program then shows the result.
# The user may enter q to exit the program.
calc1 = 0.0
calc2 = 0.0
operation = ""
while calc1 != "q":   # Change 1: added ":" to end
    print("\nWhat is the first operator? Or, enter q to quit: ")
    calc1 = input() # Change 4: removed "raw" before "input" throughout script
    if calc1.lower() == "q": # Change 5: added .lower and change "Q" to lower throughout
        break
    calc1 = float(calc1)
    print("\nWhat is the second operator? Or, enter q to quit: ")
    calc2 = input()
    if calc2.lower == "q":
        break
    calc2 = float(calc2)
    print("Enter an operation to perform on the two operators (+ or -): ")
    operation = input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2)) # Change 2: added quotations around \n
    elif operation == '-': # Change 3: "ifel" to "elif"
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n Not a valid entry. Restarting...")
