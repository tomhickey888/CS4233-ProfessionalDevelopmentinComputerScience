# Capstone
 CS4233 - Professional Development in Computer Science

## Introduction
This project is intended to be the pinaccle of my bachellor's degree work.  This purpose of this project was to design software to perform CPU-intensive tasks in parallel using three different aspects of the multiprocessing module in Python.  The three methods of communication between the main process and the subprocesses that were evaluated were simplex pipes, duplex pipes, and the multiprocessing pool module.  By recording the processing time of each the efficiency of the three different methods of communication can be measured quantitatively.

## Table of Contents
- [Output](Output/README.md)
- duplexPipes.py – This is the file imported into main to run the two functions using duplex pipes
- encrypt.py – This is the encryption function called by all three of the multiprocessing functions
- main.py – This is the driver for the program
- multiprocessingPool.py – This is the file imported into main to run the two functions using a multiprocessing pool
- primes.py – the prime number function called by all three of the multiprocessing functions
- simplexPipes.py – This is the file imported into main to run the two functions using simplex pipes

## License
[MIT License](LICENSE)