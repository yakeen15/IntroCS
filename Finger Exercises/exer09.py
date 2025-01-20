def dot_product(tA, tB):
    sum = 0
    n = len(tA)
    for i in range(n):
        sum = sum + tA[i]*tB[i]
    return (n,sum)

tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB))