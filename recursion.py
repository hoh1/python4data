
#factorial
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
    
print(fact(3))



def move(n,a,b,c):
    if n==3:
        print(a,'-->',c)
        print(a,'-->',b)
        print(c,'-->',b)
        print(a,'-->',c)
        print(b,'-->',a)
        print(b,'-->',c)
        print(a,'-->',c)
#expected output
#A --> C 
#A --> B 
#C --> B 
#A --> C
#B --> A 
#B --> C 
#A --> C 
move(3,'A','B','C')




input()