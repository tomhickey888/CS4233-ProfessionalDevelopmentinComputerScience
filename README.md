# Capstone
 CS4233 - Professional Development in Computer Science

## Introduction
This project is intended to be the pinnacle of my bachelor's degree work.  This purpose of this project was to design software to perform CPU-intensive tasks in parallel using three different aspects of the multiprocessing module in Python.  The three methods of communication between the main process and the subprocesses that were evaluated were simplex pipes, duplex pipes, and the multiprocessing pool module.  By recording the processing time of each the efficiency of the three different methods of communication can be measured quantitatively.

## Table of Contents
- [Documentation](Documentation/README.md)
- [Program Files](Program%20Files/README.md)

## Usage Instructions
This program can be utilized by opening the main.py file in a Python IDE.  Special attention needs to be paid to the following variables before running the script:


```
    min
```
This is the minimum number passed into the encryption and primes functions.  Adjust with max to determine the range processed and size of data passed.
```
    max
```
This is the maximum number passed into the encryption and primes functions.  Adjust with min to determine the range processed and size of data passed.
```
    loops
```
This is the number of times that each of the three multiprocessing functions will be executed in each loop of the main script.
```
    mainLoops
```
This is the number of loops of the main script will be executed.


After adjusting those variables, simply run the main.py script.  The console will display the current status of the script as it cycles through the various functions that it contains.  After the script is finished, check the Output directory for a text file that will contain a summary of the data measured.  The filename of the output file will be automatically generated as a timestamp for when the script was run.

## Sample Output
This is a sample output file that could be generated from a test run through the main script:

```
##########################################################################################
Total Program time taken: 891.423

Average processing time for Primes function using Simplex Pipes: 2.145
Average processing time for Encrypt function using Simplex Pipes: 2.145
Total processing time for all functions using Simplex Pipes: 429.067
Percentage of processing time used for Primes function using Simplex Pipes: 0.500
Percentage of processing time used for Encrypt function using Simplex Pipes: 0.500
Percentage of processing time used for all functions using Simplex Pipes: 0.481

Average processing time for Primes function using a Duplex Pipe: 2.125
Average processing time for Encrypt function using a Duplex Pipe: 2.125
Total processing time for all functions using a Duplex Pipe: 425.004
Percentage of processing time used for Primes function using a Duplex Pipe: 0.500
Percentage of processing time used for Encrypt function using a Duplex Pipe: 0.500
Percentage of processing time used for all functions using a Duplex Pipe: 0.477

Average processing time for Primes function using a Multiprocessing Pool: 2.337
Average processing time for Encrypt function using a Multiprocessing Pool: 2.337
Total processing time for all functions using a Multiprocessing Pool: 467.325
Percentage of processing time used for Primes function using a Multiprocessing Pool: 0.500
Percentage of processing time used for Encrypt function using a Multiprocessing Pool: 0.500
Percentage of processing time used for all functions using a Multiprocessing Pool: 0.524
##########################################################################################

Processing complete, closing file.
```

## Runtime Enviornment
This software was designed and tested in the following runtime enviornment:

### Hardware:
- Intel Core i5-9300H CPU
- 8.0 GB Physical Main Memory
- 25.8 GB Virtual Main Memory

### Software:
- Windows 10.0 Home Build 19041
- Visual Studio Code 1.55.1
- Python 3.8.8 64-bit programming environment

## License
[MIT License](LICENSE)
