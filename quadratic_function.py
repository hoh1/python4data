from quadraticfunction import my_quadratic

def quadratic(a,b,c):
    w=b*b-4*a*c
    if w<0:
        print('Error, b*b-4*a*c could not be less than '0')
        pass
else:
    x1=-b+((sqrt(b^2-4*a*c))/2*a)
    x2=-b-((sqrt(b^2-4*a*c))/2*a)
    return (x1,x2)
    
input()
print(quadratic(2,3,1)) # -> (-0.5, -1.0)
print(quadratic(1,3,-4)) # -> (1.0, -4.0)

