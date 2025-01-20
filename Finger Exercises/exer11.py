def remove_and_sort(Lin, k):
    Lin[:] = list(Lin)
    if len(Lin)<=k:
        Lin[:] = []
    else:
        for i in range(k):
            Lin.remove(Lin[i])
    for i in range(len(Lin)):
        for j in range(i+1, len(Lin)):
            if Lin[i]>Lin[j]:
                temp = Lin[j]
                Lin[j] = Lin[i]
                Lin[i] = temp

L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)