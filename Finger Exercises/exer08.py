def same_chars(s1, s2):
    flag = True
    for char in s1:
        if char not in s2:
            flag = False
            break
    for char in s2:
        if char not in s1:
            flag = False
    return flag

print(same_chars("abc", "cab"))  
print(same_chars("abccc", "caaab")) 
print(same_chars("abcd", "cabaa")) 
print(same_chars("abcabc", "cabz"))