#this is a general python library
#Author:@Cmoz
#Nov 17 2020

##################################################
##################################################
#Python's namedtuples can be a great alternative to defining a class manually

from collections import namedtuple
Car = namedtuple('Car', 'color mileage')

my_car = Car('red', 39787.4)
my_car.color
my_car.mileage
my_car

#namedtuples are immutable

###########################################################
##################################################
#The get() method on Python dicts and its "default" arg arguments

name_for_userid = {
	234:"alice",
	345:"bob",
	456:"stacey",

}

def greeting(userid):
	return "Hi %s!" % name_for_userid.get(userid, "there")

greeting(234)
# Hi alice
greeting(988)
#Hi there

#################################################
#How to sort a Python dict (dictionary) by value
# (== get a representation sorted by value)

xs = {'a':4, 'b':3, 'c':2, 'd':1}
sorted(xs.items(), key=lambda x:x[1])
#[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
#or
import operator
sorted(xs.items(),key=operator.itemgetter(1))
#[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

###########################################################
#######################################################
##Merging two dicts (dicrionaries) in Python 3.5+ with a single expression

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
z
#{'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could use this
z = dict(x, **y)
z
#{'a': 1, 'c': 4, 'b': 
# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting 
# duplicates from left to right.

########################################################
#######################################################
#Different ways to test multiple flags at once in Python
# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0
if x == 1 or y==1 or z==1:
	print('passed')

if 1 in (x,y,z):
	print('passed')

#these only test for truthiness:
if x or y or z:
	print('passed')

if any((x,y,z)):
	print('passed')

####################################################
###########################################
## Using "json.dumps()" to pretty-print Python dicts
## alternative to the recommended pprint module

my_mapping = {'a':21, 'b':13, 'c':0xc0ffee}
my_mapping
##{'b': 42, 'c': 12648430. 'a': 23}  # 😞

# the json module can do a much better job:
import json
print(json.dumps(my_mapping, indent=4, sort_keys=True))

#{
#    "a": 23,
#    "b": 42,
#    "c": 12648430
#}

#note this only works with dicts containing
#primitive types
#Note: stick to "print" module

##implementation of pprint built in module

import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'nii']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)

#[   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
#   'spam',
#   'eggs',
#    'lumberjack',
#    'knights',
#    'ni']

pp.pprint.PrettyPrinter(width=41, compact=True) #depth=6
pp.pprint(stuff)
#[['spam', 'eggs', 'lumberjack',
# 'knights', 'ni'],
# 'spam', 'eggs', 'lumberjack', 'knights',
#'ni']
#
#

#################################
################################
#Function argument unpacking
def myfunc(x,y,z):
	print(x,y,z)

tuple_vec=(1,0,1)
dict_vec={'x':1,'y':0,'z':1}
myfunc(*tuple_vec)
##1,0,1
myfunc(**dict_vec)
##1,0,1