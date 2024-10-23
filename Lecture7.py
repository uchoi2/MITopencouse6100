# Decomposition, Abstraction, and Functions
def is_even(i):
    """Assumes: i, a positive integer
    Returns True if i is even, otherwise False""" # This is a docstring
    if i%2 == 0:
        return True
    else:
        return False

print(is_even(2))
is_even.__doc__ # The docstring becomes a component of the function

# More detailes
def is_even2(i):
    """Assumes: i, a positive integer
       Returns True if i is even, otherwise False"""
    return i%2 == 0
print(is_even2(3))
is_even2.__doc__

def div_by(n,d):
    """ n and d are ints > 0
        Returns True if d divides n evenly and False otherwise"""
    if n!=0 and d!=0:
        return n%d == 0
    else:
        if n == 0:
            print("Should set n > 0")
        if d == 0:
            print("Nothing can be divisible by d = 0")
        return "Reset n and d"

print(div_by(0,4))
div_by.__doc__

# Further application
for i in range(1,10):
    if is_even2(i):
        print(f'{i} is even')
    else:
        print(f'{i} is odd')

# e.g. Adding a number
def sum_loop_for(a,b):
    """ a and b are integers,
        returns sum of all odds within a and b including a and b"""
    sum_of_odds = 0
    for i in range(a,b+1):
        if i%2 !=0:
            sum_of_odds += i
        else:
            sum_of_odds += 0
    return sum_of_odds
print(sum_loop_for(0, 20))

def sum_loop_while(a,b):
    """ a and b are integers,
        returns sum of all odds within a and b including a and b"""
    sum_of_odds = 0
    i = a
    while i <= b:
        if i%2 !=0:
            sum_of_odds += i
        i += 1
    return sum_of_odds
print(sum_loop_while(0,20))