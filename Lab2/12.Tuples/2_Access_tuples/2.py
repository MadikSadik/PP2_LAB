thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# The search will start at index 2 (included) and end at index 5 (not included).
print(thistuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":
print(thistuple[:4])

# This example returns the items from "cherry" and to the end:
print(thistuple[2:])

# This example returns the items from index -4 (included) to index -1 (excluded)
print(thistuple[-4:-1])