#this is a general python library
#Author:@Cmoz
#Nov 17 2020


#Python's namedtuples can be a great alternative to defining a class manually

from collections import namedtuple
Car = namedtuple('Car', 'color mileage')

my_car = Car('red', 39787.4)
my_car.color
my_car.mileage
my_car

#namedtuples are immutable

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
