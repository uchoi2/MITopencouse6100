# Complexity Classes Examples
# Where does the function come from?
## Given code, start with the input parameters, What are they?

def f(L,L1,L2): # Only care about code that repeats w.r.t these variables
    inL1 = False # +1
    for i in range(len(L1)): # Multiplied by len(L1) +1 because of assigning i in range
        if L[i] == L1[i]: # +3 (if statement, L[i], L1[i])
            inL1 = True #  +1 so tottaly +5*len(L1)
    inL2 = False # +1
    for i in range(len(L2)): # Multiplied by len(L2) +1
        if L[i] == L2[i]: # +3
            inL2 = True # +1 So totally +5*len(L2)
    return inL1 and inL2 # +2 (return, and)
## Come up with the equation relating input to number of ops
### f = 1 + len(L1)*5 + 1 + len(L2)*5 + 2
### theta(f) = theta(10*len(L) + 4) = theta(len(L))

# Constant complexity
## Complexity independent of inputs
## Very few interesting algorithms in this class, but can often have pieces that fit his class
## Can have loops or recursive calls, but number of iterations or calls independent of size of input
## Some built-in operations to a language are constant
### L[i], L.append(), d[key]

# Linear Complexity
## simple iterative loop algorithms: loops must be a function of input
## Linear search a list to see if an element is present
## Recursive functions with one recursive call and constant overhead for call
## Some built-in operations
### e in L, L[:len(L)//2], L1 == L2, del(L[5])

# Big Idea: Be careful about what the inputs are
def fact_recur(n): #Theta n
    """assume n >= 0"""
    if n <= 1:
        return 1
    else:
        return n*fact_recur(n-1) #running n times -> theta(n)

## Complexity of iterative fibonacci
def fib_iter(n):
    if n == 0: # constant theta(1)
        return 0
    elif n == 1:
        return 1
    else:
        fib_i = 0 #theta(1)
        fib_ii = 1 #theta(1)
        for i in range(n-1): #theta(n)
            tmp = fib_i
            fib_i = fib_ii
            fib_ii = tmp + fib_ii
        return fib_ii #theta(1)

# Polynomila
## Most common polynomial algorithms are quadratic, i.e., complexity grows with square of size of input
## Commonly occurs when we have nested loops or recursive function calls
## example1
def g(n):
    """assume n >= 0"""
    x = 0
    for i in range(n):
        for j in range(n):
            x +=1
    return x

# Exponential complexity
def fib_recur(n):
    if n == 0: # theta(1)
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recur(n-1) + fib_recur(n-2)

def gen_subsets(L):
    if len(L) == 0:
        return [[]]
    extra = L[-1:]
    smaller = gen_subsets(L[:-1])
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new
# Overall complexity is theta(n*2**(n-1))