#Iteration
## While loop: Loop until the conditions set become false
where = input("You're in the lost forest, Go left of right? ")
while where == "right":
    where = input("You're in the lost forest, Go left of right? ")
print("You get out of the lost forest!")

n = int(input("Enter a non-negative integer: "))
while n > 0:
    print('x')
    n = n-1 # if there is nothing making the coditions false, the while loop works forever

trial = 0
where = input("Go left of right? ")
while where == "right":
    trial = trial + 1
    if trial > 2:
        print(':(')
    where = input("Go left of right? ")
print("You get out!")

### Calculating factorial
x = 4
i = 1
factorial = 1
while i <= x:
    factorial *= i # same as factorial = factorial * i
    i += 1 # same as i = i + 1
print (f'{x} factorial is {factorial}')

## for loop
for n in range(5): # the default starting point is 0, the endpoint is the number of loop done
    print(n)

for n in range(3,5):
    print(n)

for n in range(3, 10, 2):
    print(n)

mynum = 0
for i in range(10):
    mynum += 1
print(mynum)

mysum = 0
start = 1
end = 5
for i in range(start, end):
    mysum += 1
print(mysum)

### Factorial with for loop
y = 4
j = 1
factorial2= 1
for j in range(1, y+1, 1):
    factorial2 *= j
print(f'{y} factorial is {factorial2}')