N = 1000
flag = False
i = 2
while i**3<=N:
    if i**3==N:
        flag = True
        break
    i = i + 1

if flag:
    print(i)
else:
    print("error")