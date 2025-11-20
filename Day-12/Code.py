# Add, Subtract, Multiply, Divide Two Numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Check Whether Number is Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# Function to Calculate Square of a Number
def square(num):
    return num * num
n = int(input("Enter a number: "))
print("Square:", square(n))

# Check Positive, Negative, or Zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# Greeting Function Using Username
def greet(name):
    print("Welcome", name + "!")
username = input("Enter your name: ")
greet(username)


# Simple Interest Program
P = float(input("Enter Principal: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time: "))
SI = (P * R * T) / 100
print("Simple Interest =", SI)

# Check Leap Year
#divisible by 4
#not divisible by 100
#unless divisible by 400
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Greatest of Two Numbers Using Function
def greatest(a, b):
    if a > b:
        print("Greater number is:", a)
    else:
        print("Greater number is:", b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
greatest(x, y)

# Check Divisible by Both 3 and 5
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")





