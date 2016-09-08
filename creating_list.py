L=[]
n=1
while n<100:
    L.append(n)
    n = n+2
    
    
print(L)

L=[]
for x in range(100):
    if x %2 == 1:
        L.append(x)
print(L)

L=list(range(100))
print(L[1::2])

input()
