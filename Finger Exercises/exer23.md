# Finger Exercise 23
## Question 1
``
def running_product(a):
    """ a is an int """
    product = 1
    for i in range(5,a+5):
        product *= i
        if product == a:
            return True
    return False
``
Big-theta $$\theta((n+5)-5)=\theta(n)$$
## Question 2
``
def tricky_f(L, L2):
    """ L and L2 are lists of equal length """
    inL = False
    for e1 in L:
        if e1 in L2:
            inL = True
    inL2 = False
    for e2 in L2:
        if e2 in L:
            inL2 = True
    return inL and inL2
``
Big-theta $$\theta(len(L))+\theta(len(L2))=\theta(max(len(L), len(L2)))$$
## Question 3
``
def sum_f(n):
    """ n > 0 """
    answer = 0
    while n > 0:
        answer += n%10
        n = int(n/10)
    return answer
``
Big-theta $$\theta(log_{10}(n)+1) = \theta(log_{10}(n))$$
