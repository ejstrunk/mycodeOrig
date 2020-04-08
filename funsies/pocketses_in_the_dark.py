#!/usr/bin/python3

import time
# A simple game of riddles
# print("Can you help Bilbo escape Gollum's Grasp?")
# Riddles:
# G-- What has roots as nobody sees; Is taller than trees; Up, up, up it goes; And yet, never grows: Mountain
# B-- Thirty white horses on a red hill; First they champ; Then they stamp; Then they stand still: Teeth
# G-- Voiceless it cries; Wingless flutters; Toothless bites; Mouthless mutters: Wind
# B-- An eye in a blue face; Saw an eye in a green face; 'That eye is like to this eye'; Said the first eye; 'But in low place; Not in high place': Sun shining on daises
# G-- It cannot be seen, cannot be felt; Cannot be heard, cannot be smelt; It lies behind stars and under hills; And empty holes it fills; It comes first and follows after; Ends life, kills laughter: Darkness
# B-- A box without hinges, key or lid; Yet golden treasure inside is hid: egg
# G-- Alive without breath; As cold as death; Never thirsty, ever drinking; All in mail never clinking: Fish
# G-- This thing all things devours; Birds, beasts, trees, flowers; Gnaws iron, bites steel; Grinds hard stones to meal; Slays kings, ruins town; And beats high mountain down: Time
# Bonus B-- What have I got in my pocket?

# Welcome message: Choose Bilbo or Gollum
team = input('Welcome traveler, to a point in time that will decide the fate of Middle Earth.\nYou will bear witness to a contest of riddles between two souls:\nthe peaceful burglar-Hobbit, Bilbo Baggins\nthe corrupted, ever-hungry creature known as Gollum..\nYou may choose who to assist, but know now, your decision may shape the world.\nWill you lend your wits to Bilbo or Gollum? ').lower()

# Team Bilbo
if team == "bilbo":
    score = 0
# Riddle 1
    round = 0
    answer = " "

    while round < 3 and answer != "mountain":
        round += 1   # increases the round counter by 1
        answer = input('\nWhat has roots as nobody sees,\nIs taller than trees,\nUp, up, up it goes,\nAnd yet, never grows: ').lower()
        if answer == "mountain":  # logic to check if user gave correct answer
            time.sleep(1)
            print("\nThat\'s it..")
            score += 1
        elif round == 3:  # logic to ensure round has not yet reached 3
            time.sleep(1)
            print("\nNo! Precious... four more riddles; then we eats it!")
            score -= 1
        elif round == 2:  # if second answer was wrong
            time.sleep(1)
            print("\nHah! No.. One more try, precious.")
        else:  # if first answer was wrong
            time.sleep(1)
            print("\nNo! Two more answers. Two more steps closer til we eats it, precious!")

# Riddle 2
    round = 0
    answer = " "

    while round < 3 and answer != "wind":
        round += 1
        answer = input('\nVoiceless it cries,\nWingless flutters,\nToothless bites,\nMouthless mutters: ').lower()
        if answer == "wind":
            time.sleep(1)
            print("\nHe must be cheating, precious!\nFine...we gives it another riddle.\nThen maybe we eats it.")
            score += 1
        elif round == 3:
            time.sleep(1)
            print("\nHooohoooo! Three more, precious: three more riddles and we bashes its pretty face!")
            score -= 1
        elif round == 2:
            time.sleep(1)
            print("\nOh come on, precious....We wants to eat it now!")
        elif round == 1:
            time.sleep(1)
            print("\nNow we eats it, precious?\n\nNo!\nWe gives it two more tries!")
    if score > 0:
        print("Your score was:")
        print(score)
        print("You've survived!")
    elif score <1:
        print("Your score was:")
        print(score)
        print("Death!")
else:
    print("goodbye")
