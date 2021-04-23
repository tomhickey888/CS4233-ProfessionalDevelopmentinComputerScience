
#Returns a list of primes from a given range of (min) to (max) to its parent process using a pipe (writer)
def pipes(min, max, writer):
    primes = []

    for n in range(min, max):
        flag = 0
        if n <=1:
            continue
        for i in range(2, n): 
            if n % i == 0:
                flag = 1
                break
        if(flag == 0):
            primes.append(n)

    writer.send(primes)
    writer.close

#Returns a list of primes from a given range of (min) to (max) to its parent process directly for multiprocessing with a pool
def multi(min, max):
    primes = []

    for n in range(min, max):
        flag = 0
        if n <=1:
            continue
        for i in range(2, n): 
            if n % i == 0:
                flag = 1
                break
        if(flag == 0):
            primes.append(n)

    return(primes)
