def primes():
    yield 2
    it = _odd_iter() #initilization
    while True:
        n=next(it) # return the first number of 
current list
        yield n 
        it = filter(_not_divisible(n), it) # create a new list
        
      