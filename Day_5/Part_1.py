"""
Advent of code : Day 5
Part 1
"""

from collections import defaultdict

#Creates a default dictionnairy that will contain all the rules
rules = defaultdict(list)
#creates the update list containing every updates
update_list = []

#Reads the input file and stores the first part in a dictionnary
#The first value is the key, and the number after the "|" is the value
#The second part after the blank line is stored in a list
with open("input.txt", "r") as f:
    input_data = f.read().strip().split("\n\n")

    for line in input_data[0].split("\n"):
        cle, valeur = map(int, line.split("|"))
        rules[cle].append(valeur)

    for line in input_data[1].split("\n"):
        update_list.append([int(x) for x in line.split(",")])

    # Sum that contains the middle value of each safe update
    safe_sum = 0

    #Loops on all update to determine wether the update is safe or not
    for update in update_list:
        update_is_safe = True
        prior_pages = [update[0]]

        for i in range(1,len(update)):
            if any(page in rules[update[i]] for page in prior_pages):
                update_is_safe = False
            prior_pages.append(update[i])

        if update_is_safe:
            safe_sum += update[len(update)//2]

    print(safe_sum)
