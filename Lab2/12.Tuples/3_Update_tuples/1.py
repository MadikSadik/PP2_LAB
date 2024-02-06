x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add items to tuple

#1 Convert into list
thistuple = ("apple", "banana", "cherry")
z = list(thistuple)
z.append("orange")
thistuple = tuple(z)
print(thistuple)

#2 Add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)