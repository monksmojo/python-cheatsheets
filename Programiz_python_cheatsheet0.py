# PROGRAMIZ PYTHON TUTORIAL CHEATSHEET

# Python Comments
# Comments are very important while writing a program. It describes what's going on inside a program so that a person looking at the source code does not have a hard time figuring it out. You might forget the key details of the program you just wrote in a month's time. So taking time to explain these concepts in form of comments is always fruitful.

# In Python, we use the hash
# (#) symbol to start writing a comment.

# It extends up to the newline character. Comments are for programmers for better understanding of a program. Python Interpreter ignores comment.

# This is a comment
# print out Hello
print('Hello')

# Multi-line comments
# If we have comments that extend multiple lines, one way of doing it is to use hash (#) in the beginning of each line. For example:

# This is a long comment
# and it extends
# to multiple lines
# Another way of doing this is to use triple quotes, either ''' or """.

# These triple quotes are generally used for multi-line strings. But they can be used as multi-line comment as well. Unless they are not docstrings, they do not generate any extra code.

"""This is also a
perfect example of
multi-line comments"""

# INTRODUCTION TO PYTHON
# PYTHON IS A CROSS PLATFORM PROGRAMMING LANGUAGE MEANS IT CAN RUN ON MULTIPLE OS LIKE WINDOWS, MACos & LINUX
# ITS FREE AND OPEN SOURCE
# PYTHON FILES ARE ALWAYS CREATED WITH THE .py EXTENSION
# TO RUN A PYTHON FILE IN CMD/TERMINAL WRITE
# python <filename>.py

# YOUR FIRST PYTHON SCRIPT
print("hello world!")

# python keywords
# keywords are the reserved meaning in python
# we cannot use keywords as a variable name function name or as a identifier.
# they are used to define syntax and structure of python language and hold a specific meaning keyword in python are case sensitive.

# there are aprox 33 keyword in the python language

# all the keywords except True, False & None are in lowercase.
# example of keywords in python
# 1.finally
# 2.class
# 3.return
# 4.try
# 5.while

# python identifier

# an identifier is a name given to entities like class function variables etc.
# it helpus to diffrentiate diffrent entities

# Rules for writing identifiers

# 1. Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore _. Identifier can be of any length.


# 2. Names like myClass, var_1 and print_this_to_screen, all are valid example.

# 3.An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.

# 4. Keywords cannot be used as identifiers.
# forex-
# global=1; //this will give invalid syntax error

# 5.We cannot use special symbols like !, @, #, $, % etc. in our identifier. for ex-h@llo=10// invalid syntax error.

# Things to Remember
# Python is a case-sensitive language. This means, VAR and var are not the same. Always name identifiers that make sense.


# Multiple words can be separated using an underscore, this_is_a_long_variable.

# PYTHON STATEMENTS
# Instructions that a Python interpreter can execute are called statements. For example, a = 1 is an assignment statement.

# Multi-line statement
# # In Python, end of a statement is marked by a newline character. But we can make a statement extend over multiple lines with the line continuation character (\). For example:
a = 1+2+3+4 +\
    5+6+7+8 +\
    10
print("value of a=", a, "using explicit line continuation")

# using \ is the explicit way to show line continuation
# we can also implement using
# In Python, line continuation is implied inside parentheses ( ), brackets [ ] and braces { }. For instance, we can implement the above multi-line statement as

a = (1+2+3+4 +
     5+6 +
     7+8+10)
print("value of a=", a, "using explicit line continuation")

# in python its not a good practice to   use ;(semicolon) after every statement.

# in python we use semicolon to put multiple statements in a single line using semicolons, as follows

a = 1
b = 2
c = 3

# Python Indentation
# Most of the programming languages like C, C++, Java use braces { } to define a block of code. Python uses indentation.

# A code block (body of a function, loop etc.) starts with indentation and ends with the first unindented line. The amount of indentation is up to you, but it must be consistent throughout that block.

# Generally four whitespaces are used for indentation and is preferred over tabs. Here is an example.

for i in range(1, 101):
    print(i)
    if(i == 5):
        break

