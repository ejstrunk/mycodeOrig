#!/usr/bin/python3
#this library allows us to generate UUID values.
import uuid

while True:
    try:
        howmany = int(input("How many UUIDs should be generated? Limit of 10. "))
        break
    except:
        print("Type in a number between 1 and 10.")

if howmany <= 10:
    print("Generating UUIDs...")
    for rando in range(howmany):
        print( uuid.uuid4() )

else:
    print("You may only select between 1 and 10 UUIDs. Try again.")
