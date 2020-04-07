#!/usr/bin/python3

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk:
    print("Looks like the IP address was set: " + ipchk)
else:   # if data is not provided
    print("You did not provide input.")
