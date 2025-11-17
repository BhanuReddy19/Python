"""
{name_ of_ variable}:{data_type} = {Value}
age : int =24
salary: float = 50000
"""
age:int=24
print("Age :",age)
salary:float = 50000
print("Salary :",salary)
name:str="Reddy"
print("Name :",name)
Is:bool =True
print("Statement :",Is)
Undefined_value="new value"
print("Undefined_value :",Undefined_value)
defined_value="old value"
print("defined_value :",defined_value)

# Declaring a Variable of Type String
variable_name = "string_value"
message = "Pass"
print(message)

#Reassignment means assigning a new value to an already existing variable.
x = 10 # initially assigned integer
print(x)

x = 20  # reassigned with another integer
print(x)

x = "Divya" # reassigned with a string value
print(x)

#The assignment operator (=) is used to assign a value to a variable.
x = 2  # Assigns 5 to x
y = "Get in"  # Assigns string to y

# don’t need to declare the data type of a variable explicitly. The type is determined automatically at runtime based on the assigned value.
x = 11  # x is int
print(type(x))

x = "Divya"  # x is now string
print(type(x))

x = 7.7  # x is now float
print(type(x))

Y = True
print(type(Y))

# Just use the variable name inside the print() function. To access a variable and print its value
name = "Divya"
age = 24

print(name)
print(age)


# Yes, we can access and print a variable after it has been declared and assigned a value.But if we can  try to access it before declaration, we will get an error.
x = 20
print(x)  # Works fine

print(y)     # Error: y is not defined
y = 10