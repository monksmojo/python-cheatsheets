# PROGRAMIZ PYTHON TUTORIAL CHEATSHEET
# 1.INTRODUCTION TO PYTHON
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

# In Python, end of a statement is marked by a newline character. But we can make a statement extend over multiple lines with the line continuation character (\). For example:

a = 1+2+3+4 +\
    5+6+7+8 +\
    10
print("value of a=", a, "boom")
