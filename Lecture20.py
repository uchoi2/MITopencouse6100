# Fitness Tracker Object-Oriented Programming Example
# Suppose we are writing a program to track workouts
## Improved workout class
### better get-calories method
### using datetime objects
## Run workout class
### reusing __str__ from parent
### override get_calories from parent
### add __eq__ method not in parent

## Common properties -> Superclass
### Swimming specific: swimming pace stroke type 100yd splits
### Running specific: cadence running pace mile splits elevation

class SimpleWorkout(object):
    """ A Simple class to keep track of workouts """
    # definining initialized parameters
    def __init__(self, start, end, calories): # start, end, calories burned
        self.start = start
        self.end = end
        self.calories = calories
        self.icon = 'icon'  #icon and kind are attributes even though an instance is not initialized with them as a param
        self.kind = 'Workout'
    # getter
    def get_calories(self):
        return self.calories
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    # setter
    def set_calories(self, calories):
        self.calories = calories
    def set_start(self, start):
        self.start = start
    def set_end(self, end):
        self.end = end
my_workout = SimpleWorkout('9/30/2021 1:35 PM', '9/30/2021 1:57 PM', 200) #instance

# self provides access to class state dictionary
print(SimpleWorkout.__dict__.keys()) # display doc and modules and programs we set
print(SimpleWorkout.__dict__.values())

# Instance state dictionary can be accessed via self_keyword
print(my_workout.__dict__.keys())
print(my_workout.__dict__.values())

# Why information hiding?
## Keep the interface of your class as simple as possible
## Use getters and setters, not attributes: get_calories() rather than calories
### Prevents bugs due to changes in implementation
## May seem inconsequential in small programs, but for large programs complex interfaces increase the potential for bugs
## If you are writing a class for others to use, you are committing to maintaining its interface!

from dateutil import parser # brings in a bunch of functions and classes for the library
# Improved version
class Workout(object):
    cal_per_hr = 200
    def __init__(self, start, end, calories = None):
        self.start = parser.parse(start) # a way of designating type of datetime rather than just string
        self.end = parser.parse(end)
        self.calories = calories # may be none
        self.icon = '😀'
        self.kind = 'Workout'
    def get_calories(self):
        if (self.calories == None): # if calories was not passed in # Why just calories not working
            return Workout.cal_per_hr*(self.end - self.start).total_seconds()/3600
            # self.end-self.start allowed on datetime object
        else: # if calories was passed in, just use that value
            return self.calories
    def get_duration(self):
        return self.end - self.start
    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def get_kind(self):
        return self.kind
    def get_icon(self):
        return self.icon
    def set_calories(self, calories):
        self.calories = calories
    def set_start(self, start):
        self.start = start
    def set_end(self, end):
        self.end = end
    def __eq__(self, other):
        """
        :param other:
        :return: true if this workout is equal to another workout
        """
        return type(self) == type(other) and \
                self.start == other.start and \
                self.end == other.end and \
                self.kind == other.kind and \
                self.get_calories() == other.get_caloreis()
    def __str__(self):
        width = 16
        retstr = f"|{'_'*width}|\n" #\n change the line
        retstr += f"|{' '*width}|\n"
        iconLen = 0
        retstr += f"| {self.icon}{' '*(width-3)}|\n"
        retstr += f"| {self.kind}{' '*(width - len(self.kind)-1)}|\n"
        retstr += f"|{' '*width}|\n"
        duration_str = str(self.get_duration())
        retstr += f"| {duration_str}{' '*(width-len(duration_str)-1)}|\n"
        cal_str = f"{self.get_calories():.0f}"
        retstr += f"| {cal_str} Calories {' '*(width-len(cal_str)-11)}|\n"
        retstr += f"|{' '*width}|\n"
        retstr += f"|{'_'*width}|\n"
        return retstr
# start = '9/30/2021 1:35 PM'
# end = '9/30/2021 1:45 PM'
# start_date = parser.parse(start)
# end_date = parser.parse(end)
# type(start_date)
# print((end_date - start_date)) # calculating the time differences in hour:minute:second
# print((end_date - start_date).total_seconds())  # convert the difference into the second level
#
# print(Workout.cal_per_hr)
# w = Workout('1/1/2021 2:34', '1/1/2021 3:35')
# print(w.cal_per_hr)
# Workout.cal_per_hr = 250 # cal_per_hr changes from 200 to 250
# print(w.cal_per_hr)

# RunWorkout subclass
from lec20_helpers import gpsDistance
from math import sin, cos, tan, atan2, ladian
def getDistance(p1,p2):
    R = 6373.0
    lat1 = radians(p1[0])
    lon1 = radians(p1[1])
    lat2 = radians(p2[0])
    lat2 = radians(p2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)
class RunWorkout(Workout):
    cal_per_km = 100
    def __init__(self, start, end, elev=0, calories = None):
        super().__init__(start, end, calories) # to setup Workout base instance / parent access via super().
        # Workout.__init__(start, end, calories) # call directly
        self.icon = '🏃'
        self.kind = 'Running'
        self.elev = elev
    def get_elev(self):
        return self.elev
    def set_elev(self, e):
        self.elev = e
    def get_calories(self):
        if (self.route_gps_points != None):
            dist = 0
            lastP = self.routGpsPoint[0]
            for p in self.routeGpspoint[1:]:
                dist += gpsDistance(lastP,p)
                lastP = p
            return dist * Runworkout.cal_per_km
        else:
            return super().get_calories()
## Why use inheritence
### Improve clarity
#### commonalities are explicit in parent class
#### differences are explicit in subclass
### Reuse code
### Enhance modularity
#### can psss subclasses to any method that uses parent

# Where can I use an instance of a class
## We can use an instance of RunWorkout anywhere Workout can be used
## Opposite is not true (Cannot use Workout anywhere RunWorkout is used)
## Consider two helper functions

def total_calories(workouts):
    cals = 0
    for w in workouts:
        cals += w.get_calories()
    return cals

def total_elevation(run_workouts):
    elev = 0
    for w in run_workouts:
        elev += w.get_elev()
    return elev

w1 = Workout('9/30/2021 1:35 PM', '9/30/2021 2:05 PM')
w2 = Workout('9/30/2021 4:35 PM', '9/30/2021 5:05 PM')
rw1 = RunWorkout('9/30/2021 1:35 PM', '9/30/2021 3:35 PM', 100)
rw2 = RunWorkout('9/30/2021 1:35 PM', '9/30/2021 3:35 PM', 200)

total_calories([w1,w2,rw1,rw2])
total_elevation