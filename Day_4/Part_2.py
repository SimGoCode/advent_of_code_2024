"""
Advent of code : Day 4
Part 2
"""

# Determines if a star is found around the central A that the fonctions receives.
# Tests downward and upward diagonals to see if a SAM or MAS is found, it both
# diagonals contain a SAM or MAS, then it's a X-MAS star.
def verifDiagonale(puzzle,i,j):
    border = len(puzzle)-1

    if 0 < i < border and 0 < j < border:
        if "".join(puzzle[i + k][j + k] for k in range(-1,2)) in ["MAS", "SAM"]:
            if "".join(puzzle[i + k][j - k] for k in range(-1, 2)) in ["MAS", "SAM"]:
                return True
    return False



# Adds the puzzle from input to the xmas_puzzle variable
with open("input.txt") as file:
    xmas_puzzle = [list(line.strip()) for line in file]

# initialise the x-mas found counter
xmas_counter_total = 0

# Loop and validates each "A" found to determine wether its a x-mas star or not.
for i in range(len(xmas_puzzle)):
    for j in range(len(xmas_puzzle)):
        if xmas_puzzle[i][j] == "A":
            if verifDiagonale(xmas_puzzle,i,j):
                xmas_counter_total +=1 # adds one if a star is found

print (xmas_counter_total)