
# Rules for Naming Convention of a Variable.

# 1. We are using A-z characters.
# 2. Numbers can be utilized in the variable names. At the same time, the variable name should not start with numbers.
# 3. Special characters => _(Underscore) only allowed
# !, @,#,$,%,^ etc are not allowed.

age: int = 24 # Good Practice to start variable with smaller case.

#Avatar1 ------- 
#Avatar2

Avatar_1 = "Avatar 1" # Good Practice name a variable which is holding multipole words in it, seperationg by underscore.

# Operators : In Python, operators are special symbols or keywords used to perform operations on variables and values.
#Arithmetical Operators : Used to perform basic mathematical operations.
#Logical Operators : Used to combine conditional statements.
#Comparison operators

"""
Arithmetical Operators => +, -,*,/,%
Logical Operators => AND, OR

"""
#add_res = A+ B
#sub_res = A-B
#multi_res = A*B
#div_res = A/B
# mod_res = A%B


# Logical Operators =>  AND, OR, NOT


# True and False => 1 and 0

"""
AND =>                               OR =>                 NOT =>

True => 1 False => 0                

1 AND 0 = 0                         0 OR 1 = 1             not of 0 => 1                   
1 AND 1 = 1                         1 OR 0 = 1             not of 1 => 0
0 AND 1 = 0                         0 OR 0 = 0
0 AND 0 = 0                         1 OR 1 = 1

"""

#programs on Arithmatical and Logical Operators.

#Arithmatical Operators
A : int = 20

B: int = 4

add_res = A + B # 20 + 4 = 24
print("Addition  :", add_res)

sub_res = A-B
print("Substraction :", sub_res)

multi_res = A*B
print("Multiplication :", multi_res)

multi_res = A**B
print("Multiplication :", multi_res)

div_res = A/B
print("Division :", div_res)

mod_res = A%B
print("Modulus :", mod_res)

#Logical Operators
#AND
Logic_A1 = False and False # 0 * 0 = 0 => False
print("True and False :", Logic_A1 )

Logic_A2 = True and False # 1 * 0 = 0 => False
print("True and False :", Logic_A2 )

Logic_A3 = True and True # 1 * 1 = 1 => True
print("True and False :", Logic_A3 )

#OR
Logic_O1 = True or False # 1 + 0 => True
print("True or False :", Logic_O1)

Logic_O2 = False or False # 0 + 0 => false
print("True or False :", Logic_O2)

Logic_O3 = True or True # 1 + 1 => True
print("True or False :", Logic_O3)



#NOT
Logic_N1 = not False # not of 0 => 1
print("not False :", Logic_N1)

Logic_N2 = not True # not of 1 => 0
print("not False :", Logic_N2)

