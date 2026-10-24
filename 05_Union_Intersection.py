s1 = {1,  45, 67, 81}
ss1 = {1,45}
s2 = {1, 7, 8 ,81, 78}

print(s1.union(s2)) 
print(s1.intersection(s2))

print(s1-s2) #prints s1-s2 or all the elements in s1 which are not in s2
print(s2.difference(s1)) #prints s2-s1 or all the elements in s2 which are not in s1

print(ss1.issubset(s1)) #ss1 is subset of s1
print(s1.issuperset(ss1)) #s1 is superset of ss1
print(s2.issuperset(ss1)) #False 