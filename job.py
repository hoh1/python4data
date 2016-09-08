extra={'city':'Beijing', 'job': 'Engineer'}
person('Jack',24,**extra)
name:Jack age:24 other:{'city':'Beijing','job':'Engineer'}

def f1(a,b,c,=0, *args, **kw):
    print('a =',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

input()