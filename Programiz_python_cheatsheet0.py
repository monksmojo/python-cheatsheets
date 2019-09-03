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
