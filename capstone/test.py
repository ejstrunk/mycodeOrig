#!/usr/bin/python3
from time import sleep
import datetime
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
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n""")
# resources

ingredients_csv = pe.get_sheet(file_name="ingredients.csv")


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

def options():
    choice = input()
    if choice == "all":
        view_all()
    elif choice == "id":
        view_id()
    elif choice == "primary":
        view_primary()
    elif choice == "secondary":
        view_secondary()
    elif choice == "tertiary":
        view_tertiary()
    elif choice == "quaternary":
        view_quaternary()
    elif choice == "weight":
        view_weight()
    elif choice == "value":
        view_value()

init_choice = input("Would you like to view all ingredients by specific values? ")

if init_choice == "yes":
    options()
