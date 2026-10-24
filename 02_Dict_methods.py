marks = {
    "Zeyan": 70,
    "Meezan": 80,
    "Fahad": 100,
    0: "Harry"
}
d = {} #empty dictionary

print(marks.items()) #prints all the items of the dictionary
print(marks.keys()) #prints all the keys of the dictionary
print(marks.values()) #prints all the values of the dictionary

print(len(marks))

marks.update({"Meezan": 85, "Aman":50}) #Update by either changing a value or adding a new key and value. 
print(marks) #dictionary are mutuable

print(marks.get("Gojo")) #Prints "None" if the key does not exist. 

#print(marks.pop("Aman")) #returns the key value and removes the specified key

#marks.clear()

print(marks.copy()) #Returns a shallow copy of the dictionary.

print(marks.popitem()) #Removes and returns the last inserted key-value pair as a tuple