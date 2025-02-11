def all_positive(d):
    vals = []
    for ind in d:
        sum = 0
        for item in d[ind]:
            sum = sum + item
        if sum > 0:
            vals.append(ind)
            vals.sort()
    return vals

d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))