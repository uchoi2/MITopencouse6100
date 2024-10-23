#Lambda Functions, Tuples, and Lists
## Lambda function: Using when we don't want to name the function
def is_even(x):
    return x % 2 == 0

lambda  x: x%2 == 0

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

def is_5(x):
    return x == 5

# Exactly same result
print(f'apply with is_5: {apply(is_5, 10)}')
print(f'apply with anon fcn: {apply(lambda x: x == 5, 10)}')

is_even(8)
(lambda x: x%2 == 0)(8)

def do_twice(n, fn):
    return fn(fn(n))

print(do_twice(3, lambda x: x**2)) # First run fn(fn(3)) and fn is defined as x**2

# Tufle
## Compound data types
### indexed sequences of elements, which could themselves be compound structure
#### tuples - immutable / list - mutable
### Mutability, aliasing, cloning

te = () # Empty tufle
ts = (2, ) # Each element is immutable
print(te)
print(ts)

t = (2, "mit", 3)
print(t[0])
print(t[1])
print(t[2])
s = (4, 5)
print(t+s) # + just add the tufle next to the former
len(t) # The number of element in the tufle
max((3,5,0)) # return the maximum value among the element in the tufle

seq = (2, 'a', 4, (1,2)) # Can define tufle with a tufle element
print(len(seq)) # 4 because the outer tufle has 4 elements
print(seq[3]) # (1,2)
print(seq[-1]) # (1,2)
print(seq[3][0]) # The first element of the fourth element of seq
print(len(seq[3]))

print(seq[1])
print(seq[-2:])
print(seq[1:4:1])
print(seq[:-1]) #From the first to the element before the last
print(seq[1:3])

for e in seq:
    print(e)

#Tufle is used to return more than one value from a function
def quotient_and_reminder(x,y):
    q = x//y
    r = x%y
    return (q, r)

both = quotient_and_reminder(10, 3)
(quot, rem) = quotient_and_reminder(5,2) # Separately defining the variable
print(f'quotient is {quot}')
print(f'remainder is {rem}')

# Application
def char_counts(s):
    """
    s is a string of lowercase chars
    returns a tuple where the first element is the number of
    vowels in s and the second element is the number of consonants in s
    """
    vowels = 'aeiou'
    v = 0
    c = 0
    for char in s:
        # char is 'a' then 'b' then 'c' then ..
        if char in vowels: # vowels count
            v += 1
        else: # cons count
            c += 1
    return(c,v)

print(char_counts('vocabulary'))

# Variable number of arguments
## * make function set arbitrary number of variables
def mean(*args):
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)
## numbers is bound to a tuple of the supplied values
print(mean(1,2,3,4,5,6)) # args = a tufle of (1,2,3,4,5,6)

def mean2(args):
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)
print(mean2((1,2,3,4,5,6))) # because of no *, we manually set up a tufle to get a result

# Lists
## Indexable ordered sequence of objects
### Usually homogeneous ( all integers, all strings, all list) but can contain mixed tipe
## Denoted by square brackets []
## Mutable
a_list = [] # empty list
L = [2, 'a', 4, [1,2]]
[1,2] + [3,4] # [1,2,3,4]
len(L) # 4
L[0] # 2
L[2] + 1 # 5
L[3] # [1,2]
max([3,5,0]) # 5

total = 0
L = [1,2,3,4,5]
for i in range(len(L)):
    total += L[i]
print(total)

total = 0
for i in L: # Interating over list directly
    total += i
print(total)

# Add the length of elements of a list
def len_sum(L):
    total = 0
    for s in L:
        total += len(s)
    return(total)
len_sum(['ab', 'abc', 'efg'])