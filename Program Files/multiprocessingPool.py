#Import built-in functions for multiprocessing and timing
import multiprocessing as mp
import time

#Import custom functions to process primes and encrypt
import primes
import encrypt

#Store the number of cores in the CPU to control number of processes to spawn
cpus = int(mp.cpu_count())

#Pass in the minimum and maximum numbers from main to pass as arguments to primes and encrypt
def run(min, max):

    #Create dictionaries to store the results from the spawned processes
    primesDigest = {}
    encryptDigest = {}

    print("Processing functions with a multiprocessing pool")

    #Start timer for primes with a multiprocesing pool
    primesStart = time.time()

    #Spawns processes to perform primes function using a multiprocessing pool
    for c in range(int((cpus)/2)):
        primesDigest[c]=[]
        with mp.Pool(int((cpus)/2)) as pool:
            primesDigest[c] = pool.apply(primes.multi,(min,max))

    #End timer for primes with a multiprocessing pool
    primesTime = time.time() - primesStart

    #Start timer for encrypt with a multiprocessing pool
    encryptStart = time.time()

    #Spawns processes to perform encrypt function using a multiprocessing pool
    for c in range(int((cpus)/2)):
        encryptDigest[c]=[]
        with mp.Pool(int((cpus)/2)) as pool:
            primesDigest[c] = pool.apply(encrypt.multi,(min,max))
    
    #End timer for encrypt with a multiprocessing pool
    encryptTime = time.time() - encryptStart

    #Return a tuple of the times for primes and encrypt with a multiprocessing pool
    return (primesTime,encryptTime)