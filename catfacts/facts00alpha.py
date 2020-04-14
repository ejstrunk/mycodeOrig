#!/usr/bin/python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests
import random

r = requests.get('https://cat-fact.herokuapp.com/facts') # create r, our request object

def main():
    """Runtime code"""
    ## catfact is our iterable -- that just means it will take on the values found within r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary print the value associated with text"
    for catfact in r.json()["all"]:
        print(catfact.get("text"))  # the .get() method returns NONE if key not found

def random_cat_fact():
    fact_list= []
    for fact in r.json()["all"]:
        fact_list.append(fact.get("text"))
    list_count= len(fact_list) - 1
    random_fact= random.randint(0, list_count)
    print("\nAnd now, another random CAT FACT!")
    print("===================================")
    print(fact_list[random_fact])

#main()
random_cat_fact()
