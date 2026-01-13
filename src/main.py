import math as m
from utils import *
from format import format_field
from mineMap import generate_map
from completeMap import complete_map

field = []

ROWS = 3
COLS = 3
MINES = 3

correct_flags = 0
flags = MINES
running = True


field.append(["/"])
for i in range(COLS):
    field[0].append(i+1)

for i in range(ROWS):
    field.append([i+1])
    for _ in range(COLS):
        field[i+1].append("?")
        
mineMap = generate_map(ROWS, COLS, MINES)

complete_map(mineMap)

def format_input(inp):
    inp = inp.split()   
    if len(inp) == 2:
        return int(inp[1])-1, int(inp[0])-1, None
    if len(inp) > 3:
        raise IndexError
    return int(inp[1])-1, int(inp[0])-1, inp[2]

def play_loop():
    global correct_flags, flags
    print(f"Grid: ({ROWS}x{COLS}) | Mines: {MINES}| Flags: {flags}")
    #format_field(mineMap) # Debug only
    format_field(field)
    x, y, action = format_input(input())
    if action is None:
        field[x+1][y+1] = mineMap[x][y]
        if mineMap[x][y] == "M":
            print("BOOOOM!!!")
            format_field(mineMap)
            return False
    else:
        if field[x+1][y+1] == "?":
            field[x+1][y+1] = "F"
            flags -= 1
            if mineMap[x][y] == "M": 
                correct_flags += 1
        elif field[x+1][y+1] == "F":
            field[x+1][y+1] = "?"
            flags += 1
            if mineMap[x][y] == "M": 
                correct_flags -= 1
        else:
            print(f"Error: cannot place a flag in (x:{x} y:{y})")
    
    if correct_flags == MINES and flags == 0:
        print(f"YOU WON!!!\nGrid({ROWS}x{COLS}) | M: {MINES}")
        format_field(mineMap)
        return False
    return True
        
while running:
    clear_console()
    running = play_loop()