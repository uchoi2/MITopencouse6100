# List Comprehension, Functions as Objects, Testing, and Debugging (Fixed)
# List Comprehension
## Applying a function to every element of a sequence, then creating a new list with
## - therse values is a common concept
### e.g.
def f(L):
    Lnew = [] # new list
    for e in L:
        Lnew.append(e**2) # Function to apply
    return Lnew
## Python provides a concise one-liner way to do dis, called a list comprehention
### Creates new list
### Applies a function to every element of another iterable
### Optional, only apply to elements that satisfy a test
### [expression for elem in iterable if test]
## e.g.
Lnew = [e**2 for e in L] # Same as f(L)

def F(L): # F(L) is same as below
    Lnew = []
    for e in L:
        if e%2==0:
            Lnew.append(e**2)
    return Lnew
Lnew = [e**2 for e in L if e%2 == 0]

def f(expr, old_list, test = lambda x: True):
    """
    :param expr: function
    :param old_list: a list to be modified
    :param test: test criteria for the element: if the element is True
    :return:
    """
    new_list = []
    for e in old_list:
        if test(e):
            new_list.append(expr(e))
    return new_list

List = [len(x) in ['xy', 'abcd', 7, '4.0'] if type(x) == str]

# Functions default parameters
def bisection_root(x, epsilon = 0.01): # if we set = alpha, then that is the default value.
    """
    :param x: a positive real number want to find the root
    :param epsilon: a degree of precision, default is 0.01
    :return: a square root of x
    """
    low = 0
    high = x
    guess = (high + low) / 2
    while abs(guess**2 - x) >= epsilon:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2
    return guess

print(bisection_root(123))

# Calling a function
## Okay
bisection_root(123)
bisection_root(123,0.001)
bisection_root(x = 123, epsilon = 0.01)
bisection_root(epsilon = 0.01, x = 123)

## Wrong
bisection_root(epsilon = 0.001, 123) # give error

# Function returning function
def is_even(i):
    return i%2 == 0
my_func = is_even # Not a function call, just a name
a = is_even(3)
b = my_func(4) # This also works because my_func is connected with is_even (just alias)

def make_prod(a):
    def g(b):           # Function defined within another function
        return a * b
    return g # Not a function call

val = make_prod(2)(3)
print(val)

doubler = make_prod(2)
print(doubler) # returns the function g with a = 2
val = doubler(3) # select the parameter on g
print(val)

# Testing and Debugging
## Classes of Tests
### Unit Testing : Testing each function separately
### Regression Testing : Add test for bugs as I find them
#### Catch reintroduced errors that were previously fixed
### Integration Testing : Does overall program work? Tend to rush to do this

## Testing Approaches
### Intuition about natural boundaries to the problem
### If no natural partitions, might do random testing
### Black box testing: Explore paths through specification
### Glass box testing: Explore paths through code

## Black box testing
### Designed without looking at the code
### Can be done by someone other than the implementer to avoid some implementer biases
### Testing can be reused if implementation changes
### Paths through specification
#### Build test cases in different natural space partitions
#### Also consider boundary conditions
def sqrt(x, eps):
    """
    Assume x, eps floats, x >= 0, eps >0
    :param x: floats, positive number
    :param eps: floats number larger than 0
    :return: res such that x-eps <= res*res <= x+eps
    """

## Glass Box Testing
### Use code directly to guide design of test cases
### Called path-complete if every potential path through code is tested at least once
### What are some drawbacks of this type of testing?
#### Can go through loops arbitrary many times
#### Missing paths
### Guidelines
#### Branches
#### For loops
#### While loops

def abs(x):
    """
    Assumes x is an int
    :param x: an integer
    :return: x if x>- 0 and -x otherwise
    """
    if x<-1: # x = -1 incorrectly returns -1 -> boundary case testing
        return -x
    else:
        return x

## Debugging
### Once you have discovered that your code does not run properly
#### Isolate the bugs
#### Eradicate the bugs: 근절하다
#### Retest until code runs correctly for all cases
#### Steep learning curve
### Tools
#### Built in to IDLE and Anaconda
#### Python Tutor
#### print statement

def is_pal(x):
    """
    :param x: a string
    :return: if x is a palindrome then true, otherwise false
    """
    # temp = x
    # print(f'before reverse: {temp}')
    # temp.reverse
    # print(f'after revers: {temp}')
    temp = []
    for e in x:
        temp.append(e)
    temp.reverse
    counter = ''.join(temp)
    if counter == x:
        return True
    else:
        return False
print(is_pal("abcba")) # input should be changed to the list