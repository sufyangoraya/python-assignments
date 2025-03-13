# Lesson 05: Control Flow & Loops

# Conditional Statements
# Using if-elif-else to compare two numbers
x = 10
y = 20
if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

# Loops
# For Loop - Iterates through a range of numbers from 0 to 4
for i in range(5):
    print("Iteration:", i)

# While Loop - Runs while count is less than 5
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Nested Loop - Loop inside another loop
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Lesson 06: Lists, Tuples & Dictionary

# List - Ordered, mutable collection
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
my_list.append(6)  # Adding an element to the list
print("After Append:", my_list)
my_list.remove(3)  # Removing an element from the list
print("After Remove:", my_list)

# Tuple (Immutable) - Ordered but cannot be changed after creation
my_tuple = (10, 20, 30)
print("Tuple:", my_tuple)

# Dictionary - Key-value pairs
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", my_dict)
print("Name:", my_dict["name"])  # Accessing value using a key
my_dict["age"] = 26  # Updating value in dictionary
print("Updated Dictionary:", my_dict)

# Lesson 07: Set & Frozenset

# Set - Unordered collection of unique items
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)
my_set.add(6)  # Adding an element to the set
print("After Add:", my_set)
my_set.remove(2)  # Removing an element from the set
print("After Remove:", my_set)

# Frozenset (Immutable Set) - Similar to a set but cannot be changed
my_frozenset = frozenset([1, 2, 3, 4, 5])
print("Frozenset:", my_frozenset)

# Set Operations - Demonstrating union, intersection, difference, and symmetric difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1.union(set2))  # Combines both sets, removing duplicates
print("Intersection:", set1.intersection(set2))  # Common elements in both sets
print("Difference:", set1.difference(set2))  # Elements in set1 but not in set2
print("Symmetric Difference:", set1.symmetric_difference(set2))  # Elements in either set but not in both
