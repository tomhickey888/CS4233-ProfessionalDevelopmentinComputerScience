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

    print("Processesing functions with simplex pipes")

    #Start timer for primes with simplex pipes
    primesStart = time.time()

    #Spawns processes to perform primes function using two simplex pipes
    for c in range(int((cpus)/2)):
        primesDigest[c]=[]
        primesReader,primesWriter = mp.Pipe(False)
        primesReader2,primesWriter2 = mp.Pipe(False)
        p = mp.Process(target=primes.pipes, args=(min,max,primesWriter))
        p.start()
        primesDigest[c] = primesReader2.recv()
        p.join
    
    #End timer for primes with simplex pipes
    primesTime = time.time() - primesStart
    #Start timer for encrypt with simplex pipes
    encryptStart = time.time()

    #Spawns processes to perform encrypt function using two simplex pipes
    for c in range(int((cpus)/2)):
        encryptDigest[c]=[]
        encryptReader,encryptWriter = mp.Pipe(False)
        encryptReader2,encryptWriter2 = mp.Pipe(False)
        p = mp.Process(target=encrypt.pipes, args=(min,max,encryptWriter))
        p.start()
        encryptDigest[c] = encryptReader2.recv()
        p.join

    #End timer for encrypt with simplex pipes
    encryptTime = time.time() - encryptStart

    #Return a tuple of the times for primes and encrypt with two simplex pipes
    return (primesTime,encryptTime)