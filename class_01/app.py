# 🔹 Python Data Types (with Examples)
                                                                            # 1. Numeric Types


# Integer (int)
x = 10
print(type(x))

# Floating-point (float)
y = 3.14
print(type(y))

# Complex number (complex)
z = 2 + 3j
print(type(z))

                                                                            # 2. Sequence Types

# String (str)
text = "Hello, Python!"
print(type(text))

# List (list) - Mutable ordered collection
my_list = [1, 2, 3, "Python"]
print(type(my_list))

# Tuple (tuple) - Immutable ordered collection
my_tuple = (1, 2, 3, "Python")
print(type(my_tuple))

# Range (range) - Sequence of numbers
my_range = range(5)
print(type(my_range))

                                                                            # 3. Set Types

# Set (set) - Unordered collection with unique elements
my_set = {1, 2, 3, 3, 2}
print(type(my_set))
print(my_set)

# Frozenset (frozenset) - Immutable version of a set
frozen = frozenset([1, 2, 3])
print(type(frozen))

                                                                            # 4. Mapping Types

# Dictionary (dict) - Key-value pairs
my_dict = {"name": "Alice", "age": 25}
print(type(my_dict))

                                                                            # 5. Boolean Type

# Boolean (bool) - True or False
is_active = True
print(type(is_active))

                                                                            # 6. Binary Types

# Bytes (bytes) - Immutable byte sequence
my_bytes = b"hello"
print(type(my_bytes))

# Bytearray (bytearray) - Mutable byte sequence
my_bytearray = bytearray(5) 
print(type(my_bytearray))

# Memoryview (memoryview) - Memory-efficient byte handling
mv = memoryview(b"Python")
print(type(mv))

                                                                            # 7. None Type

# NoneType (None) - Represents the absence of a value
nothing = None
print(type(nothing))

# 🔹 Python Special Keywords (with Examples)
                                                                          


import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
#  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 
#  'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
#  'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield', 
#  'match', 'case']

                                                                         # 1. Control Flow Keywords

x = 10
# if, elif, else
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")

# for loop
for i in range(3):
    print("Loop:", i)

# while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# # break, continue, pass
for i in range(5):
    if i == 2:
        break  # Stops the loop
    if i == 1:
        continue  # Skips this iteration
    print("i:", i)


                                                                            # 2. Exception Handling Keywords

try:
    num = 10 / 0  # Will cause ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This runs no matter what.")

# # assert - Used for debugging
x = 5
assert x > 0, "x should be positive"

                                                                                # 3. Function & Class Keywords

# def - Define a function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# # lambda - Anonymous function
square = lambda x: x * x
print(square(5))

# # class - Define a class
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.name)

                                                                                # 4. Variable Handling Keywords

# global - Access global variables inside a function
x = 10
def modify():
    global x
    x = 20

modify()
print(x) 

# # nonlocal - Modify variables from an enclosing scope
def outer():
    y = 5
    def inner():
        nonlocal y
        y = 10
    inner()
    print(y)

outer() 
# # del - Delete a variable or object
z = 100
del z 

                                                                        # 5. Boolean & None Keywords

# True, False - Boolean values
print(True and False)  # Output: False
print(not True)  # Output: False

# # None - Represents a null value
value = None
print(value)

                                                                        # 6. Import & Module Keywords

# import - Importing a module
import math
print(math.sqrt(16))

# # from, as - Importing specific part of a module
from math import pi as circle_pi
print(circle_pi)

# # with - Used in resource management
with open("example.txt", "w") as file:
    file.write("Hello, world!") 

                                                                        # 7. Object-Oriented Programming Keywords

# is - Identity comparison
a = [1, 2, 3]
b = a
print(a is b)  # Output: True

# # in - Membership test
print(2 in [1, 2, 3])  # Output: True

# # not, and, or - Logical operators
print(not False)  # Output: True
print(True and False)  # Output: False
print(True or False)  # Output: True

# 8. Asynchronous Programming Keywords

import asyncio
# async, await - Define asynchronous functions
async def my_async_function():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(my_async_function())

                                                                        # 9. Special Keywords

# match, case - Pattern matching (Python 3.10+)
value = 2
match value:
    case 1:
        print("One")
    case 2:
        print("Two")  # Output: Two
    case _:
        print("Unknown number")