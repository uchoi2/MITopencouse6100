#Recursion on Non-numerics
def fib(x): #Fibonacci recursive
    if x == 1 or x == 2:
        return 1
    else:
        return fib(x-1) + fib(x-2)


print(fib(6))

def fib_efficient(n, d): # Fibonacci with memorization
    if n in d: # loop over keys
        return d[n] # exclude the case of 1 and additional stored values so that decreases the number of function calls
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans # Storing the results
        return ans
d = {1:1, 2:1}
d[2] # [] inside the dictionary is key
print(fib_efficient(6, d))

def score_count(x):
    """
    :param x: an integer larger or equal to 1, total score
    :return: all the ways to make a score of x adding 1,2, and/or 3 together
    """
    if x == 1:
        return 1 # one ways to make it
    if x == 2:
        return 2 # two ways to make it
    if x == 3:
        return 3 # three ways to make it
    else:
        return score_count(x-1) + score_count(x-2) + score_count(x-3) # Think that the last score is 1 or 2 or 3

print(score_count(5))

# The list is naturally recursive
def total_recur(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + total_recur(L[1:])

L = [1,2,3,4,5,6]

def total_len_recur(L):
    if len(L) == 1:
        return len(L[0])
    else:
        return len(L[0]) + total_len_recur(L[1:])
test = ["ab", "abc", "efghi"]
print(total_len_recur(test))

# Another example: is an element in a list? (Careful with this implementation)
def in_list(L,e):
    if len(L) == 1:
        return L[0] == e
    else:
        return in_list(L[1:],e) # be careful because the base case is len(L) == 1, it only tests the statement whenever the len(L[1:]) reach to 1
test = [2,5,8,1]
print(in_list(test,1)) # this returns true
test2 = [2,1,5,8]
print(in_list(test2,1)) # But this returns false

def in_list2(L,e):
    if len(L) == 1:
        return L[0] == e
    else:
        if L[0] == e: # By adding this part, we can test every recursion.
            print(L[0])
            return True
        else:
            return in_list2(L[1:], e)
test2 = [2,1,5,8]
print(in_list2(test2,1)) # But this returns false

def in_list3(L,e):
    if len(L) == 0:
        return False
    elif L[0] == e: # Test the first element == e for all recursions
        return True
    else:
        return in_list3(L[1:],e) # if not pass, then move over the next recursion
test2 = [2,1,5,8]
print(in_list3(test2,1)) # But this returns false

# Big Idea: Each case(base cases, recursive step) must return the same type of object
## Remember that function returns build upon each other
## If the base case returns a bool and the recursive step returns an int, this gives a type mismatch error at runtime

# Flatten a List Containing Lists of ints
## e.g. [[1,2],[3,4],[9,8,7]] -> [1,2,3,4,9,8,7]
def flatten(L):
    if len(L) == 1:
        return L[0]
    else:
        return L[0] + flatten(L[1:]) # because L[0] is also the list

def in_list_of_lists(L,e):
    """
    :param L: is a list whose elements are lists containing ints
    :param e: an arbitrary integers
    :return: True if e is an element within the lists of L
    """
    # if len(L) == 0:
    #     return False
    # elif e in L[0]:
    #     return True
    # else:
    #     return in_list_of_lists(L[1:], e)
    if len(L) == 1:
        return e in L[0]
    else:
        first = L[0]
        if e in first:
            return True
        else:
            return in_list_of_lists(L[1:], e)

# reverse the list
def my_rev(L):
    if len(L) == 1:
        return L
    else:
        return my_rev(L[1:]) + [L[0]] # L[0] may not be a list [] make a list of one element

test = [1, 2, "abc"]
print(my_rev(test))

# revers all elements even in the list of lists
def deep_rev(L):
    if len(L) == 1:
        if type(L[0]) != list:
            return L
        else:
            return [deep_rev(L[0])] # Make a list of one element by []
    else:
        # if type(L[0]) != list:
        #     return deep_rev(L[1:]) + [L[0]]
        # else:
        #     return deep_rev(L[1:]) + [deep_rev(L[0])]
        return deep_rev(L[1:]) + [deep_rev(L[0])]
# Big Idea: Recursion procedure from this lecture can be applied to indexable ordered sequence
## Same Idea will work on problems involving strings or tuples