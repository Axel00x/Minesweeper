def complete_map(mMap):
    _rows = len(mMap)
    _cols = len(mMap[0])
    
    for i in range(_rows):
        for j in range(_cols):
            if mMap[i][j] == 1:
                mMap[i][j] = "M" # Replace 1 with M (idk why I choose 1 for the mine, now it's too late)

    for i in range(_rows):
        for j in range(_cols):
            if mMap[i][j] == "M":
                try:
                    if j-1 >= 0: # check if j can go -1
                        if mMap[i][j-1] != "M": # check left
                            mMap[i][j-1] += 1
                except: ...
                try:
                    if mMap[i][j+1] != "M": # check right
                        mMap[i][j+1] += 1
                except: ...
                try:
                    if i-1 >= 0:
                        if mMap[i-1][j] != "M": # check top
                            mMap[i-1][j] += 1
                except: ...
                try:
                    if mMap[i+1][j] != "M": # check bottom
                        mMap[i+1][j] += 1
                except: ...
                try:
                    if i-1 >= 0 and j-1 >= 0:
                        if mMap[i-1][j-1] != "M": # check top-left
                            mMap[i-1][j-1] += 1
                except: ...
                try:
                    if i-1 >= 0:
                        if mMap[i-1][j+1] != "M": # check top-right
                            mMap[i-1][j+1] += 1
                except: ...
                try:
                    if j-1 >= 0:
                        if mMap[i+1][j-1] != "M": # check bottom-left
                            mMap[i+1][j-1] += 1
                except: ...
                try:
                    if mMap[i+1][j+1] != "M": # check bottom-right
                        mMap[i+1][j+1] += 1
                except: ...
                
    return mMap