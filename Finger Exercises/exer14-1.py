def keys_with_value(aDict, target):
    vals = []
    for ind in aDict:
        if aDict[ind] == target:
            vals.append(ind)
    return vals

aDict = {1:2, 2:4, 5:2}
target = 2
print(keys_with_value(aDict, target))