my_str = "somerandomtext"
new_str = []
for i in range(len(my_str)):
    if (i+1)%2==0:
        new_str.append(my_str[i])

for char in new_str:
    print(char, end="")