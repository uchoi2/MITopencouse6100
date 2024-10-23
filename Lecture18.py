# More Python Class Methods

class Coordinate(object):
    """ A Coordinate made up of an x and y value """
    def __init__(self, xval, yval):
        """
        Sets the x and y values
        """
        self.x = xval
        self.y = yval
    def distance(self, other):
        """
        Returns euclidean dist between two coord obj
        """
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def to_origin(self):
        """
        Always sets self.x and self.y to 0.0
        """
        self.x = 0
        self.y = 0
c = Coordinate(3,4)
origin = Coordinate(0,0)

print(c.distance(origin))
c.to_origin()
print(c.x, c.y)

# Using Classes to Build other classes
class Circle(object):
    def __init__(self, center, radius):
        if type(center) != Coordinate:
            raise ValueError
        if type(radius) != int:
            raise ValueError
        self.center = center
        self.radius = radius
    def is_inside(self, point):
        """
        :param point: variable type Coordinate
        :return: True if point is in self, False otherwise
        """
        return point.distance(self.center) <= self.radius # because type of point is Coordinate, it can use attribute of it.
    def is_inside2(self, point):
        return self.center.distance(point) <= self.radius # distance from center to the point

center = Coordinate(2,2)
my_circle = Circle(center, 2) # No error
# my_circle = Circle(center, 'two') # ValueError
p = Coordinate(1,1)
print(my_circle.is_inside(p))
print(my_circle.is_inside2(p))

# Example: Multiply Fractions
class SimpleFraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
    def times(self, oth):
        top = self.num*oth.num
        bottom = self.denom*oth.denom
        return top/bottom
    def plus(self, oth):
        top = self.num*oth.denom + self.denom*oth.num
        bottom = self.denom*oth.denom
        return top/bottom
    def get_inverse(self): # default function
        """
        :return: Return a float representing 1/self
        """
        return self.denom/self.num
    def invert(self):
        """
        :return: sets self's num to denom and vice versa
        Return None
        """
        newdenom = self.num
        newnum = self.denom
        self.num = newnum
        self.denom = newdenom
        #other way
        # (self.num, self.denom) = (self.denom, self.num)
f1 = SimpleFraction(3,4)
f2 = SimpleFraction(1,4)
print(f1.num, f1.denom)
print(f1.plus(f2))
print(f1.times(f2))
print(f1.get_inverse())

# Special Operators implemented with dunder methods
## +,-,==,<,>,len(),print, and many others are shorthand notation
## Behind the scenes, these get replaced by a method
### https://docs.python.org/3/reference/datamodel.html#basic-customization
## Can override these to work with your class 코딩에서 override는 재정의를 의미
## e.g.
# __add__(self,other) -> self + other
# __sub__(self,other) -> self - other
# __mul__(self,other) -> self * other
# __truediv__(self,other) -> self / other
# __eq__(self,other) -> self == other
# __lt__(self,other) -> self < other
# __len__(self) -> len(self)
# __str__(self) -> print(self)
# __float__(self) -> float(self) i.e cast
# __pow__ -> self**other
# etc..

# Printing out own datatype
class Coordinate(object):
    """ A Coordinate made up of an x and y value """
    def __init__(self, xval, yval):
        """
        Sets the x and y values
        """
        self.x = xval
        self.y = yval
    def distance(self, other):
        """
        Returns euclidean dist between two coord obj
        """
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5
    def to_origin(self):
        """
        Always sets self.x and self.y to 0.0
        """
        self.x = 0
        self.y = 0
    def __str__(self): # controlling how print() apply to Coordinate
        return f'<{str(self.x)},{str(self.y)}>'

c = Coordinate(3,4)
origin = Coordinate(0,0)
print(c)

class Fraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
    def __str__(self):
        if self.denom == 1:
            return f'{self.num}'
        else:
            return f'{self.num}/{self.denom}'
    def __mul__(self, other):
        top = self.num*other.num
        bottom = self.denom*other.denom
        return Fraction(top, bottom) # For new method, return type is also Fraction object.
f1 = Fraction(3,4)
f2 = Fraction(1,4)
f3 = Fraction(5,1)
print(f1)
print(f2)
print(f3)
a = Fraction(1,4)
b = Fraction(3,4)
print(a)
c = a*b
print(c)
print(a.__mul__(b))
print(Fraction.__mul__(a,b))

# Big Idea: Special operations we've been using are just method behind the scenes
## Things like:
### print, len + * / ....

# Can keep both options by adding a method to cast to a float
class Fraction(object):
    def __init__(self, n, d):
        self.num = n
        self.denom = d
    def __str__(self):
        if self.denom == 1:
            return f'{self.num}'
        else:
            return f'{self.num}/{self.denom}'
    def __mul__(self, other):
        top = self.num*other.num
        bottom = self.denom*other.denom
        return Fraction(top, bottom) # For new method, return type is also Fraction object.
    def __float__(self): # Change the definition of float() for this class
        return self.num/self.denom
    def reduce(self):
        def gcd(n,d): # Funtion to find the greatest common divisor
            while d!= 0:
                (d, n) = (n%d, d)
            return n
        if self.denom == 0:
            return None
        elif self.denom == 1: # is this a good idea?
            # return self.num
            return Fraction(self.num, 1) # much better to sustain the consistency on the type
        else:
            greatest_common_divisor = gcd(self.denum, self.denom)
            top = int(self.num/greatest_common_divisor)
            bottom = int(self.denom/greatest_common_divisor)
            return Fraction(top, bottom)
a = Fraction(1,4)
b = Fraction(3,4)
c = a*b
print(c)
print(float(c))

# Add a method