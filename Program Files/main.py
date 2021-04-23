#Import built-in functions for timing, file operations, and log file naming
import time
import os
from datetime import datetime

#Import custom functions to multiprocess data with Simplex Pipes, Duplex Pipes, and a Multiprocessing Pool
import simplexPipes
import duplexPipes
import multiprocessingPool

#File operations to set path for generating the log file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
path = os.getcwd() + "\Output"

#Creating the time stamp string used to name each log file to ensure data is not overwritten
now = datetime.today()
timeStamp = now.strftime("%m%d%y-%H%M-%S")

#Main driver program definition
if __name__ == "__main__":

    #Variables to determine how many loops to run in main and how many times each loop and function should be performed
    min = 1
    max = 10
    loops = 10
    mainLoops = 10

    #Index counter for main loop
    i=1

    #Lists to store output from each different type of multiprocessing for the Primes function
    simplexPrimes = []
    duplexPrimes = []
    multiPrimes = []

    #Lists to store output from each different type of multiprocessing for the Primes function
    simplexEncrypt = []
    duplexEncrypt = []
    multiEncrypt = []

    #Begin timer to track the entire program operation time
    mainStart = time.time()

    #Main loop for consistency/averaging potential - executes the entire loop however many times is specified by the mainLoop variable above
    while i <= mainLoops:

        print(f"\n\nBeginning main loop execution {i}\n")

        #Lists to capture output from each function that reset with each loop
        simplexTuples = []
        duplexTuples = []
        multiTuples = []

        #
        loopStart = time.time()

        #Execute the simplex pipes loop the number of times specified by the loop variable above
        for x in range(loops):
            simplexTuples.append(simplexPipes.run(min, max))
        
        #Execute the duplex pipes loop the number of times specified by the loop variable above
        for x in range(loops):
            duplexTuples.append(duplexPipes.run(min, max))

        #Execute the multiprocessing pool loop the number of times specified by the loop variable above
        for x in range(loops):
            multiTuples.append(multiprocessingPool.run(min, max))

        #Calculate and display the operation time for this main loop
        loopTime = time.time() - loopStart
        print(f"Main loop execution {i} complete, execution time: {loopTime} seconds")

        #Unpack each tuple from its output list into the correct list for the function it describes
        for tuple in simplexTuples:
            simplexPrimes.append(tuple[0])
            simplexEncrypt.append(tuple[1])
        for tuple in duplexTuples:
            duplexPrimes.append(tuple[0])
            duplexEncrypt.append(tuple[1])
        for tuple in multiTuples:
            multiPrimes.append(tuple[0])
            multiEncrypt.append(tuple[1])

        #Increment loop index counter
        i += 1

    #Calculate and display the total program operation time
    totalMain = time.time() - mainStart
    print(f"\n\nTotal execution time for program: {totalMain} seconds.")

    #Calculate Simplex Pipes statistics for data logging
    primesTotalSimplex = 0
    for x in simplexPrimes:
        primesTotalSimplex += x

    primesAverageSimplex = primesTotalSimplex / len(simplexPrimes)

    encryptTotalSimplex = 0
    for x in simplexPrimes:
        encryptTotalSimplex += x

    encryptAverageSimplex = encryptTotalSimplex / len(simplexEncrypt)

    totalSimplex = primesTotalSimplex + encryptTotalSimplex

    #Calculate Duplex Pipe statistics for data logging
    primesTotalDuplex = 0
    for x in duplexPrimes:
        primesTotalDuplex += x

    primesAverageDuplex = primesTotalDuplex / len(duplexPrimes)

    encryptTotalDuplex = 0
    for x in duplexPrimes:
        encryptTotalDuplex += x

    encryptAverageDuplex = encryptTotalDuplex / len(duplexEncrypt)

    totalDuplex = primesTotalDuplex + encryptTotalDuplex

    #Calculate Multiprocessing Pool statistics for data logging
    primesTotalMulti = 0
    for x in multiPrimes:
        primesTotalMulti += x

    primesAverageMulti = primesTotalMulti / len(multiPrimes)

    encryptTotalMulti = 0
    for x in multiPrimes:
        encryptTotalMulti += x

    encryptAverageMulti = encryptTotalMulti / len(multiEncrypt)

    totalMulti = primesTotalMulti + encryptTotalMulti

    #Begin plotting operations
    

    #Begin file operations
    print('\nBeginning file operations:')

    #Only continue if there are no file errors when creating the new file
    try:
        print('Processing...')

        #Open the file in the path specified at the beginning of the program and with a filename including the time stamp and record log information
        with open(file = f"{path}\log-{timeStamp}.txt", mode = 'x', encoding = 'utf-8') as f:
            f.write(f'##########################################################################################\n')
            f.write(f'Total Program time taken: {totalMain:.3f}\n\n')

            f.write(f'Average processing time for Primes function using Simplex Pipes: {primesAverageSimplex:.3f}\n')
            f.write(f'Average processing time for Encrypt function using Simplex Pipes: {encryptAverageSimplex:.3f}\n')
            f.write(f'Total processing time for all functions using Simplex Pipes: {totalSimplex:.3f}\n')
            f.write(f'Percentage of processing time used for Primes function using Simplex Pipes: {primesTotalSimplex/totalSimplex:.3f}\n')
            f.write(f'Percentage of processing time used for Encrypt function using Simplex Pipes: {encryptTotalSimplex/totalSimplex:.3f}\n')
            f.write(f'Percentage of processing time used for all functions using Simplex Pipes: {totalSimplex/totalMain:.3f}\n\n')

            f.write(f'Average processing time for Primes function using a Duplex Pipe: {primesAverageDuplex:.3f}\n')
            f.write(f'Average processing time for Encrypt function using a Duplex Pipe: {encryptAverageDuplex:.3f}\n')
            f.write(f'Total processing time for all functions using a Duplex Pipe: {totalDuplex:.3f}\n')
            f.write(f'Percentage of processing time used for Primes function using a Duplex Pipe: {primesTotalDuplex/totalDuplex:.3f}\n')
            f.write(f'Percentage of processing time used for Encrypt function using a Duplex Pipe: {encryptTotalDuplex/totalDuplex:.3f}\n')
            f.write(f'Percentage of processing time used for all functions using a Duplex Pipe: {totalDuplex/totalMain:.3f}\n\n')

            f.write(f'Average processing time for Primes function using a Multiprocessing Pool: {primesAverageMulti:.3f}\n')
            f.write(f'Average processing time for Encrypt function using a Multiprocessing Pool: {encryptAverageMulti:.3f}\n')
            f.write(f'Total processing time for all functions using a Multiprocessing Pool: {totalMulti:.3f}\n')
            f.write(f'Percentage of processing time used for Primes function using a Multiprocessing Pool: {primesTotalMulti/totalMulti:.3f}\n')
            f.write(f'Percentage of processing time used for Encrypt function using a Multiprocessing Pool: {encryptTotalMulti/totalMulti:.3f}\n')
            f.write(f'Percentage of processing time used for all functions using a Multiprocessing Pool: {totalMulti/totalMain:.3f}\n')
            f.write(f'##########################################################################################\n\n')

            f.write(f'Processing complete, closing file.\n')

    #If the file operations terminate with an error indicating a file with the specified filename already exists, display this message and terminate program
    except FileExistsError:
        print('\nLog file already exists - Terminating program to protect data\n\n')

    #If the file operations terminate with a file error other than above, display this message and terminate program
    except:
        print('\nUnknown file error occured - Terminating program to protect data\n\n')

    #If the file operations complete successfully, display this message and terminate program
    finally:
        print('File operations complete - Terminating program\n\n')