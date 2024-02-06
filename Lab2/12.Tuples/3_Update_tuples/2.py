# Remove items from a tuple

# We can use the same workaround as we used for changing and adding tuple items:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Or you can delete the tuple completely:
anothertuple = ("apple", "banana", "cherry")
del anothertuple
print(anothertuple) #this will raise an error because the tuple no longer exists