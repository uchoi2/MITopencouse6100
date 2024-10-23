# Loops over strings, Guess-and-Check, and Binary
## Misuse of break command
mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break # This 'break' stop for-looping
        mysum += 1 # This command is not working
print(mysum) # Output = 5

## Eg) Counting even number within the given range
even_nums = 0
for i in range(5):
    if i%2 == 0: #i%2 returns the remainder of i divided by 2
        even_nums += 1
print(even_nums) #includes 0, 2, 4 so that total 3

## Looping on strings
### All loops below return same results
s = "demo loops - fruit loops"
#### Loop through index of strings
for index in range(len(s)):
    if s[index] == 'i' or s[index] == 'u':
        print('There is an i or u')
#### Loop directly through characters
for char in s:
    if char == 'i' or char == 'u':
        print('There is an i or u')
####
for char in s:
    if char in 'iu': # in command set the range of the strings so that same as i or u
        print('There is an i or u')

### e.g. digital cheerleaders
an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Enter a word: ")
times = int(input("Enthusiasm level (1-10): "))

for c in word:
    if c in an_letters:
        print(f'Give me an {c}: {c}')
    else:
        print(f'Give me a {c}: {c}')
print("What's that spell?")
for i in range(times):
    print(f'{word} !!!')

### e.g. count the number of different characters used in the string
s = 'abca'
seen = ''
count = 0
for char in s:
    if char not in seen:
        seen = seen + char
        count += 1
    # else: # Truly not necessary part
    #     pass
print(count)
print(seen)

## Guess-and-Check
### Square_root1
guess = 0
x = int(input("Enter and integer: "))
while guess**2 < x:
    guess = guess + 1
if guess**2 == x:
    print(f'Square root of {x} is {guess}')
else:
    print(f'{x} is not a perfect square')

### Square root2
guess = 0
neg_flag = False
x = int(input("Enter a positive integer: "))
if x < 0 :
    neg_flag = True
while guess**2 < x :
    guess = guess + 1
if guess**2 == x :
    print(f'Square root of {x} is {guess}')
else:
    print(f'{x} is not a perfect square')
    if neg_flag == True:
        print(f'Just checking... did you mean {-x} ?')

### Search and break the code if we find
secret = int(input("Enter a positive integer between 1 and 10: "))
for i in range(1,11,1):
    if i == secret:
        print('found')
        break
    else:
        print('not found')

secret = int(input("Enter a positive integer between 1 and 10: "))
found = False
for i in range(1,11,1):
    if i == secret:
        print("Yes, it's", i)
        found = True
if not found: # if the boolen of found changes to True, then not found is false so that print not work
    print("not found")

### Guess and check cube root
#### Positive cubes
cube = int(input("Enter an integer: "))
for guess in range(cube + 1): # To include when cube = 1
    if guess**3 == cube:
        print(f'Cube root of {cube} is {guess}')
#### Negative cubes
cube = int(input("Enter an integer: "))
for guess in range(cube + 1):
    if guess**3 == abs(cube):
        if cube < 0:
            guess = -guess
        print(f'Cube root of {str(cube)} is {str(guess)}')
#### Other cube root
cube= int(input("Enter an integer: "))
for guess in range(abs(cube) + 1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print(f'{cube} is not a perfect cube')
else:
    if cube < 0 :
        guess = -guess
    print(f'Cube root of {str(cube)} is {str(guess)}')

### Guess-and-Check with word problems
#### Small number
for alyssa in range(11):
    for ben in range(11):
        for cindy in range(11):
            total = (alyssa + ben + cindy == 10) # return True or False
            two_less = (ben == alyssa -2)
            twice = (cindy == 2*alyssa)
            if total and two_less and twice: # Because all are boolen
                print(f'Alyssa sold {alyssa} tickets')
                print(f'Ben sold {ben} tickets')
                print(f'Cindy sold {cindy} tickets')
#### Large number
for alyssa in range(1001):
    for ben in range(1001):
        for cindy in range(1001):
            ben = max(alyssa - 20, 0) # Direct calculation
            cindy = alyssa * 2 # Direct Calculation
            if ben + cindy + alyssa == 1000: # Because all are boolen
                print(f'Alyssa sold {alyssa} tickets')
                print(f'Ben sold {ben} tickets')
                print(f'Cindy sold {cindy} tickets')

## Comparision of float
x = 0
for x in range(10):
    x += 0.1 # same as x + 0.1 so that x = 0+0.1 -> 1+0.1 -> 2+0.1
print(x)
print (x == 1) # Return false

## Binary transformation algorithm
### e.g 1507 = 1*10**3 + 5*10**2 + 0*10**1 + 7*10**0 = 1507_10
### e.g.1507 = 1*2**10 + 1*2**8 + 1*2**7 + 1*2**6 + 1*2**5 + 1*2**1 + 1*2**0 -> 10111100011_2
num = int(input('Enter an integer: '))
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result # For 8 -> 1*2**3 + 0*2**2 + 0*2**1 + 0*2**0: 0 -> 00 -> 000 -> 1000
    num = num//2 # Only Extracting the integer e.g. 3 = 1*2**1 + 1*2**0 3/2 = 1.5 -> 1*2**0
    print(num)
print(result)
