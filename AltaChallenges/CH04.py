#!/usr/bin/python3

# Challenge Lab 04: Dictionary in a list in a list

mess = [1, 2, [3, 4, 5, {"six":6, "seven":7, "eight":8}]]

print(mess[2][3]["eight"])
