def eval_quadratic(a, b, c, x):
    return a*x**2+b*x+c

def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    print(eval_quadratic(a1,b1,c1,x1)+eval_quadratic(a2,b2,c2,x2))

two_quadratics(1,1,1,1,1,1,1,1)
print(two_quadratics(1,1,1,1,1,1,1,1))