#to generate a list of [1X1, 2X2, 3X3, ..., 10X10]

L=[]
for x in range(1,11):
    L.append(x*x)
    
print(L)

new_L=[x*x for x in range(1,11)]

print(new_L)

# to filter the list by adding if

new_L2=[x*x for x in range(1,11) if x%2==0]

print(new_L2)


new_L3=[m+n+x for m in 'ABC' for n in 'XYZ' for x in '123']

print(new_L3)

import os
file_dir=[d for d in os.listdir('.')]
print (file_dir)

d={'x':'A', 'y':'B','z':'C'}
new_L4=[k+'='+ v for k, v in d.items()]
print(new_L4)


L=['Hello','World','IBM','Apple']
new_L5= [s[0].lower()+s[1:]for s in L]
print(new_L5)

L=['Hello','World', 18, 'Apple', None]
new_L6=[s.lower() if isinstance(s, str) else s for s in L]
print(new_L6)

input()