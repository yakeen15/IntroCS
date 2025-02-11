def flatten(L):
    L_new = []
    for item in L:
        if type(item) == type(L_new):
            L_new = L_new + flatten(item)
        else:
            L_new.append(item)
    return L_new

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L))