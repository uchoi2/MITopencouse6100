# Lists and Mutability (Fixed)
L = [1, 2, 3, 4, 5]
L[3] = 10 # Changable of each element in the list
print(L)

# Operation on lists
## list.append(element) is a function for list to append element at the end of the list
L.append(6)
print(L)
L = L.append(7) # This returns none even though .append mutates L but .append itself mutate L and return new L


L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
L3.append(L4) #Append add L4 as an element so that L3[1] is ['re', 'mi']
L = L1.append(L3) # Not defined so that None because .append define a new variable. So L1 changes but L become None

# Meaning of dot
## Lists are python Object
## Objects have data
## Object types also have associated operations
## Access this information by object_name.do_something()
## Equivalent to calling append with arguemnts L and 5

def make_ordered_list(n):
    """
    n is a positive int
    returns a list containing all ints in order
    from 0 to n (inclusive)
    """
    mylist = []
    for i in range(0,n+1):
        mylist.append(i)
    return mylist

def remove_elem(L, e):
    """
    L is a list
    Returns a new list with elements in the same order as L
    but without any elements equal to e
    """
    newlist = []
    for i in L:
        # i is 1 then 2 then 2 then 2
        print(i)
        if i != e: #in cannot use for integer
            newlist.append(i)
    return newlist
L = [1,2,2,2]
print(remove_elem(L,2)) #pirnts [1]

# Strings to Lists
## String can be converted to the list by list(s
## string.split() splits a string on a character parameters, if no param, then splits on spaces
s = "I<3 cs &u"
L = list(s)
s.split()
ss = s.split() # Split s into 3 part I<3 cs &u: ' ' excluded
sss = s.split('<') # Split s into two part 'I' '3 cs &u': < excluded

## 'something'.join(list) to turn a list of strings into a bigger string
## something inside '' is filled between the elements
## Join by using ''
L = ['a', 'b', 'c']
A = ''.join(L)
B = '_'.join(L)
C = ' '.join(L)
D = ''.join(['a','b','c'])
# E = ''.join([a,b,c]) # Make an error because a,b,c is undefined

def count_words(sen):
    """
    :param sen: is a string representing a sentence
    :return: how many words are in s
    words is a sequence of characters between spaces
    """
    words = sen.split(' ')
    return len(words)
print(count_words("Hello it's me"))

# other list operators
## .sort .reverse .sorted(not mutation)
L = [4, 2, 7]
L.sort() # Ascending order

L = [4, 2, 7]
L.reverse() # Reverse the order of the list

L = [4, 2, 7]
L_new = sorted(L) # Ascending sorting but not mutate the L

# Application
def sort_words(sen):
    """
    :param sen: is a string representing a sentence
    :return: a list containing all words in sen but sorted in alphabetical order
    """
    words = sen.split(' ')
    words.sort() # when we use .sort() on string, then sorting it alphabetical order
    return words

print(sort_words("loot at this photograph"))

# Lists support Iteration
## Square every element of the list

# def square_list(L):
#     for elem in L:
#         # ?? How to do L[Index] = the square
#         # ?? elem is an element in L, not the index

#Solutions
## Option 1: Make a new variable representing the index
## Option 2: Loop over the index not the element and use L[index]
## Option 3: Use enumerate in the for loop (i.e. for i,e in enumerate(L))

# Example
def square_list(L):
    for i in range(len(L)):
        L[i] = L[i]**2
    squared_L = L
    return squared_L

# Mutation of Lists
## e.g. 1 A loop iterates over indices of L and mutates L each time (adds more element)
L = [1, 2, 3, 4]
for i in range(len(L)):
    L.append(i)
    print(L)
## e.g. 2 A loop iterates over L's elements directly and mutates L each time (adds more element)
L = [1, 2, 3, 4]
i = 0
for e in L:
    L.append(i) # L is mutated each iteration so that loop over list run infinitely
    i += 1
    print(L)

# Combining Lists
L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2 # Concatenation, +
print(L3)
L1.extend([0,6]) # L1 is mutated and works as L1 = L1 + [0,6]
L2.extend([[1,2], [3,4]]) #L2 is mutated and works as L2 = L2 + [[1,2],[3,4]]

## e.g. 3 A loop iterates over L's elements directly but reassigns L to a new object each time
L = [1,2,3,4]
for e in L:
    L = L+L # This also will run infinitely
    print(L)

# Empty out a list and checking that it's the same object by list.clear()
# Checking the same object in memory by using id()
## Case 1
L = [4,5,6]
id(L) # showing the set id of the object in the memory
L.append(8)
id(L)
L.clear()
id(L)

## Case 2
L = [4,5,6]
id(L)
L.append(8)
id(L)
L = []
id(L) # id changes because L is redefined
## e.g. 4 A loop iterates over L's elements directly and mutates L by removing element