# Bisection Search
x = 54321
epsilon = 0.01
num_guesses = 0
low = 0
high = x
guess = (high + low)/2.0
while abs(guess**2 - x) >= epsilon :
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print(f'num_guesses = {num_guesses}')
print(f'{guess} is close to square root of {x}')

# Bisection search x in (0,1)
x = 0.5
epsilon = 0.01
num_guesses = 0
if x >= 1:
    low = 1.0
    high = x
else:
    low = x
    high = 1.0
guess = (high+low)/2.0
while abs(guess**2 - x) >= epsilon :
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print(f'num_guesses = {num_guesses}')
print(f'{guess} is close to square root of {x}')

# Bisection search for cube root
cube = -0.027
epsilon = 0.01
if cube >= 1:
    high = cube
    low = 1
elif cube <1 and cube >=0:
    high = 1
    low = cube
elif cube <0 and cube > -1:
    high = cube
    low = -1
else:
    high = -1
    low = cube
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print(f'num_guesses = {num_guesses}')
print(f'{guess} is close to square root of {cube}')

# Newton-Raphson Root Finder
## When p(x) = a_n*x**n + a_n-1*x**n-1 + ... + a_1x + a_0
## Newton and Rapson show that if g is an approximation to the root, then g - p(g)/p'(g) to the sqrt(g)
## Try to find out sqrt(24) then find out the squar root of x^2 -24
epsilon = 0.01
k = 9.0
guess = k/2.0
num_guesses = 0
while abs(guess**2 - k) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess**2) - k)/(2*guess))
print(f'num_guesses = {str(num_guesses)}')
print(f'Square root of {str(k)} is about {str(guess)}')
