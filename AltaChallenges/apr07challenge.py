#!/usr/bin/python3

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}}, "banana": 15, "d": "nothing"}]
hurt_me_plenty= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
not_too_rough= ["science", "turbo", ["goggles", "eyes"], "nothing"]

print(f"My {not_too_rough[2][1]} these {not_too_rough[2][0]} do {not_too_rough[3]}!") # easy
print(f"My {hurt_me_plenty[2]['goggles']} these {hurt_me_plenty[2]['eyes']} do {hurt_me_plenty[3]}!") # medium
print(f"My {nightmare[0]['user']['name']['first']} these {nightmare[0]['kumquat']} do {nightmare[0]['d']}!") # hard
