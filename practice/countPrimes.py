def count_primes(num):
    
    if num <2:
        return 0
    
    primes = [2]
    x = 3
    
    #x is going througn every number up to input num
    
    while x <= num:
        #check if x is prime
        for y in range(3,x,2):
            if x%y ==0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
            
    print(primes)
    return len(primes)