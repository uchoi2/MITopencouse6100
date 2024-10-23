# Floats and Approximation method
##
x = 0.625 # 5*2**-3
p = 0
while ((2**p)*x)%1 !=0: #
    print(f'Remainder = {str((2**p)*x - int((2**p)*x))}') # Because p starts at 0
    p += 1
num = int(x*(2**p))
print(num)
result = ''
if num == 0:
    result = '0' # This is the two possible cases that x*2**p is equal to 0 (the other is p = -infy)
while num > 0 : # Transfroming to the binary
    result = str(num%2) + result
    num = num//2
print(result)
for i in range(p - len(result)):
    result = '0' + result
print(result)

result = result[0:-p] + '.' + result[-p:]
print('The binary representation of the decimal ' + str(x) + ' is ' +  str(result))

## Warning for the comparison of float variables
x = 0
for i in range(10):
    x += 0.125
print(x == 1.25)

x = 0
for i in range(10):
    x += 0.1
    print(x) #Floating number problem occurs because in binary 0.1 has infinity
print(x == 1)

## Approximation
x = 4
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

while abs(guess**2 - x) >= epsilon:
    guess += increment
    num_guesses += 1

print(f'num_guesses = {num_guesses}')
print(f'{guess} is close to square root of {x}')

## Approximation2: Overshooting the epsilon
x = 54321
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

while abs(guess**2 - x) >= epsilon:
    guess += increment
    num_guesses += 1
    if num_guesses%100000 == 0:
        print(f'Current guess = {guess}')
        print(f'Current guess**2 - x = {abs(guess*guess - x)}')
print(f'num_guesses = {num_guesses}')
print(f'{guess} is close to square root of {x}')

## Approximation3: Fixing the overshooting
x = 54321
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

while abs(guess**2 - x) >= epsilon and guess**2 < x:
    guess += increment
    num_guesses += 1
    if num_guesses%100000 == 0:
        print(f'Current guess = {guess}')
        print(f'Current guess**2 - x = {abs(guess*guess - x)}')
if abs(guess**2 - x) >= epsilon:
    print(f'Failed on square root of {x}')
else:
    print(f'{guess} is close to square root of {x}')