"""
Advent of code : Day 3
Part 1
"""

# Initializes the string that will contain the corrupted memory
corrupted_memory = ""

# Adds the corrupted memory from input to the string
with open("input.txt") as file:
    for line in file:
        corrupted_memory += line

#Initializes the multiplication sum to 0
mult_sum = 0

# Each time the sub string "mul(" is found, we look at the next 8 characters to see if it matches the criteria
# for a uncorrupted piece, if so, we multiply and add it to the sum
while "mul(" in corrupted_memory:
    index = corrupted_memory.find("mul(")
    # Creates a substring that will contain the first and second number and the closing parenthesis at least
    corrupted_piece = corrupted_memory[index+4:index+12]
    # Continues if there is at least one ")"
    if corrupted_piece.count(")") > 0 :
        # Cuts the piece at the first ")"
        corrupted_piece = corrupted_piece[:corrupted_piece.find(")")]
        #if theres is only one coma, then split the string into two variables
        if corrupted_piece.count(",") == 1 :
            a, b = corrupted_piece.split(",")
            # if the remains of the string are numerical, multiplies them and adds them to the total.
            if a.isnumeric() and b.isnumeric():
                mult_sum += int(a) * int(b)
    corrupted_memory = corrupted_memory[index+4:]

# Prints the result
print(mult_sum)
