"""
Advent of code : Day 4
Part 1
"""

# Initializes the list that will contain every characters from the input puzzle
# and the xmas variable that will be used to search in the list
xmas_puzzle = []

## Horizontal verification for forward and backward XMAS
def verifHorizon(puzzle,i,j):
    xmas_counter = 0

    if i < (len(puzzle)-3):
        if puzzle[i+1][j] == "M":
            if puzzle[i+2][j] == "A":
                if puzzle[i+3][j] == "S":
                    xmas_counter +=1
    if i > 2:
        if puzzle[i - 1][j] == "M":
            if puzzle[i - 2][j] == "A":
                if puzzle[i - 3][j] == "S":
                    xmas_counter += 1

    return xmas_counter

## Vertical verification for upward and downward XMAS
def verifVerticale(puzzle,i,j):
    xmas_counter = 0

    if j < (len(puzzle) - 3):
        if puzzle[i][j+1] == "M":
            if puzzle[i][j+2] == "A":
                if puzzle[i][j+3] == "S":
                    xmas_counter += 1
    if j > 2:
        if puzzle[i][j-1] == "M":
            if puzzle[i][j-2] == "A":
                if puzzle[i][j-3] == "S":
                    xmas_counter += 1

    return xmas_counter

## Diagonal verification for all four diagonals XMAS
def verifDiagonale(puzzle,i,j):
    xmas_counter = 0

    ## verif diagonal droite haut
    if i < (len(puzzle)-3) and j > 2:
        if puzzle[i+1][j-1] == "M":
            if puzzle[i+2][j-2] == "A":
                if puzzle[i+3][j-3] == "S":
                    xmas_counter +=1
    ## verif diagonal droite bas
    if i < (len(puzzle)-3) and j < (len(puzzle) - 3):
        if puzzle[i+1][j+1] == "M":
            if puzzle[i+2][j+2] == "A":
                if puzzle[i+3][j+3] == "S":
                    xmas_counter +=1

    ## verif diagonal gauche haut
    if i > 2 and j > 2:
        if puzzle[i-1][j-1] == "M":
            if puzzle[i-2][j-2] == "A":
                if puzzle[i-3][j-3] == "S":
                    xmas_counter +=1

    ## verif diagonal gauche bas
    if i > 2 and j < (len(puzzle) - 3):
        if puzzle[i-1][j+1] == "M":
            if puzzle[i-2][j+2] == "A":
                if puzzle[i-3][j+3] == "S":
                    xmas_counter +=1
    return xmas_counter


# Adds the puzzle from input to the list
with open("input.txt") as file:
    for line in file:
        xmas_puzzle_line = []
        for character in line.strip():
            xmas_puzzle_line.append(character)
        xmas_puzzle.append(xmas_puzzle_line)

xmas_counter_total = 0

for i in range(len(xmas_puzzle)):
    for j in range(len(xmas_puzzle)):
        if xmas_puzzle[i][j] == "X":
            xmas_counter_total += verifHorizon(xmas_puzzle, i, j)
            xmas_counter_total += verifVerticale(xmas_puzzle, i, j)
            xmas_counter_total += verifDiagonale(xmas_puzzle, i, j)

print (xmas_counter_total)