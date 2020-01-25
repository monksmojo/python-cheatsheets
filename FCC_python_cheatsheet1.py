# THIS IS FREE CODE CAMP Learn Python - Full Course for Beginners [Tutorial] PYTHON CHEATSHEET CREATED BY FOLLOWING THEIR VIDEO TUTORIAL ON YouTube.
# CHEATSHEET AUTHOR - MONKS_MOJO
# DATE-12TH august 2019
# VIDEO TITLE-Learn Python - Full Course for Beginners [Tutorial]
# VIDEO LINK-https://youtu.be/rfscVS0vtbw
#  BIG THANKS TO FREE CODE CAMP AND MIKE DANE FROM GIRAFFE ACADEMY FOR BECOMING MY TEACHER FOR THIS COURSE


from math import ceil, floor, sqrt

print("hello world")
# first python programme to print hello world
# printing some slashes and symbol
# using semicolon at the end of every statement is optional
print("   /|")
print("  / |")
print(" /__|")

########################### variables in python ####################

print("once there was a man name george")
print("he was 70 years old")
print("he liked his name very much")
print("but he didn't like age 70")


# instead of hard coding age and name  we can use a variable to store character name and age;

# Variables-> a container to store some data values to manage data. some of them are defined below.

character_name = "clark"
character_age = "35"
print("once there was a man name" + character_name)
print("he was" + character_age + "years old")
print("he liked his name very much")
print("but he didn't like age " + character_age)

# so we use  variables character_name and character_age to store the value which can be changed later on.

###################different type of variables###################

# string= stream of character forming plain text;
string_name = "clark kent"

# number= can contain decimal/float/double values
number_age = 10
amount_in_decimal = 46.23

# boolean= can contain true or false
is_male = True
is_female = False  # first character of true and false is uppercase

######################### working with the strings ###################
# phrase is sequence of characters
phrase = "hi i am a phrase"  # example of a string

# string with newline character in it
print("Hello everyone\nMy name is monks_mojo")

# concatenation of two strings
phrase2 = "What monks_mojo"
print(phrase2+" is noob !!!")

############ type specific function in strings ###############

# conversion of string into uppercase string.upper()
print("conversion of string into uppercase-->", phrase.upper())

# conversion of string into lowercase lower(string)
print("conversion of string into lowercase-->", phrase.lower())

# to check wether the string is in uppercase or lowercase by using if isupper() #and islower() function which returns a boolean value True Or False
print("is phrase is in uppercase -->", phrase.isupper())  # False
print("is phrase is in lowercase -->", phrase.islower())  # True

# we can also call type specific function after a type specific function
print("is " + phrase + " is in uppercase - ->",
      phrase.upper().isupper())  # True


phrase2 = "What monks_mojo knows python"

# length of the string with the help of len(string) function
print("string is-->", phrase2)
print("length of the " + phrase2 +
      " string is with the help of len(string) function is -->", len(phrase2))

# accessing a perticular character in the string with the help of index numbers which start from zero
print("first character in " + phrase2 + " is-->", phrase2[0])
print("last character in " + phrase2 + " is-->", phrase2[-1])

# you can also retrieve a index number of a character or a word from a string using string.index("character function") function
print("index of m in " + phrase2 + " is-->", phrase.index("m"))
# returns the index of the occurrence of the first m
print("index from where monks word start in-> " +
      phrase2 + " is-->", phrase2.index("monks"))

# replace a perticular sub string inside a string by using string.replace("old-substring","new-substring")
print(phrase2+" has been changed to-->\n  ",
      phrase2.replace("python", "front-end"))

############################## working with numbers#########################
# decimal number can go up to 15 position after decimal point
print("decimal number can go up to 15 position after decimal point", 2.3256)

# there is no limit of number or decimal it all depends on the memory of computer

# printing of the negative number
print("printing of the negative number", -78.32)

# calculation of the equation
print("result of the equation 10*3+4 is-->", 10*3+4)  # 34

print("result of the equation 10*(3+4) is-->", 10*(3+4))  # 70

# precedence of the numbers and operators matters

my_num = 5
print("type of {0} is {1}".format(my_num, type(my_num)))

# performing type conversion on variables
my_num = str(5)
print("type of {0} is {1}".format(my_num, type(my_num)))

