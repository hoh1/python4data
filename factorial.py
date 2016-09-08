def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

input()
#Expected output using recursion
#A-->C
#A-->B
#C-->B
#A-->C
#B-->A
#B-->C
#A-->C
#move(3,'A','B','C')