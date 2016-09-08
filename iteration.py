names = ['Michael','Bob','Tracy']
for x in names:
    print(x)
    
   
#to print sum of integers from 1 to 10
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)
#how about 1 to 100
# range() to generate lists containing arithmetic progressions

a = list(range(5))
print(a)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)
# another method
sum = 0
n = 100
while n>0:
    sum=sum+n
    n=n-1
print(sum)
# even number between 1-100
sum_even = 0
n = 0
while n<=100:
    sum_even=sum_even+n
    n=n+2
print(sum_even)

# sum of odd numbers
sum_odd = 0
n = 1
while n<= 100:
    sum_odd = sum_odd + n
    n = n + 2
print(sum_odd)

print(sum_even+sum_odd)

# to print names
L = ['Bart','Lisa','Adam']
# use while
i = 0
while i < len(L):
    print('Hello, %s!' % L[i])
    print('i is ', i)
    i = i+1
    print('after adding 1, i is', i)

# use for
for name in L:
    print('Hello, %s!' % name)
