#Exercise 1
def normalize(name):
    pass
##to test:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
##output:
##['Adam', 'Lisa', 'Bart']

#Exercise 2
Use reduce() to calculate the production of a list

from functools import reduce
def prod(L):
    return reduce(lambda x, y: x*y, s)
    
def prod(L):
    def p(x,y):
        return x*y
    return reduce(p,L)   
  
print('3*5*7*9=', prod([3,5,7,9])