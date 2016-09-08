import math
def quadratic(a,b,c):
    w=b*b-4*a*c
    if w<0:
        print('Error, b*b-4*a*c could not be less than '0')
        return None
else:
    x1=(-b + math.sqrt(w))/(2*a)
    x2=(-b - math.sqrt(w))/(2*a)
    return (x1,x2)