# Recursion
# Multiplecation - Another Iterative solution
def mult(a,b):
    return a*b #general multiplication

def mult2(a,b):
    total = 0
    for n in range(b):
        total += a # think a*b into a+a+...+a b times
    return total

def mult3(a,b):
    result = 0
    while b>0: # control the number of iteration
        result += a
        b -= 1
    return result

# recursive step
## if b!=1, a*b = a + a*(b-1_
# Base case
## If b = 1, a*b = a

def mult_recur(a,b):
    if b == 1: # base case
        return a
    else: # recursive step
        return a + mult_recur(a,b-1)

print(mult_recur(4,5))

# big idea: earlier function calls are waiting on results before completing

# What is recursion
## Algorithmically: a way to design solutions to problems by divide-and-conquer or decrease-and-conquer
### Reduce a problem to a simpler versions of the same problem or to problem that can be solved directly

## Semantically: a programming technique where a function calls itself
### In programming, goal is to not have infinite recursion
### Must have 1 or more base cases that are easy to solve directly
### Must solve the same problem on some other input with the goal of simplifying the larger input problem, ending at base case

def power_recur(n,p):
    """
    :param n: a number
    :param p: an integer want to implement
    :return: n**p
    """
    assert type(p) == int, "p is not an integer"
    if p == 0:
        return 1
    elif p > 0:
        return n*power_recur(n,p-1)
    elif p < 0:
        return (1/n)*power_recur(n,p+1)

print(power_recur(-5,-1))

# Other example: Factorial
def fact(n): # Much pythonic
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))

# Big Idea: In recursion, each function call is completely separate
## separate scope/environments
## Separate variable names
## Fully independent

def fact_iter(n):
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

