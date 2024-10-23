# Timing Programs, Counting Operations

# Writing Efficient Programs

# Efficiency is important
## Separate time and space efficiency of a program
## Tradeoff between them: can use up a bit more memory to store values for quiker lookup later
### Think Fibonacci recursive vs Fibonacci with memorization
## Challenges in understanding efficiency
### A program can be implemented in many different ways
### You can solve a problem using only a handful of different algorithms
## Want to separate choice of implementation from choice of more abstract algorithm

# Evaluating Programs
## Measure with a timer
## Count the operations
## Abstract notion of order of growth

# Aside on Modules
## A module is a set of python definitions in a file
## Pyuthon provides many useful modules: math, plotting/graphing, random, etc
## You first need to import the module into your environment
import time
import random
import dateutil
import math
## call funtions from inside the module using the modules' name and dot notation
math.sin(math.pi/2)

def c_to_f(c):
    return c*9.0/5 + 32
# tstart = time.time() # Start clock
# c_to_f(37)
# dt = time.time() - tstart # Stop clock
# print(dt, "s,")

def mysum(x):
    total = 0
    for i in range(x+1):
        total += i
    return total

def square(n):
    sqsum = 0
    for i in range(n):
        for j in range(n):
            sqsum += 1
    return

def time_wrapper(f, L):
    """
    :param f: is a function to test
    :param L: number of iterations
    :return:
    """
    print('Timing', f.__name__)
    for i in L:
        t = time.time()
        f(i)
        dt = time.time()-t
        print(f"{f.__name__}({i}) took {dt} sec")
L_N = [1]
for i in range(8):
    L_N.append(L_N[-1]*10)

time_wrapper(square, L_N)

# Timing Programs is inconsistent
## Goal: to evaluate differnet algorithms
## Running time should vary between algorithm
## Running time should not vary between implementations (x)
## Running time should not vary between computers (x)
## Running time should not vary between languages (x)
## Running time should be predictable for small inputs

## Time varies for different inputs but cannot really express a relationship b/w inputs and time needed
## Can only be measured a posteriori

# Counting Operations
## Assume these steps take constant time: (c_to_f, mysum, square)
### Mathematical operations
### Comparisions
### Assignments
### Accessing objects in memory
## Count number of operations executed as function of size of input
### c_to_f -> 3 / mysum -> total+=1 two ops, for i in range(x+1): one op -> 1*(x+1)(1+2)
### square 1op for sqsum = 0 / for i in range(n) one op, for j in range one sqsum +=1 2ops
### so that 1+n*1*n*(1+2)

def c_to_f(c):
    counter = 3
    return (counter, c*9.0/5 + 32)

def mysum(x):
    counter = 1
    total = 0
    for i in range(x+1):
        counter += 3
        total += i
    return (counter, total)

def square(n):
    counter = 1
    sqsum = 0
    for i in range(n):
        counter += 1
        for j in range(n):
            counter += 3
            sqsum += 1
    return (counter, square)

# Counting Operations is independent of computer variations but,
## Goal: To evaluate different algorithms
## Running "time" should vary between algorithms
## Running "time" should vary between implementations (X)
## Running "time" should not vary between computers
## Running "time" should not vary between languages
## Running "time" should be predictable for small amounts
## No real definition of which operations to count
## Count varies for different inputs and can derive a relationship between inputs and the count
