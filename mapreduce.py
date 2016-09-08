def f(x):
    return x*x

#map reduce

r=map(f,[1,2,3,4,5,6,7])
print(list(r))

#converting numbers to strings

print(list(map(str,[1,2,3,4,5,6,7,8,9])))


#reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)
#have to call from package
from functools import reduce

def add(x,y):
    return x*x + y*y

print(reduce(add,[1,2,3,4]))


#
def fn(x,y):
    return 10*x+y
    
print(reduce(fn,[1,3,5,7,9]))

#how to switch str to int? 
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

print(char2num('3'))

print(reduce(fn,map(char2num,'13579')))


#normlize


def normalize(name):
    low_name=name.lower()
    first_letter = {'a':'A','b':'B','c':'C','d':'D','e':'E','f':'F','g':'G','h':'H','i':'I','j':'J','k':'K','l':'L','m':'M','n':'N','o':'O',
    'p':'P','q':'Q','r':'R','s':'S','t':'T','u':'U','v':'V','w':'W','x':'X','y':'Y','z':'Z'}[low_name[0]]
    new_name=first_letter+low_name[1:]
    return new_name
    
    
#to test
L1=['adam','LISA','barT']
L2=list(map(normalize,L1))
print(L2)



#use reduce() to calculate the production of a list
#from functools import reduce
def fn2(x,y):
    return x*y
def prod(L=[]):
    return reduce(fn2,L)


print("3 * 5 * 7 * 9 =", prod([3,5,7,9]))

input()