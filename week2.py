#1 while (loop)(can be used for repetetion)
#mewoing 3 times
""" i = 0
while i < 3:
    print("meow")
    i += 1  # means i=i+1   """


#2 for loop

"""for i in [0,1,2]:  #we used list in []
    print("meow")  # or we can do it ass """


""" for i in range(100):  # range function
    print ("meow")  """  

#OR WE CAN DO IT AS

"""   print("meow\n" * 3, end="") """   # end="" for ending without \n  


#taking input

"""while True:    # used when we have to do something again and again
    n = int(input("what's n? "))
    if n < 0:
        continue    #to continue the code
    else:
        break       # to break the code

for _ in range (n):
    print("meow")   """  #to run code first remvoe """

# another way

"""def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n=int(input("what's n: "))
        if n > 0:
            break
    return n 
    

def meow(n):
    for _ in range(n):
        print("meow")
    
main()   """


# 3 List

""" students = ["hermione", "harry", "ron"]"""

""" print(students[0])  # 0 1 2  means index or oth location in list
print(students[1])
print(students[2])  """
 
# can also be done as 

"""for student in students:
    print(student) """

#4 len (length of list)

"""students = ["hermione", "harry", "ron'"]

for i in range(len(students)):
    print(i+1, students[i]) """


#5 dict(dictionary in list)

"""
students = {
    "hermione": "gryffindor",
    "harry": "gryffindor",
    "ron": "gryffindor",
    "draco": "slytherin",   
}

for student in students:

    print(student,students[student], sep=", ")

    """

 
#list of dict.

students=[
    {"name" : "Hermione", "house": "gryffindor","patronus":"otter"},
    {"name": "harry" , "house": "gryffindor","patronus": "stag"},
    {"name": "ron", "house": "gryffindor", "patronus": "jack russel terrier"},
    {"name": "draco", "house": "slytherin","patronus": None}  # -> none is a keyword we can use for none(nothing)

]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=",")    


#super mario example(to build a 3x3 square)