# Docstring in Python

# Docstring is short for documentation string.

# It is a string that occurs as the first statement in a module, function, class, or method definition. We must write what a function/class does in the docstring.
# Triple quotes are used while writing docstrings. For example:


def double_function(num):
    """Function to double the value"""
    print(2*num)


print(double_function.__doc__, "of 10")
double_function(10)

# Python Variables

# A variable is a named location used to store data in the memory. It is helpful to think of variables as a container that holds data which can be changed later throughout programming. For example,

number = 10
print(number)
# here we created a variable name number to which we can assign the value.

# a variable value can be changed
number = 0.1
print(number)

# Initially, the value of number was 10. Later it's changed to 1.1.
# we can assign value to the operator using assigment operator

# Note: In Python, we don't assign values to the variables, whereas Python gives the reference of the object (value) to the variable.

# changing the value of the variable using assigment operator
website = "apple.com"
print(website)
website = "google.com"
print(website)

# Note : Python is a type inferred language; it can automatically know apple.com is a string and declare website as a string.

# either python is loosely typed either the type of the variable or the value that variable holds is known when the statement is interprated

# example to assign multiple value to the multiple variables

a, b, c = 10, 0.6, "snake & ladders"
print("a= ", a, "b= ", b, "c= ", c)

# we can also assign same value to multiple variable

a = b = c = 10
print("a= ", a, "b= ", b, "c= ", c, "are all same")

# Constants
# A constant is a type of variable whose value cannot be changed. It is helpful to think of constants as containers that hold information which cannot be changed later.

# in python the CONSTANTS are declared in seprate module and the we import module to the main file

# for ex-:
# create a file constant.py
# declare consyants in it
# like
PI = 3.14
GRAVITY = 9.8
# import constant.py file in main file
# print the constants
print("printing the constants")
print(PI)
print(GRAVITY)

# Literals
# Literal is a raw data given in a variable or constant. In Python, there are various types of literals they are as follows:

# Numeric Literal
# Numeric Literals are immutable (unchangeable). Numeric literals can belong to 3 different numerical types Integer, Float and Complex.

a = 0b1010  # binary literal
b = 100  # decimalliteral
c = 0o310  # octal literal
d = 0x12c  # hexadecimal literal

print("a value hold binary literal conveted to decimal", a)
print("b value hold decimal literal", b)
print("c value hold octal literal conveted to decimal", c)
print("d value hold hexadecimal literal conveted to decimal", d)

# float literal
float_1 = 10.5
float_2 = 1.5e2  # 1.5*10^2
print("value of float_1 literal", float_1)
print("value of float_2 literal", float_2)

# complex literal
x = 3.14j
print("complex literal value", x)
print("real_part =", x.real)
print("imaginary part=", x.imag)

# String literals

# A string literal is a sequence of characters surrounded by quotes. We can use both single, double or triple quotes for a string. And, a character literal is a single character surrounded by single or double quotes.

string_literal = "this is python string"
character_literal = 'c'
print("the string literal is", string_literal)
print("the character literal is", character_literal)
multiline_string = '''hello today i am gonna show you->
the multiline string->
present in python'''
print("multiline strig in python")
print(multiline_string)

# We can use the slicing operator [ ] to extract an item or a range of items from a string. Index starts form 0 in Python
print("string length-", len(string_literal))
print("string_literal[0:4]-", string_literal[0:4])
print("string_literal[7:]", string_literal[7:])
print("string_literal[:len(string_literal)]",
      string_literal[:len(string_literal)])
# strings are immutable in nature so below command will cause an error
#string_literal[22] = 's'

# Boolean literals

# A Boolean literal can have any of the two values: True or False.

x = (1 == True)  # since value of true=1 it will return 1
y = (1 == False)  # since value of false=0 it will return 0 as 1!=0
a = True+1  # 2
b = False+5  # 5
print("boolean literal")
print("x is ", x)
print("y is", y)
print("a is", a)
print("b is", b)

# special literal(None Literal)
# python contains one special literal i.e None. We use to give null value to it
# for ex
drink = "available"
food = None


