# Python Classes

# Object Oriented Programming
## Everything in Python is an object (has a type)
## Can Create new objects of some type
## Can maniplate objects
## Can destroy objects
### explicitly using del or just forget about them
### Python system will reclaim destroyed or inaccessible objects - garbage collecting

# What are objects
## Objects are a data abstraction
### An internal representation
### An interface for interacting with object

# Advantage of opp
## Bundle data into packages together with procedures that work on them through well-defined interfaces
## Divide-and-conquer development
### Implement and test behavior of each class separately
### Increased modularity reduces complexity
## Classes make it easy to reuse code
### Many Python modules define new classes
### Each class has a separate environment (no collision 충돌 on function names)
### Inheritance allows subclasses to redefine or extend a selected subset of superclass' behavior

# Big Idea: You write the class so you make the design decisions
## You decide what data represents the class
## You decide what operations a user can do with the class

# Creating and Using your own types with classes
## Make a distinction b/w creating a class and using an instance of class
## Creating the class involves
### defining the class name
### Defining class attributes
### e.g. someone wrote code to implement a list class
## Using the class involves
### Creating new instances of the class
### doing operations on the instances
### e.g. L=[1,2] and len(L)

# A parallel with functions
## Defining a class is like defining a function
### with functions, we tell Python this procedure exists
### with classes, we tell Python about a blueprint for this new data type
#### it's data attributes and procedural attributes
## Creating instances of objects is like calling the function
### With functions we make calls with different actual parameters
### with classes, we create new object instances in memory of this type
#### L1 = [1,2,3] L2 = [5,6,7]

# class Coordinate(object): # in parentheses: class parent
#     #define attribute here

# What are attributes?
## Data and procedures that "belong" to the class
## data attributes
### Think of data as other objects/variables that make up the class
### e.g. a coordinate is made up of two numbers
## Methods(procedural attributes)
### Think of methods as functions that only work with this class
### How to interact with the object
### e.g. you can define a distance between two coordinate objects but there is no meaning to a distance b/w two list objects

# Defining how to create an instance of a class
## First have to define how to creat an instance of class
## Use a special method called __init__ to initialize some data attributes or perform initialization operations
class Coordinate(object):
    def __init__(self, xval, yval): # parameter to refer to an instance of the class without having created one yet
        self.x = xval # two data attributes make up your type
        self.y = yval # every single object I make will have two attributes called x and y if I add self.
## self allows you to create variables that belong to this object
## w/o self, you are just creating regular variable

# What is self?
## Think of the class definition as a blueprint with placeholders for actual item
### self has a chair
### self has a coffee table
### self has a sofa
## Now when you create one instance (name it living_room), self becomes this actual object
### living_room has a blue chair
### living_room has a black table
### living_room has a white sofa
## can make many intances using the same blueprint

# Big Idea: When defining a class, we don't have an actual tangible object here
## It's only a definition
c = Coordinate(3,4) #type = Coordinate with x = 3 and y = 4
origin = Coordinate(0,0)
print(c.x) # this make Python access to the x attribute of c
print(origin.x)

# What is a method?
## Procedural attribute
### Think of it like a function that works only with this class
## Python always passes the object as the first argument
### Convention is to use self as the name of the first argument of all methods
class Coordinate(object):
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval
    def distance(self, other): # use slef to refer to the object I call this method on self
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    # Other than self and dot notation, methods behave just like functions (take params, do operations, return)

# How to call a method?
## The "." operator is used to access any attribute
### a data attribute of an object
### a method of an object

c = Coordinate(3,4) #type = Coordinate with x = 3 and y = 4
origin = Coordinate(0,0)
print(c.distance(origin)) # call the method attributes on c with parameter origin
# parameters not including self (self is implied to be c)

#equivalent way
Coordinate.distance(c, origin) # directly use class