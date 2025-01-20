def sum_str_lengths(L):
    count = 0
    for strn in L:
        if type(strn) == list:
            for chars in strn:
                if type(chars) == str:
                    count = count + len(chars)
                else:
                    raise ValueError
        elif type(strn) == str:
            count = count + len(strn)
        else:
            raise ValueError("Non-string entered")
    return count

print(sum_str_lengths(["abcd", ["e", "fg"]]))  
print(sum_str_lengths([12, ["e", "fg"]]))      
print(sum_str_lengths(["abcd", [3, "fg"]]))