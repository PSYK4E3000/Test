import copy
# Initialize list with numbers 2-10
spam = [2, 4, 6, 8, 10]

# Assign value to index 2
spam[2] = "hello"

# Print the list
print(spam)

# Initialize list with strings
spam = [ "a", "b", "c", "d" ]

# Calculate the result
result = int(int("3" * 2) / 11)
print(result)

# Print the element at result
print(f"{spam[int(result)]}")

# Print the last element
print(spam[-1])

# Print the first two elements
print(spam[:2])

##############################

# Initialize list with mixed data types
bacon = [3.14, "cat", 11, "cat", True]

# 1. Find the index of the first occurrence of "cat"
result = bacon.index("cat")
print(result)

# 2. Append 99 to the end of the list
bacon.append(99)
print(bacon)

# 3. Remove the first occurrence of "cat" from the list
bacon.remove("cat")
print(bacon)

# 4. Insert "Super cat" at index 0
bacon.insert(0, "Super cat")
print(bacon)

# 5. Delete the element at index 0
del bacon[0]
print(bacon)

# 6. Create a tuple with a single element (note: requires trailing comma)
tuplita = (42,)
print(tuplita)

# 7. Convert list to tuple and back to list
spam_tuplita = tuple(spam)
print(spam_tuplita)

spam_tuplita = list(spam_tuplita)
print(spam_tuplita)

# 8. Demonstrate shallow copy vs deep copy
# Shallow copy: creates a new list but references the same objects
new1_list = copy.copy(spam)
new1_list[0] = "Experimental: Copy!"
print(new1_list)

# Deep copy: creates a new list with new copies of all objects
new2_list = copy.deepcopy(spam)
new2_list[0] = "Experimental: DeepCopy!"
print(spam, new2_list)