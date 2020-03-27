import time
import numpy as np
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

class Name:
    def __init__(self, value):
        self.value = value
        self.next = None 
        self.prev = None

    def insert(self,value):
        self.next = Name(value)

first_name = Name(names_1[0])
this_name = first_name
i = 1
while i != len(names_1):
    this_name.insert(names_1[i])
    this_name = this_name.next
    i +=1 
current_name = first_name
q = 0
while q != len(names_2):
    if current_name.value in names_2:
        duplicates.append(current_name.value)
    current_name = current_name.next
    q += 1

print(duplicates)
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

#The best time I was able to accomplish with the set built-in function was around 0.008 seconds.
 duplicates = set(names_1) & set(names_2)
