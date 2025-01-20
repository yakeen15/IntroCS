def bisec_search(N, a, b, count=0):
    i = count
    mid = round((a+b)/2)
    if N>mid:
        return bisec_search(N,mid,b,count = i+1)
    elif N<mid:
        return bisec_search(N,a,mid,count = i+1)
    else:
        return N, i
    
N = 500
guess, count = bisec_search(N, 0, 1000)
print(guess)
print(count+1)