#!/usr/bin/python3
from time import sleep
import sys
import random
import pyexcel as pe
""" Skyrim Alchemy Index """
print("""
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   @@                                           @@
   @@                                           @@
   @@    Welcome to the Skyrim Alchemy Index    @@
   @@                                           @@
   @@        Man the Mortar and Pestle          @@
   @@      Arm Yourself with Your Alembic       @@
   @@            Brace Your Bottles             @@
   @@         Let's Brew Some Poisons!          @@
   @@                                           @@
   @@                                           @@
   @@        Er...........Potions......         @@
   @@                                           @@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n""")

# bringing in the csv and effects txt
ingredients_csv = pe.get_sheet(file_name="ingredients.csv")
temp = open('pos_effects.txt', 'r')
pos_effects = temp.readlines()
pos_effects = [pos_effects[i][:-1] for i in range(len(pos_effects) - 1)] + [pos_effects[-1]]
temp.close()

# view all effects
def view_effects():
    for effect in pos_effects:
        print(effect)

# view all ingredients in detail
def view_all():
    print(ingredients_csv)

# view all ingredients with id
def view_id():
    for item in ingredients_csv:
        print("%s: %s" % (item[0], item[1]))

# view all ingredients with primary effect
def view_primary():
    for item in ingredients_csv:
        print("%s: %s" % (item[0], item[2]))

# view all ingredients with secondary effect
def view_secondary():
    for item in ingredients_csv:
        print("%s: %s" % (item[0], item[3]))

# view all ingredients with tertiary effect
def view_tertiary():
    for item in ingredients_csv:
        print("%s: %s" % (item[0], item[4]))

# view all ingredients with quaternary effect
def view_quaternary():
    for item in ingredients_csv:
        print("%s: %s" % (item[0], item[5]))

# view all ingredients with weight
def view_weight():
    for item in ingredients_csv:
        print("%s: %s" % (item[0], item[6]))

# view all ingredients with septim value
def view_value():
    for item in ingredients_csv:
        print("%s: %s" % (item[0], item[7]))

# function for viewing all ingredients by certain methods
def options():
    choice = " "
    again = " "
    while choice != "q":
        choice = input("You may list the ingredients by: all, id, primary, secondary, tertiary, quaternary, weight, or value.\n>").lower()
        if choice == "q":
            sys.exit("Have a Great Day!")
        elif choice == "all":
            view_all()
            break
        elif choice == "id":
            view_id()
            break
        elif choice == "primary":
            view_primary()
            break
        elif choice == "secondary":
            view_secondary()
            break
        elif choice == "tertiary":
            view_tertiary()
            break
        elif choice == "quaternary":
            view_quaternary()
            break
        elif choice == "weight":
            view_weight()
            break
        elif choice == "value":
            view_value()
            break
        else: 
            print("Please select a valid search method")
    while again != "q":
        again = input("\n==========================================================================\nContinue this method of research, return to scouring the book, or restart?\n>").lower()
        if again == "q":
            sys.exit("Had a Blast! See You Next Time!")
        elif again in ["research", "this method", "this method of research", "continue this method of research"]:
            options()
        elif again in ["book", "scour the book", "return to the book", "return to scouring the book"]:
            book()
        elif again == "restart":
            main()
        else:
            print("Please select a valid response from research, book, restart, or 'q' to exit.")

def book():  # function for basic lists of ingredients and effects
    init_choice = " "
    while init_choice != "q":
        init_choice = input("\n\nWould you like to view all ingredients or search by effect?\n>").lower()
        if init_choice == "q":
            sys.exit("See you later!")
        elif init_choice in ["all", "view all", "ingredients", "all ingredients", "view all ingredients"]:
            options()
        elif init_choice in ["effect", "effects", "search by effect", "search by effects"]:
            eff = " "
            while eff != "Q":
                eff = input('\n\nIn what effect are you interested?\n>').title()
                if eff == "Q":
                    sys.exit("Have a Great Day!")
                else:
                    if eff in pos_effects:
                        print(f"\n\nIngredients containing the {eff} effect are as follows\n==================================================================\n")
                        eff_rows = []
                        for i in range(1,len(ingredients_csv)):
                            if eff in ingredients_csv.row[i]:
                                eff_rows.append(i)
                        eff_rows = list(set(eff_rows))
                        for i in eff_rows:
                            print('\n' + ingredients_csv.row[i][0] + '\n')
                        print("==================================================================")
                        again = input("\nWould you like to continue?\n>").lower()
                        if again in ["yes", "y","yep", "yup", "yah"]:
                            book()
                        else:
                            sys.exit("Catch you next time!")
                    else:
                        print("\n" + eff + " is not a valid effect\n")
                        eff_list = input("If you would like to view the list of possible effects, please type 'list'. Otherwise, press ENTER\n>").lower()
                        if eff_list == "list":
                            #for effect in pos_effects:
                                #print(effect)
                            view_effects()
                        else:
                            print("\nLet's try again!\n")
        else:
            print("\nThat is not a valid option. Please enter 'all' or 'effect.\n\nYou may also exit with 'q'\n")

def main():
    start = " "
    while start != "q":
        start = input("Where would you like to begin?\nYou may retrieve the Guide Book or begin brewing on your own!\nAlso, feel free to take a break from your alchemical pursuits anytime with 'q'\n>").lower()
        if start == "q":
            sys.exit("Good Luck in Your Endeavors!")
        elif start in ["guide book", "guide", "book", "guidebook", "pick up the book", "pick up the guide book", "pick up the guidebook"]:
            book()
        elif start in ["brewpotions", "brewing", "begin brewing", "brew", "brew potions"]:
            print("\nThis feature is not yet implemented\n")
        else:
            print("\nPlease pick up the book or begin brewing.\nIf you would like to exit, select 'q'\n")

main()
