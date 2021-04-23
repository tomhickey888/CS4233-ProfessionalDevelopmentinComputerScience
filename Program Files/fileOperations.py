import time
import os
from datetime import datetime
import multiprocessing as mp

import primes
import encrypt

os.chdir(os.path.dirname(os.path.abspath(__file__)))

path = os.getcwd() + "\Output"

now = datetime.today()
x = now.strftime("%m%d%Y%H%M%S")

cpus = int(mp.cpu_count())

def run(min, max):
    print('\nBeginning file operations:')

    try:
        print('Processing...')
        with open(file = f"{path}\log{x}.txt", mode = 'x', encoding = 'utf-8') as f:
            primesDigest = {}
            encryptDigest = {}

            f.write("Beginning primes function with simplex pipes:\n\n")

            primesAccumulater = 0.0
            primesIncrementer = 0

            primesStart = time.time()

            for c in range(int((cpus)/2)):
                primesDigest[c]=[]
                primesReader,primesWriter = mp.Pipe(False)
                start = time.time()
                p = mp.Process(target=primes.pipes, args=(min,max,primesWriter))
                p.start()
                primesDigest[c] = primesReader.recv()
                p.join
                end = time.time() - start
                f.write(f'Process primes{c} reports: Data received and recorded.\n')
                f.write(f'Process time for primes on processor {c+1}: {end:.3f}\n\n')
                primesAccumulater += end
                primesIncrementer += 1

            primesTime = time.time() - primesStart
                        
            primesAverageSimplex = primesAccumulater/primesIncrementer


            f.write("\nBeginning encryption function with simplex pipes:\n\n")

            encryptAccumulater = 0.0
            encryptIncrementer = 0

            encryptStart = time.time()

            for c in range(int((cpus)/2)):
                encryptDigest[c]=[]
                encryptReader,encryptWriter = mp.Pipe(False)
                p = mp.Process(target=encrypt.pipes, args=(1,1000,encryptWriter))

                start = time.time()
                p.start()
                encryptDigest[c] = encryptReader.recv()
                p.join
                end = time.time() - start

                f.write(f'Process encrypt{c} reports: Data received and recorded.\n')
                f.write(f'Process time for encrypt on processor {c+5}: {end:.3f}\n\n')
                encryptAccumulater += end
                encryptIncrementer += 1

            encryptTime = time.time() - encryptStart
                        
            encryptAverageSimplex = encryptAccumulater/encryptIncrementer

            f.write(f'\nTotal processing time for simplex pipes primes function: {primesTime:.3f}\n')
            f.write(f'Total processing time for simplex pipes encryption function: {encryptTime:.3f}\n\n\n')

            print('Adding data summary...')
            f.write(f'##########################################################################################\n')
            f.write(f'Total Program time taken: \n\n')

            f.write(f'Average processing time for Primes function using Simplex Pipes: {primesAverageSimplex:.3f}\n')
            f.write(f'Average processing time for Encrypt function using Simplex Pipes: {encryptAverageSimplex:.3f}\n')
            f.write(f'Total processing time for all functions using Simplex Pipes: {(primesTime + encryptTime):.3f}\n')
            f.write(f'Percentage of processing time used for Primes function using Simplex Pipes: {primesTime/(primesTime + encryptTime):.3f}\n')
            f.write(f'Percentage of processing time used for Encrypt function using Simplex Pipes: {encryptTime/(primesTime + encryptTime):.3f}\n')
            f.write(f'Percentage of processing time used for all functions using Simplex Pipes: {(primesTime + encryptTime)/(primesTime + encryptTime):.3f}\n\n')

            f.write(f'Average processing time for Primes function using a Duplex Pipe: \n')
            f.write(f'Average processing time for Encrypt function using a Duplex Pipe: \n')
            f.write(f'Total processing time for all functions using a Duplex Pipe: \n')
            f.write(f'Percentage of processing time used for Primes function using a Duplex Pipe: \n')
            f.write(f'Percentage of processing time used for Encrypt function using a Duplex Pipe: \n')
            f.write(f'Percentage of processing time used for all functions using a Duplex Pipe: \n\n')

            f.write(f'Average processing time for Primes function using a Multiprocessing Pool: \n')
            f.write(f'Average processing time for Encrypt function using a Multiprocessing Pool: \n')
            f.write(f'Total processing time for all functions using a Multiprocessing Pool: \n')
            f.write(f'Percentage of processing time used for Primes function using a Multiprocessing Pool: \n')
            f.write(f'Percentage of processing time used for Encrypt function using a Multiprocessing Pool: \n')
            f.write(f'Percentage of processing time used for all functions using a Multiprocessing Pool: \n')
            f.write(f'##########################################################################################\n\n')

            f.write(f'\nProcessing complete, closing file.\n\n\n')

    except FileExistsError:
        print('Log file already exists - Terminating program to protect data\n\n')

    except:
        print('Unknown file error occured - Terminating program to protect data\n\n')

    finally:
        print('File operations complete - Terminating program\n\n')
        

if __name__ == '__main__':
    run(1,1000)