# Python Operators Examples

# Arithmetic Operators
# Used to perform mathematical operations
x = 10
y = 3
print("Addition:", x + y)        # Addition
print("Subtraction:", x - y)     # Subtraction
print("Multiplication:", x * y)  # Multiplication
print("Division:", x / y)        # Division (float result)
print("Floor Division:", x // y) # Division (integer result)
print("Modulus:", x % y)         # Remainder
print("Exponentiation:", x ** y) # Power

# Assignment Operators
# Used to assign values to variables
x = 5
x += 3  # Same as x = x + 3
print("After +=:", x)
x -= 2  # Same as x = x - 2
print("After -=:", x)

# Comparison Operators
# Used to compare values
print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)

# Logical Operators
# Used to combine conditional statements
print("Logical AND:", x > 2 and y < 5)  # Returns True if both conditions are true
print("Logical OR:", x > 2 or y > 5)   # Returns True if at least one condition is true
print("Logical NOT:", not(x > 2))     # Reverses the result

# Identity Operators
# Used to compare memory locations of two objects
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print("Is:", a is b)     # True because b is assigned the same object as a
print("Is not:", a is not c) # True because c is a different object with the same values

# Membership Operators
# Used to check if a value is in a sequence
print("In operator:", 2 in a)   # True because 2 exists in the list a
print("Not in operator:", 4 not in a)  # True because 4 is not in the list a

# Bitwise Operators
# Used to perform operations at the bit level
m = 5  # 0b0101
n = 3  # 0b0011
print("Bitwise AND:", m & n)  # 0b0001 (1)
print("Bitwise OR:", m | n)   # 0b0111 (7)
print("Bitwise XOR:", m ^ n)  # 0b0110 (6)
print("Bitwise NOT:", ~m)     # Inverts bits
print("Bitwise Left Shift:", m << 1)  # 0b1010 (10)
print("Bitwise Right Shift:", m >> 1) # 0b0010 (2)
