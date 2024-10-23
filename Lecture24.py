# Sorting Algorithm

# Searching a sorted list
## Using binary search, can search for an element in theta(log(n))
### Assumes the list is sorted!
## When does it make sense to sort first then search?
## Sort + \theta(log(n) < theta(n)
## Sort + k*theta(log(n)) < k*theta(n): Multiple search -> sorting become irrelavent

# BOGO/RANDOM/MONKEY sort
## Bogo sort (theta(n))
## To sort a deck in cards
### Throw them in the air, pick them um, are tehy sorted? -> repeat if not sorted

def is_sorted(L):
    i = 0
    j = len(L)
    while i + 1 < j:
        if L[i] > L[i+1]:
            return False
        i += 1
    return True
def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)0

## Bubble Sort
## Compare consecutive pairs of elements
## Swap elements in pare such that smaller is first
## When reach end of list, start over again
## Stop when no more swaps have been made
def bubble_sort(L):
    did_swap = True
    while did_swap: #theta(len(n))
        did_swap = False
        for j in range(1,len(L))): #theta(len(n))
            if L[j-1] > L[j]:
                did_swap = True
                L[j],L[j-1] = L[j-1],L[j]
    return None

## Selection Sort
## First step: Extract minimum element -> Swap it with element at index 0
## Second step: In remaining sublist, extract minimum element -> Swap it with the element at index1
## Keep the left portion of the list sorted
### At ith step, first i elements in list are sorted
### al other elements are bigger than first i elements
def selection_sort(L, detail = False): #theta(len(L)^2)
    for i in range(len(L)):
        for j in range(i, len(L)):
            if L[j] < L[i]:
                L[i], L[j] = L[j], L[i]
            if detail == True:
                print(L)

def selection_sort_var(L, detail = False):
    for i in range(len(L)):
        smallest = L[i]
        smallestj = i
        for j in range(i, len(L)):
            if L[j] < L[smallestj]:
                smallest = L[j]
                smallestj = j
            if detail == True:
                print(L)
        L[i], L[smallestj] = L[smallestj],L[i]
        print()

## Merge Sort
## Use a divide-and-conquer approach:
### If list of length 0 or 1, already sorted
### If list has more than one element, split into two lists, and sort each
### Merge sorted sublists
#### Look at first element of each, move smaller to end of the result
#### When one list empty, just copy rest of other list

def merge(left, right): #theta(len(left) + len(right)
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while (i < len(left)):
        result.append(left[i])
        i+=1
    while (j < len(right)):
        result.append(right[j])
        j+=1
    return result

## Full merge sort algorithm
def merge_sort(L): #complexity theta(nlogn)
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)