print("you can concatenate a number and string by type conversion of number into string")

print("the number is"+my_num)

################ some type defined number functions of number are ###########
my_num = int(my_num)
# absolute function
print("absolute of ", my_num, " is->", abs(my_num))

# power function
# pow(x,y) function will returns the power of pow x^y
print("2^3 is->", pow(2, 3))

# max
# max(x,y) will return the maximum number from the argument passed i.e x,y
print("maximum number between 10 and 45 is->", max(10, 45))

# min
# min(x,y) will return the minimum number from the argument passed i.e x,y
print("minimum number between 10 and 45 is->", min(10, 45))

# sometimes to perform some of the math function inside the python file you have to include the math libraray

# round() function round of decimal number
print("rounding of 3.6 is->", round(3.6))  # 3

# ceil() function round of decimal number to upper value
print("ceil of 3.6 is->", ceil(3.6))  # 4

# floor() function round of decimal number to lower value
print("floor of 3.6 is->", floor(3.6))  # 3

# sqrt() function finds squareroot of the number
print("squareroot of 36 is->", sqrt(36))  # 6

################## geting input from the user #################################

name = input("enter your name: ")
print("welcome "+name+" to python cheatsheet")

# by default the input taken from the user are in string format so we have to perform type conversion
age = input("enter your age : ->")
print("so yourage is ->", age)

# what happens if we forgot to type convert data explicitly while taking input from the user
num1 = input("enter the first number: ")  # let say 3
num2 = input("enter the second number: ")  # let say 4
print("addition of "+num1+" and "+num2+" is ", num1+num2)  # 34 wrong output

# since the user input is treated as string so the above code will produce wrong output
print("wrong output")

print("correct output programme")
print("basic calculator")

num1 = float(input("eneter the first number: "))  # let say 3
num2 = float(input("eneter the second number: "))  # let say 7
print("addition of ", num1, " and ", num2,
      " is ", num1+num2)  # 10 right output

print("subtraction of ", num1, " and ", num2,
      " is ", num1-num2)  # -4 right output

##################### creation of passage based on user input ######
print("creation of passage based on user input")
name = input("enter your name: ")
age = int(input("enter your age: "))
weight = float(input("enter your weight: "))

print("hello welcome {0} to the python cheatsheet your age is {1} and your weight is {2}".format(
    name, age, weight))

# ############################### list in python ######################
# list are ordered and mutable form of collection of data which can be manipulated
friend = ["chief", "monks", "bossman"]

# since lists are ordered collection of data we can access them using index number
print(friend)
print("first element in->", friend, "is-> ", friend[0])  # chief
print("last element in->", friend, "is-> ", friend[-1])  # bossman
print("second last element in->", friend, "is-> ", friend[-2])  # monks
# to access list from reverse we use negative number notation

# a list can contain diffrent data types

data_list = ["derek", 17.3, 100, True]
print("display of list with diffrent data type->", data_list)

# slicing
print("display list from second element to second last element in->", data_list)
print(data_list[1:-2])

################ type defined function in the list ################

# append("value")
# add item to the end of the list with append() function
print("adding tom hanks to ", friend)
friend.append("tom hanks")
print(friend)

# another way to add item to list are using slicing method
friend[2:2] = ["tony"]
print("another way to add item to list are using slicing method")
print(friend)

# insert(index,value)
# when we want to add a item in a list at a specific position we use insert(index,value) function. taking two arguments 1. index where we want to insert 2. the value which we want to insert in the list
print("adding the weekend to 2nd position of", friend)
friend.insert(1, "the weekend")
print(friend)

# remove("value")
# when we want to remove an item from the list by giving item name as the argument
print("removing the weekend from the list")
friend.remove("the weekend")
print(friend)

# pop(index number)
# by default the pop() function will remove and return the last element from the list
# but we can also specify which element to remove from the list by giving index number as argument
friend.pop(2)
print(" removing tony from the list of friends ")
print(friend)

# clear()
# when we want to delete all items from the list we use clear
data_list.clear()
print("empty list ", data_list)

print("populating the list again")
data_list.append(3.14)
data_list.append(3.14)
data_list.append(3.14)
print(data_list)

