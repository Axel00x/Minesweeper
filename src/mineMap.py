import random as r


def generate_map(rows, cols, num):
    mineMap = []
    
    choices = [0 for i in range(rows*cols)]
    
    for i in range(num):
        if choices[i] == 0:
            choices.insert(choices.pop(i), 1)
        
    for i in range(rows):
        mineMap.append([])
        for _ in range(cols):
            mine = r.choice(choices)
            if mine == 1: choices.remove(1)
            else: choices.remove(0)
            mineMap[i].append(mine)
    
    return mineMap

print(generate_map(6, 6, 16))