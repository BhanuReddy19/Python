
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