def menu(item):
    if item == drink:
        print(drink)
    else:
        print(food)


print("use of none literal")
menu(drink)
menu(food)

# Literral Collectuons
# there are four different literals collection like list,set,tuple,dictionary..

# Data Types in python
# Every value in python has a datatype Since everything is an object in Python programming, data types are actually classes and variables are instance (object) of these classes.

# There are various data types in Python. Some of the important types are listed below.

# 0. pytyhon number
# Integers, floating point numbers and complex numbers falls under Python numbers category. They are defined as int, float and complex class in Python.

# We can use the type() function to know which class a variable or a value belongs to and the isinstance() function to check if an object belongs to a particular class.

a = 5  # integer
print(a, "is of type", type(a))

a = 2.0  # float
print(a, "is a type of", type(a))
# A floating point number is accurate up to 15 decimal places. Integer and floating points are separated by decimal points. 1 is integer, 1.0 is floating point number.

a = 1+2j  # complex
print(a, "is it complex number ? \n ans:", isinstance(a, complex))

# 1. python list
# list is an orered sequence of item(WE CAN PERFORM SLICING OPERATION ON LIST BECAUSE THEY ARE ORDERED). it is one of the most used data type in the python and is very flexible.
fruit = ["apple", "orange", "banana"]

# all the items in the list do not to be of same type
list1 = [1, 2.8, "python-list"]
print("python list1-", list1)

print("list literal- ", fruit)
# We can use the slicing operator [ ] to extract an item or a range of items from a list. Index starts form 0 in Python
print("slicing exapmle on fruit & list1")
print("list1[0]-", list1[0])  # 1 index start from 0
print("list1[0:3]-", fruit[0:3])  # apple orange banana
print("list1[1:2]-", fruit[1:2])  # start from index 1 to (2-1)
print("list1[1:]-", fruit[1:])  # orange banana
print("list1[:3]", fruit[:3])  # apple orrange banana

# python list are mutable
fruit[2] = "mangos"
print("printing fruit list to show mutability \n", fruit)

# 2. python tuple
# Tuple is an ordered sequence of items same as list.The only difference is that tuples are immutable. Tuples once created cannot be modified.

# Tuples are used to write-protect data and are usually faster than list as it cannot change dynamically.

# It is defined within parentheses () where items are separated by commas.
number = (10, 20, 30, 30)
print("tuple literal-", number)

# all the elements of the tuple can be of diffrent types
tuple1 = (1.0, 6, "HelloTupple")
# We can use the slicing operator [] to extract items but we cannot change its value.
print("tuple1[2]-", tuple1[2])
print("tuple1[0:3]-", tuple1[0:3])

# 3. python dictionary
# Dictionary is an unordered collection of key-value pairs.

# It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.

# In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.

alphabets = {"a": "apple", "b": "ball", "c": "cat"}
print("dictionary literal", alphabets)
print("type of alphabets-", type(alphabets))
print("alphabets['a']-", alphabets["a"])
print("alphabets['b']-", alphabets["b"])
# 4. python set
# Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.

# We can perform set operations like union, intersection on two sets. Set have unique values. They eliminate duplicates.
vowels = {"a", "e", "i", "o", "u"}
set1 = {5, 2, 3, 3, 4, 6}
print("set literal-", vowels)
print("set1-", set1)
# Since, set are unordered collection, indexing has no meaning. Hence the slicing operator [] does not work. so below statement will give error
# print(set1,set[1])

# we can also convert one one data type to another
print("converting", 5, "int to float", float(5))
print("converting", 5.0, "float to int", int(5.0))
print("converting", 100, "int to string", str(5.0))
# you can't convert string to int the following code will give error
# >>> int('12po')

# converting string to a list
print("converting string-"+'"cool mamba"'+"to list", list("cool mamba"))
# converting list to tuple
print("converting list", [10, 11.56, "hello"],
      "to tuple", tuple([10, 11.56, "hello"]))

# we can alos convert list to set, tuple to set & # and vice versa

# list to dict
print("converting list", [[1, 2], [3, 4]], "to dict", dict([[1, 2], [3, 4]]))
