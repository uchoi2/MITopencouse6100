#String, Input/Output, Branching

#String
## Defining String Variable
a = "me"
type(a)
b = 'you'
type(b)

## Operation of string variables
c = 'myself'
d = a + b
print(d)
e = a + ' ' + b + ' ' + c
print(e)
multiple = a*3
print(multiple)
multiple2 = (a + ' ')*3
print(multiple2)

## Orders and length of variables / Slicing the specific units in the string
state = 'I am a doctor in Georgia'
len(state)
state[0] # The order of the first unit of string is 0 : I
state[1] # Second unit : ' '
state[-1] # The last unit of state : a
state[-2] # The second last unit of state : i

state[0 : len(state) : 3] # string[starting point: End Point(Not included) : Interval]
                          # 0 Default for the starting point, 1 default for the interval
state[:]
state[: : -1] # Starting from the last to the first
state[len(state) - 1 : 4 : -2]

## Input Output
text = input("Type anything : ") # The returns of input function are always string
print(5*text)

### Application
text = input("Type a number : ") # return string of the number
print(5*text)
ex = int(input("Type a number: "))
print(5*ex)

#Algorithm
## Newton's Methond: f(g,x) = g**3 - x = 0 / next_guess = guess - f(guess)/f'(guess)
x = int(input('What x to find the cube root of ? '))
g = int(input('What guess to start with? '))
print('current estimate cubed = ', g**3)
next_g = g - ((g**3-x)/(3*g**2))
print('Next guess to try = ', next_g)

#F-Strings
num = 300
fraction = 1/3
print(num*fraction, 'is', fraction*100, '% of', num)
print(num*fraction, 'is', str(fraction*100) + ' % of', num)
print(f'{num*fraction} is {fraction*100} % of {num}') #in f string, command inside {} works as function or operator

#Comparision operators: This returns boolen - true or false
i = 5
j = 3
i > j # i is larger than j
i >= j # i is larger than or equal to j
i < j # i is smaller than j
i <= j # i is smaller than or equal to j
i == j # i is exactly equal to j
i != j # i is not equal to j

## and or not will return True or False
(3 > 2) and (4 > 3) # 'and' adds additional arguments to check and returns true when all conditions are true, otherwise false
not (2<3) # 'not' will return true when the inverse of conditions inside the parenthesis are true
not (3<2 and 4<3)
(3>2) or (4<3) # 'or' will return true when one of the conditions connected with 'or' is true
not (3<2 or 3<4)

## Example
secret = 5
guess = int(input('Please guess a number: '))
equal = (guess == secret)
print(equal)

# Branching: if statement
pset_time = int(input('How long do you work in hours? '))
sleep_time = int(input('How long do you sleep a day in hours? '))
if (pset_time + sleep_time) > 24:
    print("impossible")
elif (pset_time + sleep_time) == 24:
    print("full schedule!")
else:
    leftover = abs(24-pset_time-sleep_time) #abs meas absolute values
    print(f'{leftover} hours of freetime!')
print("end of day")

alpha = float(input("Enter a number for alpha: "))
beta = float(input("Enter a number for beta: "))
if alpha == beta:
    print("alpha and beta are equal")
    if beta != 0:
        print(f'therefore, alpha / beta is {alpha/beta}')
elif alpha < beta:
    print('alpha is smaller')
else:
    print('beta is smaller')
print('thanks!')

real_value = 5
guess = int(input('Please guess a number: '))
if guess >= real_value:
    print('too high')
elif guess == real_value:
    print('equal')
else:
    print('too low')
