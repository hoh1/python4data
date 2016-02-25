#tuple is immutable; can't be changed, thus safe
# tuple uses ( ), instead of [ ]

classmates = ('Michael','Bob','Tracy')
print(type(classmates))

print(classmates)

# classmates.append('Mark')

t=(1,2)
print(type(t))
print(t)

# if there is only one element inside the list. it translates as the type of that element, not duple
t=(1)
print(type(t))
print(t)
# if put comma(,), it recognizes it as duple even if there is only one element
t=(1,)
print(type(t))
print(t)

# value in the list can be changed even if it is inside the tuple, given that its in the list of the list
t=('a','b',['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
# t[0] = 'C' -> it incurs an error if try to change the list in the tuple
print(t)
