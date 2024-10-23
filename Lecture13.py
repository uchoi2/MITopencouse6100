# Exceptions and Assertions
## Hit unexpected conditions -> Error code
## e.g.
test = [1,7,4]
test[4] # Index Error (0,1,2,3) not 4
int(test) # type error
a # Name error
'a'/4 # Type error

# Handling exception
# try:
#     # do some potentially
#     # problematic code
# except:
#     # do something to
#     # handle the problem
## If expressions in try block all succeed
### Evaluation continues with code after except block
## Exceptions raised by any statement in body of try are handled by the except statement
### Execution continues with the body of the except statement
### Then other expressions after that bock of code

def sum_digits(s):
    """
    :param s: a non-empty string containing digits
    :return: sum of all chars that are digits
    """
    total = 0
    for char in s:
        if char in '0123456789':
            val = int(char)
            total += val
    return total
print(sum_digits('123abc'))

def sum_digits_except(s):
    """
    :param s: a non-empty string containing a digit
    :return: sum of all chars that are digits
    """
    total = 0
    for char in s:
        try:
            val = int(char) # if there is an error on here
            total += val
        except:
            print("can't convert", char) #  this command working
    return total
print(sum_digits_except('123abc'))

a = int(input("Tell me one number: "))
b = int(input("Tell me another number: "))
print(a/b)

def divide_num():
    try:
        a = int(input("Tell me one number: "))
        b = int(input("Tell me another number: "))
        print(a / b)
        return a/b
    except:
        print("Bug in user input.")

# Exception by types
try:
    a = int(input("Tell me one number: "))
    b = int(input("Tell me another number: "))
    print(f'a/b = {a/b}')
    print(f'a+b = {a+b}')
except ValueError:
    print("Could not convert to a number.")
except ZeroDivisionError:
    print("Can't divide by Zero")
    print(f'a/b = infinity')
    print(f'a+b = {a+b}')
except:
    print("Something went very wrong")
else:
    print("Success")

# Other Blocks associated with a try bloc
# else:
#     # Body of this is executed when execution of associated try body completes with no exceptions
# finally:
#     # Body of this is always executed after try, else, and except clauses
#     # even if they raised another error or executed a break, continue, or return
#     # useful for clean-upcode that should be run no matter what else happened

# What to do when encounter an error
## Fail Silently
### Substitute default values or just continue but bad idea
## Return an error value
### What value to choose?
### Complicates code having to check for a special value
## Stop execution, signal error condition
### In Python, raise an exception
# raise ValueError("Something is wrong")

def sum_digits2(s):
    """
    :param s: a non-empty string containing digits
    :return: sum of all chars that are digits
    """
    total = 0
    for char in s:
        try:
            val = int(char)
            total += val
        except:
            # raise ValueError("string contained a character") # Halt the execution as soon as
                                                               # meet a character
            print("string contained a character")
    return total

print(sum_digits2("123abc"))

def pairwise_div(Lnum, Ldenom):
    """
    :param Lnum: non-empty lists having same length with Ldenom
    :param Ldenom: non-empty lists having same length with Lnum
    :return: a new list whose elements are the pairwise division of an element in Lnum by an
    element in Ldenom
    Raise a ValueError if Ldenom contains 0.
    """
    if len(Lnum) != len(Ldenom):
        return f'{Lnum} and {Ldenom} must have the same length'
    # list = []
    # for e in range(len(Lnum)):
    #     try:
    #         x = Lnum[e]
    #         y = Ldenom[e]
    #         val = x/y
    #         list.append(val)
    #     except:
    #         #raise ValueError("Can't divide by zero")
    #         print("Can't divide by zero")
    try:
        list = [Lnum[i]/Ldenom[i] for i in range(len(Lnum))] # if i use this then the second case not work well
    except:
        raise ValueError("Can't divide by zero")
    return list
L1 = [4,5,6]
L2 = [1,2,3]
print(pairwise_div(L1,L2))

L2 = [1,0,3]
print(pairwise_div(L1,L2))

# Assertions: Defensive Programming Tool
## Want to be sure that assumptions on state of computation are as expected
## Use an assert statement to raise an Assertion Error exception if assumptions not met
# assert <statement that should be true>m "message if not true"
## An example of good defensive programming
### Assertions don't allow a programmer to control response to unexpected conditions
### Ensure that execution halts whenever an expected condition is not met
### Typically used to check inputs to functions, but can be used anywhere
### Can be used to check outputs of a function to avoid propagating bad values ## propagate : 전파하다 보급하다
### Can make it easier to locate a source of a bug

def sum_digits3(s):
    """
    :param s: is a non-empty string containing digits
    :return: sum of all chars that are digits
    """
    assert len(s) !=0, "s is empty"
    nint = 0
    for char in s:
        try:
            temp = int(char)
            nint += 1
        except:
            pass
    assert nint !=0, "s has no digits"
    sum = 0
    for char in s:
        try:
            val = int(char)
            sum += val
        except:
            pass
    return sum

print(sum_digits3("abc"))

def pairwise_div2(Lnum, Ldenom):
    """
    Assert: Lnum and Ldenom are non-empty lists of equal lengths
    :param Lnum: non-empty lists having same length with Ldenom
    :param Ldenom: non-empty lists having same length with Lnum
    :return: a new list whose elements are the pairwise division of an element in Lnum by an
    element in Ldenom
    Raise a ValueError if Ldenom contains 0
    """
    assert len(Lnum) !=0 and len(Ldenom) !=0, "Empty list"
    assert len(Lnum) == len(Ldenom), "length different"
    list = []
    for e in range(len(Lnum)):
        try:
            x = Lnum[e]
            y = Ldenom[e]
            val = x/y
            list.append(val)
        except:
            #raise ValueError("Can't divide by zero")
            print("Can't divide by zero")
    return list

## Further example
def get_stats(class_list):
    new_stats = []
    for stu in class_list:
        new_stats.append([stu[0], stu[1], avg(stu[1])])
    return new_stats
def avg(grades):
    try:
        avg = sum(grades)/len(grades)
        return avg
    except ZeroDivisionError:
        print("warning: no grades data")

list = [[['peter','parker'], [80.0, 70.0, 85.0]], [['bruce', 'wayne'],[100.0, 80.0, 74.0]], [['captain', 'america'], []]]
print(get_stats(list))

def avg2(grades):
    assert len(grades) !=0, "no grade data"
    return sum(grades)/len(grades)