# count("value")
# returns the no. of times argument value passed in the function is present in the list
print("no. of 3.14 item in list->", data_list)
print(data_list.count(3.14))  # 3

# index(index number)
# gives the index position of the item if its present in the list.
print("index of 'chief' in {0} is {1}".format(friend, friend.index("chief")))

# sort()
# sort the list in the accending order
print(
    "sorting the list {0} in accending order-> {1}".format(friend, friend.sort()))

# copy()
# copies the list to another list
print("creating copy of the list", friend)
friend_copy = friend.copy()

# reverse of the string
print("reversing the items of the list", friend_copy.reverse())

#################### tuples ################################

# it is a datastructure similar to the list where we store diffrent items.

# tuples are defined inside parantheses ()

# main difference between list and tuple is that tuple are immutable.
# i.e you cannot add items to the tuples neither you can edit the element of the tuples.

# similarities between list and tuple is both of them are ordered

coordinates = (4, 5)
# coordinates[0]=7 this will give syntax error
print("2d coordinates")
# since tuples are ordered collection of data you can access the element using index number
print(
    "x cordinate in the following 2d coordinates->{0} are ->{1}".format(coordinates, coordinates[0]))

coordinates1 = (10, 11)
coordinates2 = (16, 15)
# we can add two tuples to create one tuples
xyz_coordinates = coordinates1+coordinates2

print("The dimensional coordinates ", xyz_coordinates)

# we can create a list which contain tuples
coordinates_list = [(4, 5), (7, 10), (11, 13)]
print("a list of coordinates are", coordinates_list)

####################### Functions ########################
# function are bunch of statements used to execute a specific task.
# helps you to organizer code
# function defined once can be called again and again

# defining of the function


def sayhello(name):
    print("hello "+name+" from sayhello function")


# function call
sayhello("freddy")
# make sure you have defined function before calling it
sayhello("david")

# function can also return data
# or sometimes we want functions to return data hence we use return keyword in functions


def number_cube(num):
    return num*num*num
# any statements after return will not execute.
# after returning the value the function terminates until and unless called again


# we can directly print return value or can store it inside the variable
cube_result = number_cube(15)
print("the cube of 15 is ->", cube_result)

cube_result = number_cube(127)
print("the cube of 127 is ->", cube_result)

################# IF CONDITIONAL STATEMENTS ########################

# if statements are used when we want execute statements only when certain conditions are met
# we use comparison and logical operator in the conditional statement
# if elif and else mostly return boolean value(True,False)


is_male = True
is_tall = False

if(is_male):
    print("you are male")
else:
    print("you are not male")

# use of logical operator and or not
if(is_male or is_tall):
    if(is_male):
        print("you are male")

    if(is_tall):
        print("you are tall")
elif(is_male and is_tall):
    print("you are both male and tall")
else:
    print("you are neither male nor tall")

# comparison operator in conditional statements


def max_of_3(num1, num2, num3):
    if((num1 >= num2) and (num1 >= num3)):
        print(num1, "is greatest")
    elif(num2 >= num3):
        print(num2, "is greatest")
    else:
        print(num3, " is greatest")


print(" find greatest of 3 numbers")
num1 = int(input("eneter 1st number"))
num2 = int(input("eneter 2nd number"))
num3 = int(input("eneter 3rd number"))

max_of_3(num1, num2, num3)

# upgrading basic calculator
print("welcome to basic calculator to perform")
print("1.+ ,2.- ,3.* ,4./,5.%   ")
num1 = int(input("eneter 1st number"))
num2 = int(input("eneter 2nd number"))
op = input("enter the operator you want to use on operands")
if(op == "+"):
    print("addition of {0}+{1} is->{3}".format(num1, num2, num1+num2))
elif(op == "-"):
    print("subtraction of {0}-{1} is->{3}".format(num1, num2, num1-num2))
if(op == "*"):
    print("multiplication of {0}*{1} is->{3}".format(num1, num2, num1*num2))
if(op == "/"):
    print("division of {0}/{1} is->{3}".format(num1, num2, num1/num2))
if(op == "%"):
    print("modulas of {0}%{1} is->{3}".format(num1, num2, num1 % num2))
else:
    print("sorry operator not suppourted")

########################### dictionaries ##########################
