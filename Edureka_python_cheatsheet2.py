#THIS IS EDUREKA PYTHON CHEATSHEET CREATED BY FOLLOWING THEIR VIDEO TUTORIAL#
# CHEATSHEET AUTHOR - MONKS_MOJO
# DATE-12TH DECEMBER 2019
# VIDEO TITLE-Python Tutorial For Beginners | Python Full Course From Scratch | Python Programming | Edureka
# VIDEO LINK-https://www.youtube.com/watch?v=vaysJAMDaZw
# THIS TITORIAL IS TILL-3:34:22 User-Defined Exceptions
# CAUSE I JUST WANT TO LEARN PYTHON BASICS AND USE IT FOR COMPETITIVE PROGRAMMING

#################### START OF TUTORIAL ####################

# Python was created in December 1989 by Guido van Rossum
# Python is a interpreted, object oriented high level programming language.

# Q-difference between interpreted language and compiled time language
# Ans-
# Interpreted language-Reads every line individually and executes it. If found error it will stop the execution until the error is resolved.Interpreter is always present in the memory.
# Compiled language- the whole language is compiled in one go in to object code.if there are syntax error they are displayed at the end of compilation.Compiler is only loaded into the memory when the source code is needed to be converted to object code.

#### Features Of Python #####
# -> python is easy to learn read and write language
# -> python is free and open source software--FOSS(FREE OPEN SOURCE SOFTWARE)which means one can freely distribute the copies of this software and reads it source code and modify it.
# -> High level Language--one does not need to worry about the low level operating system functionalities like memory management while writing python scripts.
# -> Python is portable souppotred by many operating system.
# -> support functional programming and object oriented programming paradigm.
# -> python is extensible i.e it can be called by a c++ function of can be integrated in a c++ program.
#############################################


###### Operatorts In Python #######
# we have following operators.
# 1-Arthemetic Operator
# 2-Assignment Operator
# 3-Logical Operator
# 4-Comaprison Operator
# 5-Bitwise Operator
# 6-Identity Operator
# 7-Membership Operator

############## Arthemetic Operator ###########
num1 = 10
num2 = 25
print(" num-1 is ->{0}\n num2-2 is ->{1}".format(num1, num2))
# 1.a-addition
# add two operand or unary plus
print("addition->", num1+num2)  # 35

# 1.b-subtraction
# subtract two operand or unary subtract.
print("subtraction->", num1-num2)  # 15

# 1.c-multiplication
# multiplication two operand.
print("multiplication", num1*num2)  # 250

# 1.d-Division
# devision of left operand with right operand and return a float.
print("Devision", num1/num2)  # 0.4

# 1.e-Exponential
# left operand raised to the power of  right operand.
print("Exponential", num1**num2)  # 10000000000000000000000000

# 1.f-Modulas
# Remainder of the devision of left operand by the right operand.
print("Modulas", num2 % num1)  # 5

# 1.g-floor division
# the division that result into whole number adjusted to the left in the number line.
print("Floor Division", num2//num1)  # 2
#################################################

################## Assignment Operator ##############
num3 = 10
# 2.a +=
num3 += 10
print("num3=num3+10 shorthand---->num3+=10-->{0}".format(num3))  # 20
# 2.b -=
num3 -= 10
print("num3=num3-10 shorthand---->num3-=10-->{0}".format(num3))  # 10
# 2.c *=
num3 *= 10
print("num3=num3*10 shorthand---->num3*=10-->{0}".format(num3))  # 100
# 2.d /=
num3 /= 10
print("num3=num3/10 shorthand---->num3/=10-->{0}".format(num3))  # 10
# 2.e %=
num3 %= 4
print("num3=num3%4 shorthand---->num3%=4-->{0}".format(num3))  # 2
# 2.f //=
num3 //= 2
print("num3=num3%2 shorthand---->num3//=2-->{0}".format(num3))  # 1
# 2.g **=
num3 **= 4
print("num3=num3**4 shorthand---->num3**=4-->{0}".format(num3))  # 1
######################################################################

################### Comparison Operator #########################
# 3.a >(greater than) return True if left operand is greater than right operand otherwise False
print(
    "num1-->{0} & num2--->{1} then  Is num1>num2-->{2}".format(num1, num2, num1 > num2))

# 3.b <(less than) return True if left operand is smaller than right operand otherwise False
print(
    "num1-->{0} & num2--->{1} then  Is num1<num2-->{2}".format(num1, num2, num1 < num2))

# 3.c ==(equal too) return True if left operand is equal to the right operand otherwise False
print("num1-->{0} & num2--->{1} then  Is num1==num2-->{2}".format(num1, num2, num1 == num2))

# 3.d !=(not equal too) return True if left operand is not equal to the right operand otherwise False
print(
    "num1-->{0} & num2--->{1} then  Is num1>num2-->{2}".format(num1, num2, num1 > num2))
############################################################################

####################### Logical Operator ##############################
x = True
y = False
print("x value-->", x)
print("y value-->", y)
# 1.and return True if both statement are true otherwise False
# 2.or return True if any of the statement is True Otherwise False
# 3.not return complement of the value
print("x and y-->", x and y)  # False
print("x or y-->", x or y)  # True
print("not y-->", not y)  # True
# -logical operator are mainly used in conditional statement
#######################################################################

#################### BITWISE OPERATOR ########################
# &(and)-->perform or operator on each bit of  number
# 7-->111(in binary),5--->101(in binary)
# performing bitwise & on -- (111-->7 & 101-->5) will result in 101-->5
print("7-->111(in binary),5--->101(in binary) performing bitwise & on it will give-->", 7 & 5)  # 5(101)

# |(or)-->perform and operator on each bit of number
# 7-->111(in binary),5--->101(in binary)
# performing bitwise | on -- (111-->7 | 101-->5) will result in 111->7
print("7-->111(in binary),5--->101(in binary) performing bitwise | on it will give-->", 7 | 5)  # 7(111)


# ^(xor)-->perform xor operator on each bit of number
# 7-->111(in binary),5--->101(in binary)
# performing bitwise ^ on -- (111-->7 ^ 101-->5) will result in 010->2
print("7-->111(in binary),5--->101(in binary) performing bitwise ^ on it will give-->", 7 ^ 5)  # 2(010)
##############################################################

###############Identity Operator################
# --> is (return True if the operands are identical.i.e refers to the same object)
# --> is not(return True if the operands are not identical.i.e does not refer to same object)
# everything in python is an object
# to know the type of object we use type() function
x = 5  # (will be identical to number 5)

print("type of x is->", type(x))
print("Is x is 5", x is 5)  # True
print("Is x is not 5", x is not 5)  # False
################################################

##################### Membership Operator ###########################
# helps in searching of an element in the list or string
# in -->Returns true if the perticular element is found in the list
# not in --> Returns true if the perticular element is not found in the list
list1 = [1, 2, 3, 4, 5, 6]
print("the list is-->", list)
print("is 3 present in the list-->", 3 in list)
print("is 3 not present in the list-->", 3 not in list)
#######################################################################


###################### DATATYPES IN PYTHON ##############################
# >> python is a loosly typed language
# >> therefore no need to define datatype of the variable
# >> no need to declare variable before using them

# datatypes are of two types 1> mutable 2> immutable

# 1> mutable datatypes contain
#a> set
#b> dictionaries
#c> list

# 2> immutable datatypes contain
#a> number
#b> string
#c> tuple
#########################################################################
