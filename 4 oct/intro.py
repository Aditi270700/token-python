# and operator
print(True and True)
print(3>2 and 34<5)

# or operator
print(3>2 or 34<5)

print(not(24>56))
print(not(56<100))
print(not(3>2 or 34<5))

#membership operator
# in, not in
string1 = "apple @is good 4555 health"
print("is" in string1)#true
print("si" in string1)#false
print("apple  is" in string1)#false
print("4" in string1)#true

#identity operator
# is, is not

# is operator gives True when we test for same object
#otherwise false.

# variables and datatype in python
num1 = 60
num2 = 100
num3 = 60
print(id(num1))
print(id(num2))
print(id(num3))


