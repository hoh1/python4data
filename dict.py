d = {'Michael':95, 'Bob':75, 'Tracy': 85}
print(d['Michael'])

d['Mark']=96
print(d)

d['Mark'] =69
print(d)

# print(d['Wayne'])

print('Wayne' in d)
# false means wayne does not exist in data
# none means the same
# print(d.get('Wayne'))
# print(d.get('Wayne'),-1)

print(d.pop('Bob'))
print(d)