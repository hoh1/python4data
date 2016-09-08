def f(x):
    return x*x

r=map(f,[1,2,3,4,5,6,7,8,9])
list(r)
[1,4,9,16,25,36,49,64,81]

L=[]
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)
