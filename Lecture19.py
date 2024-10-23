# Inheritance
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None # setting name as attribute without parameter
    def __str__(self):
        return f'animal: {str(self.name)} : {str(self.age)}'
    def get_age(self): # getter
        return self.age
    def get_name(self): # getter
        return self.name
    def set_age(self, newage): # setter
        self.age = newage
    def set_name(self, newname=""): # setter / default as null string
        self.name = newname
a = Animal(6)
# print(a)
b = Animal(6)
# print(b)
# print(a.age)
# print(a.get_age())
a.set_name("fluffy")
print(a.name)
print(a.get_name())
print(a)

# Information hiding: https://ko.wikipedia.org/wiki/%EC%A0%95%EB%B3%B4_%EC%9D%80%EB%8B%89
## https://effectiveprogramming.tistory.com/entry/%EA%B0%9D%EC%B2%B4%EC%A7%80%ED%96%A5-%EC%A0%95%EB%B3%B4-%EC%9D%80%EB%8B%89information-hiding%EC%97%90-%EB%8C%80%ED%95%9C-%EC%98%AC%EB%B0%94%EB%A5%B8-%EC%9D%B4%ED%95%B4
## 한 코딩결정의 변화를 다른 부분으로 확대하지 않는 기술
## 두 객체 사이에 상호관계가 발생하지 않음 -> 두 객체가 완전히 분리되어 따로 놀음
## Author of class definition may change data attribute variable names
# class Animal(object):
#     def __int__(self, age):
#         self.years = age # self.age -> self.year
#     def get_age(self):
#         return self.years
## If you are accessing data attributes outside the class and class definition changes, may get errors
## Outside of class, use getters and setters instead
## Use a.get_age() Not a.age

# Python Not great at information hiding
## Allows you to access data from outside class definition: print(a.age)
## Allows you to write to data from outside class definition: a.age = 'infinite'
## Allows you to creat data attributes for an instance from outside class definition: a.size = "tiny"
## It's not good style to do any of thses!

def animal_dict(L):
    """
    :param L: is a list
    :return: a dict, d, mapping an int to an Animal object
    A key in d is all non-negative ints, n, in L. A value corresponding to
    a key is an Animal object with n as its age.
    """
    d = {}
    for n in L:
        if type(n) == int and n >= 0:
            d[n] = Animal(n)
    return d
L = [2,5,'a',-5,0]
animals = animal_dict(L)
for n,a in animals.items(): # n is a key and a is an items
    print(f'key {n} with val {a}')

# e.g.
def make_animals(L1,L2):
    """
    :param L1: is a list of ints
    :param L2: is a list of str
    :return: a list of Animals the same length as L1 and L2.
    An animal object at index i has the age and name
    corresponding to the same index in L1 and L2, respectively
    """
    assert len(L1) == len(L2), "lengths different"
    list = []
    for i in range(len(L1)):
        # list.append([L1[i],L2[i]])
        age = L1[i]
        name = L2[2]
        a = Animal(age)
        a.set_name(name)
        list.append(a)
    return list
L1 = [2,5,1]
L2 = ['bolbfish', 'crazyant', 'parafox']
animals = make_animals(L1,L2)
# print(animals)
for i in animals:
    print(i)

# Big Idea: Access data attributes(stuff defined by self.xxx) through methods - it's better style

# Hierarchies
## Parent class (superclass)
### Child class (subclass)
#### inherits all data and behaviors of parent class
#### Add more info
#### Add more behavior
#### Override behavior

# Inheritance: Subclass
class Cat(Animal): # inherits all attributes of Animal: __init()__ age, name get_age()...
    def speak(self):
        print("meow")
    def __str__(self):
        return f'cat: {str(self.name)} : {str(self.age)}'
## Add new funtionality with speak()
### Instance of type Cat can be called with new methods
### Instance of type Animal throws error if called with Cat's new method
## __init__ is not missing, uses the Animal version
c = Cat(5)
print(c)
c.set_name('fluffy')
print(c)

class Person(Animal): # subclass of animal
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends.copy()
    def add_friend(self):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print("hello")
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self): #Override Animal's __str__ method
        return f'person: {str(self.name)}: {str(self.age)}'
P1 = Person('Jack', 30)
P2 = Person('Jill', 25)

# try
def make_pets(d):
    """
    :param d: is a dict mapping a person obj to a cat ob
    :return: Prints, on each line, the name of a person, a colon, and the name of the person's cawt
    """
    for p,c in d.items():
        print(f'{p.get_name()}:{c.get_name()}')

p1 = Person("ana", 86)
p2 = Person("james", 7)
c1 = Cat(1)
c1.set_name("furball")
c2 = Cat(5)
c2.set_name("fluffsphere")
d = {p1:c1, p2:c2}
make_pets(d)
# Big Idea: A subclass can use a parent's attributes, override a parent's attributes, or define new attributes

import random

class Student(Person): # Inherits Person and Animal attributes
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age) # Person__init__ takes care of all initialization
        self.major = major
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print('I have homework')
        elif 0.25 <= r < 0.5:
            print('I need sleep')
        else:
            print("I'm still zooming")
    def __str__(self):
        return f'student:{str(self.name)}:{str(self.age)}:{str(self.major)}'

s1 = Student('alice', 20, 'CS')
s2 = Student('beth', 18)
s1.speak()

# Class variables and the Rabbit subclass
## Class variables and their values are shared b/w all instances of a class
class Rabbit(Animal):
    tag = 1 # class variable of Rabbit
    def __init__(self, age, parent1=None, parent2=None):
        Animal.__init__(self, age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag # Access shared class variable
        Rabbit.tag += 1 # Incrementing class variable changes it for all instances that may reference it
    # tag used to give unique id to each new rabbit instance
    def get_rid(self):
        return str(self.rid).zfill(5) # .zfill: Method on a string to pad the beginning with zeros e.g. 00001 not 1
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __add__(self, other):
        # returning object of same type as this class
        return Rabbit(0, self, other) # rabbit init is self, age, parent1, parent2 so that (age, parent1, parent2)
    def __eq__(self, other):
        # Compare two rabbits
        parent_same = (self.parent1.rid == other.parent1.rid and self.parent2.rid == other.parent2.rid)
        parent_opp = (self.parent2.rid == other.parent1.rid and self.parent1.rid == other.parent2.rid)
        return parent_same or parent_opp

r1 = Rabbit(8) # tag = 1
r1.rid
r2 = Rabbit(6) # tag = 2
r2.rid
r3 = Rabbit(10) # tag = 3
r3.rid
r4 = r1 + r2 # tag 4
r4.rid
r5 = r3 + r4
r6 = r4 + r3
print("r5 and r6 have same parents?", r5 == r6)
print("r4 and r6 have same parents?", r4 == r6)
