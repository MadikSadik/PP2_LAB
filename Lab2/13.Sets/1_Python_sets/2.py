thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set can be any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# A set can contain different data types:
set4 = {"abc", 34, True, 40, "male"}

# From Python's perspective, sets are defined as objects with the data type 'set':
myset = {"apple", "banana", "cherry"}
print(type(myset))

# It is also possible to use the set() constructor to make a set.
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)