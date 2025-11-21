marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: Fail")


Population = 50000
if Population >= 55000:
    print("Grade: A+")
elif Population >= 65000:
    print("Grade: A")
else:
    print("Grade: Fail")



age = 17

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

num = 0

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# String → Boolean Conversion
print("Empty String :", bool(""))

print("Not Empty String :", bool("A"))

print("Empty String, but with space :", bool(" ")) #----- Empty string with space--- True

# Boolean → Integer Conversion
Bpr = int(True)
print("int(True) :", Bpr)

Bpr = int(False)
print("int(False) :", Bpr)

# String → Integer Conversion
print("int('34567') :", int("34567"))
#print(int("34567_W"))----ValueError: invalid literal for int()

#String → Float Conversion
Bpr = float('54545.5')
print("float('54545.5'):",Bpr )

# Boolean → String Conversion
print("str(True) :", str(True))
print("str(False) :", str(False))

# Boolean Logic with Numbers (and, or)
i = 12
j = 13
print("i and j =", bool(i and j)) 

A = 0
B = 1
print("A and B =", bool(A and B))

x = 0
y = 20
print("x or y =", bool(x or y))

x = 0
y = 0
print("x or y =", bool(x or y))

h = 34
rs = h + 25
print("Sum =", rs)

# Convert sum to different data types
print("To int :", int(rs))
print("To float :", float(rs))
print("To string :", str(rs))
print("To bool :", bool(rs))

h = 34
rs = h - 55
print("Sum =", rs)

print("To int :", int(rs))
print("To float :", float(rs))
print("To string :", str(rs))
print("To bool :", bool(rs))

h = 0
rs = h + 0
print("Sum =", rs)

print("To int :", int(rs))
print("To float :", float(rs))
print("To string :", str(rs))
print("To bool :", bool(rs))









