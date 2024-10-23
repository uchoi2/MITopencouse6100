# Dictionaries
name = ['john', 'smith']
grade = ['A+', 'B']
def get_grade(student, name_list, grade_list):
    """
    :param student: a string of student name
    :param name_list: a list of student name
    :param grade_list:
    :return:
    """
    i = name_list.index(student) # Find location in list for person (return index of the student in the
    #list)
    grade = grade_list[i] # Use location index to access other info
    return (student, grade)

print(get_grade('smith', name, grade))

# List of lists
eric = ['eric', ['ps', [8,4,5]], ['mq', [6,7]]]
ana = ['ana', ['ps', [10,10,10]], ['mq', [9,10]]]
john = ['john', ['ps', [10,10,10]], ['mq', [9,10]]]

grades = [eric, ana, john] # a list of lists

# Then could access by searching lists, but code is still messy
def get_grades(who, what, data):
    for stud in data:
        if stud[0] == who:
            for info in stud[1:]:
                if info[0] == what:
                    return who, info

print(get_grades('eric', 'mq', grades))

# Better way: Dictionary
## Nice to one data structure, no separate lists
## Nice to index item of interest directly
## A Python dictionary has entries that map a key: value
## Key == custom index

my_dict = {}
d = {4:16}
grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'} # : maps key:value
grades['John']
# grades['Grace'] #KeyError

def find_grades(grades, students):
    """
    :param grades: a dict mapping student names (str) to grades (str)
    :param students: a list of student names
    :return: a list containing the grades for students (in same order)
    """
    result = []
    for char in students:
        result.append(grades[char])
    return result
d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
print(find_grades(d, ['Matt', 'Katy']))

# Dictionary operation
grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}
grades['Grace'] = 'A' # If there is no key in the dict, then this add 'Grace' on the dict and it's
                      # components
grades['Grace'] = 'C' # If the key already exists, then this changes the element of 'Grace'
del(grades['Ana']) # Delete entry of ana
'John' in grades # Testing return true
'Daniel' in grades # Testing False
'B' in grades # Testing False

def find_in_L(Ld, k):
    """
    :param Ld: a list of idcts
    :param k: is an int
    :return: True if k is a key in any dicts of Ld and False otherwise
    """
    for char in Ld:
        if k in char:
            return True
    return False
d1 = {1:2, 3:4, 5:6}
d2 = {2:4, 4:6}
d3 = {1:1, 3:9, 4:16, 5:25}
L = [d1, d2, d3]
print(find_in_L(L, 25))

## Can iterate over dictionaries but assume there is no guranteed order
## get an interable that acts like a tuple of all key
grades = {'Ana':'B', 'Matt':'A', 'John':'B', 'Katy':'A'}
grades.keys() # returns dict_keys(['Ana', 'Matt', 'John', 'Katy')
list(grades.keys()) # returns ['Ana', 'Matt', 'John', 'Katy']
## get an iterable that acts like a tuple of all dic values
grades.values() # returns dict_values(['B', 'A', 'B', 'A'])
list(grades.values()) # returns ['B', 'A', 'B', 'A']
## get an iterable that acts like a tuple of all items
grades.items()
list(grades.values())
## Typical use is to iterate over key, value tuple
for k,v in grades.items(): # k is key and v is value and loop over (k1,v1) to (k2,v2) to (kn,vn)
    print(f'key {k} has value {v}')

def count_matches(d):
    """
    :param d: is a dict
    :return: how many entries in d have the key equal to its value
    """
    count = 0
    for k,v in d.items():
        if k == v:
            count += 1
    return count

d = {1:2, 3:4, 5:6}
f = {1:2, 'a':'a', 5:5}
print(count_matches(d)) # 0
print(count_matches(f)) # 2

# Dictionaries are mutable objects (Aliasing/cloning rules apply)
# Use = sign to make an allias
# Use d.copy() to make a copy
# Assume there is no order to key or values
# Key immutable

grades = {'Ana':{'mq':[5,4,4], 'ps':[10,9,9], 'fin':'B'},
          'Bob':{'mq':[6,7,8], 'ps':[8,9,10], 'fin':'A'}}
grades['Ana']['mq'][0] # return 5

def get_average(data,what):
    all_data = []
    for stud in data.keys():
        all_data = all_data + data[stud][what]
    print(all_data)
    return sum(all_data)/len(all_data)

my_d = {'Ana':{'mq':[10], 'ps':[10,10]},
        'Bob':{'mq':[7,8], 'ps':[8]},
        'Eric':{'mq':[3], 'ps':[0]}}

print(get_average(my_d, 'mq'))

song = "RAH RAH AH AH AH ROM MAH RO MAH MAH"
def generate_word_dict(song):
    song_words = song.lower() #change word to lower case
    word_list = song_words.split() #make a list split based on the sapce
    word_dict = {}
    for w in word_list:
        if w in word_dict:
            word_dict[w] += 1 # if exist then + 1
        else:
            word_dict[w] = 1 # if not just count
    return word_dict
print(generate_word_dict(song))

word_dict = generate_word_dict(song)

def find_frequent_word(word_dict):
    words = []
    highest = max(word_dict.values())
    for k,v in word_dict.items():
        if v == highest: # possible case that there are multiple maximum.
            words.append(k)
    return (words, highest)
print(find_frequent_word(word_dict))

def occur_often(word_dict, x):
    freq_list = []
    word_freq_tuple = find_frequent_word(word_dict)
    while word_freq_tuple[1] > x:
        word_freq_tuple = find_frequent_word(word_dict)
        freq_list.append(word_freq_tuple)
        for word in word_freq_tuple[0]:
            del(word_dict[word])
    return freq_list

print(occur_often(word_dict, 1))