import math as m
import msvcrt

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

curr_x = 1
curr_y = 1

field.append(["/"])
for i in range(COLS):
    field[0].append(i+1)

for i in range(ROWS):
    field.append([i+1])
    for _ in range(COLS):
        field[i+1].append("?")
        
mineMap = generate_map(ROWS, COLS, MINES)

complete_map(mineMap)

def format_input():
    inp = msvcrt.getch()
    if inp in (b'\x00', b'\xe0'):
        global curr_x, curr_y
        key = msvcrt.getch()
        
        def check_pos():
            global curr_x, curr_y
            if curr_y < 1:
                curr_y += 1
            if curr_x < 1:
                curr_x += 1
            if curr_y > ROWS:
                curr_y -= 1
            if curr_x > COLS:
                curr_x -= 1

        if key == b'H':
            curr_y -= 1
            check_pos()
            return curr_x, curr_y, None
        elif key == b'P':
            curr_y += 1
            check_pos()
            return curr_x, curr_y, None
        elif key == b'K':
            curr_x -= 1
            check_pos()
            return curr_x, curr_y, None
        elif key == b'M':
            curr_x += 1
            check_pos()
            return curr_x, curr_y, None
                
    return curr_x, curr_y, None

def play_loop():
    global correct_flags, flags
    print(f"Grid: ({ROWS}x{COLS}) | Mines: {MINES}| Flags: {flags}")
    #format_field(mineMap) # Debug only
    format_field(field)
    y, x, action = format_input()
    if action is None:
        field[x][y] = "■" # mouse cursor
    elif action == "b'\\r'":
        field[x+1][y+1] = mineMap[x][y]
        if mineMap[x][y] == "M":
            print("BOOOOM!!!")
            format_field(mineMap)
            return False
    elif action == "F":
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