"""

names = []

for _ in range(3):
    names.append(input("what's your name? "))

for name in sorted(names):
    print(f"hello, {name}")
     
"""

# open function
"""

name = input("what's your name ? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()   

"""

# with function
"""
name = input("what's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n") 
 """


"""
with open("names.txt", "r") as file:  # r stands for read
    lines = file.readlines()

for line in lines:
    print("hello,", line) 
    """

# sorted     (used for sorting the names alphabetically)
"""

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):   # if we write reverse=true with names in sorted then we will get the names in descending order
    print(f"hello, {name}")

    """ 

# dot csv (.csv) comma seperated values

# files name csv they have comma which seperates values with commas





