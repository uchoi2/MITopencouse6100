# Alising and Cloning
# Making a copy of list
L = [1,2,3,4]
Lcopy = L[:] # Return same as looping over L and appending each element to Lcopy
# Lcopy 2 = L # Return syntex error

def remove_all(L,e):
    """
    :param L: is a list
    :param e: Mutate L to remove all elements in L that are equal to e
    :return: None
    """
    # make a copy
    Lnew = L[:]
    L.clear()
    for i in Lnew:
        if e != i:
        L.append(i)

Lin = [1,2,2,2]
remove_all(Lin, 2)
print(Lin)


# Other operation on lists: Remove
## del(list(index)) delete element at a specific index
Lin = [1,2,2,2]
del(Lin[0]) # Mutate the list

## list.pop() remove element at the end of the list and returns the value, also specifies the index
Lin = [1,2,2,2]
Lin.pop() # delete the last element and return the removed element
Lin.pop(0) # delete the first element and return the removed element

## list.remove(element) Looks for the element and removes it (mutating the list)
## If element occurs multiple times, removes the first occurrence
## If element not in list, gives an error
L = [2,1,3,6,3,7,0]
L.remove(3) # remove the element 3 at the 3rd position

def remove_all(L, e):
    """
    :param L: is a list
    :param e: Mutate L to remove all elements in L that are equal to e
    :return: None
    """
    while e in L:
        L.remove(e)

def remove_all_for(L, e):
    """
    :param L: is a list
    :param e: Mutate L to remove all elements in L that are equal to e
    :return: None
    """
    for elem in L:
        if elem == e:
            L.remove(e) # After mutating, L changes to [1,2,2] and move on to the next element
            # Hence if L changes during for-loop, the order move over to the third element.
            # Because the loop already done the 2nd element of L before mutating

L = [1,2,2,2]
remove_all(L,2) # remove all e
print(L)

L = [1,2,2,2]
remove_all_for(L,2) # return [1,2]
print(L)

## Tricky example 4
### A loop iterates over L's elements directly and mutates L by removing element
def remove_dups_for(L1, L2):
    """
    :param L1: is a list to be mutated
    :param L2: is a list
    :purpose: remove elements of L1 that are also in L2
    :return: mutated L1 that exclude all elements in L2
    """
    for e in L1:
        if e in L2:
            L1.remove(e)

L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]

remove_dups_for(L1, L2) # return [20, 30, 40] because the first element removed, the second becomes the first
# in the case, L1 = [20, 30, 40] and L2 = [10, 20, 50, 60] and loop begins at 30 (the second element)

def remove_dups(L1,L2):
    """
    :param L1: is a list to be mutated
    :param L2: is a list
    :purpose: remove elements of L1 that are also in L2
    :return: mutated L1 that exclude all elements in L2
    """
    for e in L2:
        while e in L1:
            L1.remove(e)

L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]
remove_dups(L1, L2)

# Mutation and iteration with clone
def remove_dups_for_v2(L1,L2): # L1 and L2 in the definition is an alias of the lists we use for the function call
    L1_copy = L1[:]
    for e in L1_copy: # In this case, L1_copy not mutated so that it's going by order
        if e in L2:
            L1.remove(e) # Hence this works well

L1 = [10, 20, 30, 40]
L2 = [10, 20, 50, 60]
remove_dups_for_v2(L1, L2)
print(L1)

# Aliasing
## City may be known by many names
## Attributes of a city: small, tech-savvy
## All nicknames point to the same city
### Add new attribute to one nickname
## Idea : When you pass a list as a parameter to a function, you are making an alias
### The actual parameter (from the function call) is an alias for the former parameter (From the function definition)

old_list = [[1,2],[3,4],[5,'foo']]
new_list = old_list # this does not make clone, two are exactly same so change simultaneously
id(new_list)
id(old_list) # Same id between two variables
new_list[2][1] = 6

# Controling copying
import copy # copy tool
# copy creates a "new data structure", but "actual elements are shared"
old_list = [[1,2],[3,4],[5,6]]
new_list = copy.copy(old_list)
old_list.append([7,8]) # In this case, the original elements shared are not changing
print(f'old_list: {old_list}') # Only old_list append the new list
print(f'new_list: {new_list}')

old_list[1][1] = 9
print(f'old_list: {old_list}') # Shared element has been changed
print(f'new_list: {new_list}') # Hence the element also is changed in the new_list.

# List in Memory
## Separate the idea of the object versus the name we give an object
### A list is an object in memory
### Variable name points to object
## Lists are mutable and behave differently than immutable types
## Using equal sign between objects creat aliases (connected/only names are different)
### Both variables point to the same object in memory
### Any variable pointing to that object is affected by mutation of object, even if
### - mutation if by referencing another name
## If you want a copy, you explicitly tell Python to make a copy
## Key phrase to keep in mind when working with lists is side effects
## especially when dealing with aliases
## Use python tutor