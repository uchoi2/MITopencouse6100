#Functions as Object
def triangular(n):
    """ n is an int > 0
        Returns True if n is triangular, i.e. equals a continued
        summation of natural numbers (1+2+3+...+k), False otherwise"""
    total = 0
    for i in range(n):
        total += i
    if total == n:
        return True
    else:
        return False
print(triangular(4))

def bisection_root(x, e = 0.01):
    """ x is a float larger than 0 and
        e is a degree of approximation, epsilon. The default of e is 0.01
        Returns approximated square root of x"""
    epsilon = e
    low = 0
    high = x
    ans = (high + low) / 2
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    #print(f'{ans} is close to the root of {x}')
    return ans
print(bisection_root(5))
bisection_root.__doc__

def count_nums_with_sqrt_close_to(n, k, epsilon = 0.01):
    """ n is an integer > 2
        the function check the integer between 0 and k > 0
        epsilon is a positive number; default is 0.01
        Returns how many integers have a square root within epsilon of n"""
    count = 0
    for i in range(k+1):
        sqrt = bisection_root(i)
        if abs(n - sqrt) < epsilon:
            print(f'A square root of {i} is close to {sqrt} and within {n - epsilon} and {n + epsilon}' )
            count += 1
    return count
print(count_nums_with_sqrt_close_to(10, 500, 1))

# Decomposition
def sum_odds(a,b):
    sum_of_odds = 0
    for i in range(a, b+1):
        if i%2 == 1:
            sum_of_odds += i
    return sum_of_odds
low = 2
high = 7
print(sum_odds(low, high))

# Global Environment -> Applying globally within python workplace
# Function generate new environment so that it works only within the environment
def f(x): # x in this definition only works within the function environment
    x = x+1
    print(f'in f(x): x = {x}')
    return x

x = 3
z = f(x)
print(z)

# Inside a function, can access a variable defined outside
# Inside a function,  cannot modify a variable defined outside

def f(y):
    x = 1
    x += 1
    print(x)

def g(y):
    print(x)
    print(x+1)
def h(y):
    x += 1
x = 5
print(f(x)) # x inside the function is a different object from x=5
print(g(x)) # x inside the function is just a printing the x outside the function
print(h(x)) # Inside the h, it cannot access to the global variable x.

# Function as a parameter
def calc(op, x, y):
    return op(x, y) #op is a function

def add(a,b):
    return a+b

def div(a,b):
    if b!=0:
        return a/b
    print("Denominator was 0.")

print(calc(add, 2, 3)) # Function add is working because return add(x, y)
print(calc(div, 2, 3)) # Function div is working because return div(x, y)

# Function as a parameter 2
def func_a():
    print('inside func_a')

def func_b(y):
    print('inside func_b')
    return y

def func_c(f,z):
    print('inside func_c')
    return f(z)
print(func_a())
print(5+func_b(2))
print(func_c(func_b, 3))

# Application
def apply(criteria, n):
    """
    * Criteria is a func that takes in a number and returns a bool
    * n is an integer
    Return how many ints from 0 to n (inclusive) match the criteria
    """
    count = 0
    for i in range(n + 1):
        if criteria(i):
            count += 1
    return count
def rule(x):
    if x == 0:
        return False
    elif x > 0:
        return x%2 == 0
print(apply(rule, 10))
