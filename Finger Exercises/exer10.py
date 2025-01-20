def all_true(n, Lf):
    flag = True
    for func in Lf:
        flag = flag and func(n)
    return flag

def even(n):
    if n%2==0:
        return True
    else:
        return False
    
print(all_true(6, [even]))