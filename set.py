s = set([1, 2, 3])
print(s)
# keys cannot be duplicate
s.add(4)
print(s)
s.remove(4)
print(s)

s1 = set([1,2,3])
s2 = set([2,3,4])

print('intersection:',s1&s2)
print('union:', s1|s2)

# For mutable (won't function if different type)
a=['c', 'b', 'a']
a.sort(reverse=True)
print(a)

b=[342,543,3.54,453663]
b.sort()
print(b)

# For Immutable(i.e Strings)
a= 'abc'
b= a.replace('a','A')
print(a)
print(b)

