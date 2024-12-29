"""
Advent of code : Day 3
Part 2
"""

# Initializes the string that will contain the corrupted memory
corrupted_memory = ""

# Adds the corrupted memory from input to the string
with open("input.txt") as file:
    for line in file:
        corrupted_memory += line

# Initializes an enabled corrupted memory string that will contain only parts that are enabled by the do() commands
# Initializes the state bool to true meaning that we are actually in a do() state
enabled_corrupted_memory = ""
enabled_state = True

# Search for do() or don't() commands depending on the current state and concatenate
# on the enabled_corrupted_memory string when on a do() state.
while len(corrupted_memory) > 0:
    if enabled_state:
        if "don't()" in corrupted_memory:
            cut = corrupted_memory.find("don't()")
            enabled_corrupted_memory += corrupted_memory[:cut]
            corrupted_memory = corrupted_memory[cut+7:]
            enabled_state = False

        else:
            enabled_corrupted_memory += corrupted_memory
            corrupted_memory = ""


    if  not enabled_state:
        if "do()" in corrupted_memory:
            glue = corrupted_memory.find("do()")
            corrupted_memory = corrupted_memory[glue+4:]
            enabled_state = True

        else:
            corrupted_memory = ""

# Overwrites the corrupted_memory string so that it only contains the enabled parts found before
corrupted_memory = enabled_corrupted_memory

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