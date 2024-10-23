# Big Oh and Theta
import time
def convert_to_km(m):
    return m*1.609
# t0 = time.perf_counter() # more accurate timer, meaningful when used to get a time diff
# convert_to_km(m)
# dt = time.perf_counter() - t0
# print("t =", dt, "s,")

def compound(invest, interest, n_months):
    total = 0
    for i in range(n_months):
        total = total * interest + invest
    return total

L_N = [1]
for i in range(7):
    L_N.append(L_N[-1]*10)

for N in L_N:
    t = time.perf_counter()
    km = convert_to_km(N)
    dt = time.perf_counter() - t
    print(f'convert_to_km({N}) took {dt} seconds ({1/dt}/sec)')

for N in L_N:
    t = time.perf_counter()
    km = compound(N, 1.05, 12)
    dt = time.perf_counter() - t
    print(f'compound({N}) took {dt} seconds ({1/dt}/sec)')

# Measure Time: Sum over L
def sum_of(L):
    total = 0.0
    for elt in L:
        total = total + elt
    return total

for N in L_N:
    L = list(range(N)) # [0,1,...,9] to [0,1,2,...,99] to ...
    t = time.perf_counter()
    km = sum_of(L)
    dt = time.perf_counter() - t
    print(f'sum_of({N}) took {dt} seconds ({1/dt}/sec)')

# observation 1: Size of the input is now the length of the list, not how big the element numbers are
# observation 2: average time seems to increase by 10 as size of argument increases by 10
# observation 3: relationship b/w size and time only predictable for large sizes
# observation 4: Time seems comparable to computation of compound

# Measure Time: Find element in a list
## Search each element one by one
def is_in(L, x):
    for elt in L:
        if elt == x:
            return True
    return False

## Search by bisecting the list (list should be sorted)!
def binary_search(L, x):
    lo = 0
    hi = len(L)
    while hi-lo > 1:
        mid = (hi+lo) // 2
        if L[mid] <= x:
            lo = mid
        else:
            hi = mid
    return L[lo] == x

## Search using built in operator
x in L

# observation 1: searching one-by-one grows by factor of 10, when L increases by 10
# observation 2: built-in function grows by factor of 10, when L increases by 10
# observation 3: binary search time seems almost independent of size
# observation 4: binary search much faster than is_in, especially on larger problems
# observation 5: is_in is slightly slower than using Python's "in" capability

import math
# Measure Time: Diameter function
def diameter(L):
    farthest_dist = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            p1 = L[i]
            p2 = L[j]
            dist = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
            if dist > farthest_dist:
                farthest_dist = dist
    return farthest_dist

def create_list_of_2D_points(N):
    L=[]
    for i in range(N):
        x = math.cos(i)*i
        y = math.sin(i)*i
        L.append((x,y))
    return L

L_N = [100, 200, 400, 800, 1600, 3200, 6400]

diameter_times = []
last = 0
for N in L_N:
    L = create_list_of_2D_points(N)
    t = time.perf.counter()
    d = diameter(L)
    dt = time.perf.counter() - t
    diameter_times.append(dt)
    print("diameter of", N, "points took", dt, "seconds")
    if (last != 0):
        print(f"   delta = {dt/last:.1f}x for 2x as many6 points")
    last = dt

# Don't get me wrong!
## Timing is a critical tool to assess the performance of programs
### At the end of the day, it is irreplacable for real-world assessment
## But we will see a complementary tool (asymptotic complexity) that has other advantages
### A priori evaluation (before writing or running code)
### Assesses algorithm independent of machine and implementation (what is intrinsic efficiency of algorithm?)
### Provides direct insight into the design of efficient algorithms

# Counting
## Count operations : is_in
def is_in_counter(L,x):
    global count # make python access the count variable outside of the function => Function can modify the variable
    count += 1
    for elt in L:
        count += 2
        if elt == x:
            return True
    return False
