#!/usr/bin/python3

answer = " "

while answer != "q":
    answer = input("Basic Engineering!\n==================\nDoes it move?\n> ")
    if answer.lower() == "q":
        break
    elif answer.lower() == "no":
        answer = input("Should it?\n> ")
        if answer.lower() == "q":
            break
        elif answer.lower() == "no":
            print("No Problem!")
            break
        elif answer.lower() == "yes":
            print("Spray some WD-40 on it!")
            break
        else:
            print("Please select yes or no. Select \'q\' to quit.")
            continue
    elif answer.lower() == "yes":
        answer = input("Should it?\n> ")
        if answer.lower() == "q":
            break
        elif answer.lower() == "no":
            print("Wrap it up in duct tape!")
            break
        elif answer.lower() == "yes":
            print("No Problem!")
            break
        else:
            print("Please select yes or no. Select \'q\' to quit.")
            continue
    else:
        print("Please select yes or no. Select \'q\' to quit.")
        continue
