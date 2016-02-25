classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

#len -> length
print(len(classmates))
# we always count from 0, not 1; so michael is located at 0, not 1.
# could use -1 to get the last element
# use square bracket to indicate the location of the data
print(classmates[-1])

classmates[len(classmates)-1]
print(type(len(classmates)))

# use append to add new element to the last part of the existing data set
classmates.append('Adam')
print(classmates)

# use insert to specify the locaiton of the new data
classmates.insert(1,'Jack')
print(classmates)

# use to remove the last one. If specify the location, it deletes the data in that location
print(classmates.pop(1))
print(classmates)

classmates[1] = 'Wayne'
print(classmates)

# we can use double bracket to indicate the element in the bracket of the bracket 
s=['python','java',['asp', [1,True,'February'],'php'],'scheme']

print(s[2])
print(s[2][1])
print(s[2][1][2])

# L=[] empty list <- note, that it is square bracket
L=[]
L.append('Apple')
L[0]='Google'
print(L)

L=[
    ['Apple','Google','Microsoft'],
    ['Java','Python','Ruby','PHP'],
    ['Adam','Bart','Lisa']
]
print(L[0][0]) # print apple
print(L[1][1]) # print Python
print(L[2][2]) # print Lisa


new_class= classmates + ['John','Mike']
print(new_class)

new_class[2:4]=[]
print(new_class)

new_class.remove('Wayne')
print(new_class)

# to reverse the order
new_class.reverse()
print(new_class)

vec = [-4,-2,0,2,4]
vec2 = [x*2 for x in vec]
print(vec2)

c=[x+' LastName' for x in new_class]
print(new_class)
print(c)

# to see the list of the numbers
numbers=list(range(1,101))
print(numbers)
# to do calc for numbers in the existing list
# 2 astericks represent ^ (** => ^)
numbers =[x**2 for x in numbers]
print(numbers)



