#Store a list of first names. Count the occurrences of ‘a’ within the list.
fNames = ["syed", "adam", "philip", "narayanan"]
count = 0
for x in fNames:
 for y in x:
    if y == 'a':
        count +=1
print("’a’ has occurred ", count, " times.")
