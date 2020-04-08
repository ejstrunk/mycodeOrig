#!/usr/bin/python3

stars = ["*", "**", "***", "****", "*****", "****", "***", "**", "*"]
for x in stars:
    print(x)

stars2 = ["*", "**", "***", "****", "*****"]
for x in stars2:
    print(x)
for x in reversed(stars2):
        print(x)

for x in range(0, 6):
    print("* " * x)
for x in range(4, 0, -1):
    print("* " * x)
