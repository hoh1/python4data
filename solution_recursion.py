def move(n, source, bridge, destination):
    if n==1:
        print('%s --> %s' % (source, destination))
    else:
        move(n-1, source, destination, bridge) #move n-1 plates from origin to bridge
        print('%s --> %s' % (source,destination)) #move the largest plate from origin to destination
        move(n-1, bridge, source, destination) # move n-1 plate from bridge to destination
        
move(4, 'A', 'B', 'C')
    
input()