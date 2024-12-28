"""
Advent of code : Day 1
Part 1 & part 2
"""

### Part 1 ###

# Defines two lists that will store the content of the puzzle input
list_1 = []
list_2 = []

# Opens the text file puzzle input and stores the content in the lists.
with open("day_1_input.txt") as file:
    for line in file:
        element_list_1, element_list_2 = line.strip().split("   ")
        list_1.append(int(element_list_1))
        list_2.append(int(element_list_2))

# Initiates the distance sum
sum_distance = 0

# Finds the smallest item in each list
# Adds the difference between them to the distance sum
# Remove the items from each lists
# Loop until one of the lists is empty
while len(list_1) > 0 and len(list_2) > 0:
    min_value_1 = min(list_1)
    min_value_2 = min(list_2)
    sum_distance += abs(min_value_1-min_value_2)
    list_1.remove(min_value_1)
    list_2.remove(min_value_2)

# Prints the result
print(f"The total distance between lists is: {sum_distance}")



### PART TWO ###

# Opens the text file puzzle input and stores the content in the emptied lists
list_1 = []
list_2 = []
with open("day_1_input.txt") as file:
    for line in file:
        element_list_1, element_list_2 = line.strip().split("   ")
        list_1.append(int(element_list_1))
        list_2.append(int(element_list_2))

# Sets the similiraty score to 0
similarity_score = 0

# Runs trough each item of the first list and compares it to each item of the 2nd list
# If the item is the same, adds 1 to the item_appearance counter
# adds the item value * item_appearance to the score.
for i in range(len(list_1)):
    item_appearance = 0
    for j in range(len(list_2)):
        if list_1[i] == list_2[j]:
            item_appearance += 1
    similarity_score += list_1[i] * item_appearance

# Prints the final result
print(f"The similarity score is: {similarity_score}")