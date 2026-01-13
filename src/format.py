def format_field(f):
    _rows = len(f)
    for j in range(_rows):
        for i in f[j]:
            print(i, end=" ")
        print("") # \n