# Global lets us reference and change an external variable inside a function - OK for debugging/Timing but not good practice in real programs
is_in_counts = []
for N in L_N:
    count = 0
    L = range(N)
    for x in [L[0], L[len(L)//2], L[-1]]:
        my_bool = is_in_counter(L,x)
    print('is_in_with', N, 'elements did', count, 'operations')
    is_in_counts.append(count)

# Count operations: binary search
def binary_search_counter(L, x):
    global count
    lo = 0
    hi = len(L)
    while hi-lo > 1:
        count += 2
        mid = (hi+lo) // 2
        count += 3
        if L[mid] <= x:
            lo = mid
        else:
            hi = mid
        count += 3
    return L[lo] == x

is_in_counts = []
for N in L_N:
    count = 0
    L = range(N)
    for x in [L[0], L[len(L)//2], L[-1]]:
        my_bool = binary_search_counter(L,x)
    print('binary_search_counter', N, 'elements did', count, 'operations')
    is_in_counts.append(count)

# Problems with Timing and Counting
## Timing the exact running time of the program
### depends on machine
### depends on implementation
### Small inputs don't show growth
## Counting the exact number of step
### Get us a formula
### Machine independent, which is good
### Depends on implementation
### Multiplicative/additive constants are irrelevant for large inputs
## Want to:
### evaluate algorithm
### evaluate scalability
### evaluate in terms of input size

# order of growth
## it's a notation
## evaluates programs when input is very big
## expresses the growth of programs's run time
## puts an upper bound on growth
## Do not need to be precise: "order of" not "exact" growth
## Focus on the largest factors in run time (which section of the program will take the longest to run)

# a better way: A generalized way with approximations
## Use the idea of counting operations in an algorithm but not worry about small variations in implementation
### When x is big, 3x + 4 and 3x and x are pretty much the same!
### don't care about exact value ops = 1+x(2+1)
### Express it in an "order of" way vs the input: ops = Order of x
## Focus on how algorithm performs when size of problem gets arbitrarily large
## Relate time needed to complete a computation against the size of the input to the problem
## Need to decide what to measure. What is the input?

# Which input to use to measure efficiency?
## Want to express efficiency in terms of input, so need to decide what is your input

# Different inputs change how the program runs
def is_in(L,e): # lenth of L matters in the program
    for i in L:
        if i == e:
            return True
    return False

# Asymptotic growth
## Goal: describe how time grows as size of input grows
### Formula relating input to number of operations
## Given an expression for the number of operations needed to compute an algorithm
## want to know asymptotic behavior as size of problem gets large
### want to put a bound on growth
### do not need to be precise: "order of" not "exact" growth
## Will focus on term that grows most rapidly
### ignore additive and multiplicative constants, since want to know how rapidly time required increases as we increase
### the size of input
## This is called order of growth
### Use mathematical notions of "big O" and "big theta"

# Big O definition
## Suppose some code runs in f(x) = 3x^2 + 20x + 1 steps
### Think of this as the formula from counting the number of obs
## Big Oh is a way to upper bound growth of any function
## f(x) = O(g(x)) means that g(x) times some constant eventually always exceeds f(x)
### Eventually means above some threshold value of x
### 4x^2 > 3x^2 + 20x + 1 for all x > 20.04
### hence, 3x^2 + 20x + 1 = O(x^2)

# Big O formally
## A big Oh bound is an upper bound on the growth of some function
## f(x) = O(g(x)) means there exist constants c0 x0 for which c0g(x) >= f(x) for all x>x0

# Big Theta definition
## A big theta bound is a lower and upper bound on the growth of some function
### Suppose f(x) = 3x^2 - 20x - 1
## f(x) = Theta(g(x)) means:
### There exists constant c0, x0 for which c0g(x) >= f(x) for all x>x0
### There exists constant c1, x1 for which c1g(x) <= f(x) for all x>x1
## e.g. f(x) = Theta(x^2) because 4x^2 > 3x^2 -20x - 1 for all x >= 0 (c0 = 4, x0 = 0)
##                                2x^2 < 3x^2 -20x - 1 for all x >= 21 (c1 = 2, x1 = 20.04)

# Big O Vs Big Theta
## In practice, Theta bounds are preferred, because they are "tight"
## e.g. f(x) = 3x^2 - 20x - 1
## f(x) = O(x^2) = O(x^3) = O(2^x) and anything higher order because they all upper bound it
## f(x) = theta(x^2) but theta(x^3) != thata(2^x) and anything higher order because they upperbound but now lower bound it

# Simplification examples
## thata(n^2): "n^2" + 2n + 2 only focusing on the largest share in the large number
## theta(x^2): "3x^2" + 100000x + 3^1000
## theta(a): log(a) + a + 4

# Using theta to evaluate your algorithm
def fact_iter(n):
    """
    assume n an int >= 0
    """
    answer = 1 # 1
    while n>1: # 1
        answer *= n # 2
        n -= 1 # 2
    return answer

# Number of steps : 5n + 2
# Worst case asymptotic complexity:
## ignore additive constants: 2 doesn't matter when n is big
## ignore multiplicative constants: 5 doesn't matter if just want to know how increasing n changes time needed

# Combining complexity classes loop in series
## analyze statements inside functions to get order of growth
## Apply some rules, focus on dominant term
## Law of addition for thata():
### Used with sequential  statement
### theta(f(n)) + theta(g(n)) = theta(f(n) + g(n))
## e.g.
# for i in range(n):
#     print('a')
# for j in range(n*n):
#     print('b')
## is theta(n) + theta(n*n) = theta(n+n^2) = theta(n^2) because of dominant n^2 term
## Law of multiplication for theat():
### Used with nested statements/loops
### theta(f(n))*theta(g(n)) = theta(f(n)*g(n))
## e.g.
for i in range(n): #theta(n)
    for j in range(n//2): # theta(n) for outer loop iteration
        print('a')
## theta(n)xtheta(n) = theta(nxn) = theta(n^2)

# Analyse complexity
## What is the theta complexity of this program?
def f(x):
    answer = 1 #theta(1)
    for i in range(x): # outer loop is theta(x)
        for j in range(i,x): # Inner loop is theta(x)
            answer += 2
    return answer #theta(1)

# Complexity classes
## theta(1) denotes constant running time
## theta(log n) denotes logarithmic running time
## theta(n) denotes linear running time
## theta(nlogn) denotes log-linear running time
## theta(n^c) denotes polynomial running time
## theta(c^n) denotes exponential running time ( c is a constant raised to a power based on input size)