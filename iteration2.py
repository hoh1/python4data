d={'a':1,'b':2, 'c':3}
for key in d:
    print(key)
    
for value in d.values():
    print(value)
    
# (key,value)
for k,v in d.items():
    print(k,v)
    
s = "Hello, Mark!"
      
for c in s:
    print(c)
    
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))

print(isinstance(123, Iterable))

for i, value in enumerate(['A','B','C']):
    print(i, value)

input()