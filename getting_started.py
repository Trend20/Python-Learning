# Numbers and Texts
# There are different types of numbers in python.
# 1. Integers(int): Numbers without decimal parts(1, 2, 3, 5, 6, -12)
# 2. Floating point(float): Numbers with decimal parts(2.3, 4.09, 5.34).
# String(str): They are wrapped inside double or single curly braces. ('Hello World!')

# Variables
age = 12
name = 'Michael Banta Mickey'
print(age)
print(name)

# Python Keywords
# All the keywords except True, False and None are written in lowercase.
# They include: except, if, def, elif, while, lambda, continue, else, break, class, await, except, finally ...etc

# Constants

# Data Types
'''
Numeric: Holds numeric value and are categorized into 3(int, float and complex)
String(str): Holds sequence of characters.
Sequence(list, tuple, range): Holds collection of items.
Mapping(dict): Holds data in key value pair form.
Boolean(bool): Holds either True or False.
Set(set,frozeenset): Holds collection of unique items.
'''

# Python Type Conversion
'''
There are two types of type conversion in python.
1. Implicit conversion => automatic type conversion.
2. Explicit conversion(Type Casting) => manual type conversion.
'''

# example of implicit conversion
integer_number = 23
floating_number = 2.5
new_number = integer_number + floating_number
print("Value: ", new_number)
print("Data Type: ", type(new_number))

# example of explicit conversion
# Here we use built-in functions such as str(), int() and float() to convert the data type to the required type.
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:", type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:", type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:", type(num_sum))
