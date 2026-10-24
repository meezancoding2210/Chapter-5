s = {1, 13, 32, 5, 5, "Meezan"}

print(len(s)) #does not repeat any values

s.add(566) #Adds a single element to the set. If the element is already there, the set remains unchanged.
print(s, type(s))

s.remove(32) #Removes a specified element from the set. Raises a KeyError if the element is not found.
print(s)

s.discard(0) #Removes a specified element from the set. Unlike remove(), it does not raise an error if the element is missing.
print(s)

print(s.pop()) #Removes and returns an arbitrary (random) element from the set.

#s.clear()

s.add(6)
print(s) #sets are mutuable