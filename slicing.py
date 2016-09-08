L = ['Michael','Sarah','Tracy','Bob','Jack']

#to print the first 3 elements

print([L[0],L[1],L[2]])

r=[]
n=3
for i in range(n):
    r.append(L[i])
    
print(r)

print(L[0:3])

print(L[:3])

s = "Hello, Wayne"

print(s[:5])

#check out the difference
print(s[1:5])

#we can use negative integer to get the letter from back
print(s[-5:])

print(s[-5:-2])

L=list(range(100))
print(L)

#first 10 numbers:
print(L[:10])
#last 10 numbers
print(L[-10:])
#from 10 to 19
print(L[10:20])

# even numbers in the fisrt 10 numbers; here, 2 symbolizes
# an even number
print(L[0:10:2])
#every number that could be divided by 5
print(L[::5])

input()