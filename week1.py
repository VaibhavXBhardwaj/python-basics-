#1 if , else, elif
"""  x = int (input("what's x: "))  # could use float etc
y = int(input("what's y: "))

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

else:
    print("x is equal to y")   """

# 2 or
"""  x = int (input("what's x: "))  # could use float etc
y = int(input("what's y: "))

if x < y or x > y:
    print("x is not equal to y")

else:
    print("x is equal to y")  """ 


# 3 and  (using grading system code)
"""  score = int(input("score: "))

if score>= 90 and score<= 100:
    print("Grade: A")
elif score>=80 and score<=90:
    print("Grade: B")
else:
    print("Grade less then B")  """


# 4 parity 

""" x = int(input("what's x? "))

if x%2==0:
    print("x is even")
else:
    print("x is odd")  """ #the other way is down



"""def main():
    x=int(input("what's x? "))
    if is_even(x):
        print("even")
    else:
        print("odd")

def is_even(n): 
    if n%2==0:
        return True
    else:
        return False

main()   """
    

    # we can change whole line from LINE 54 TO 58 in one line as
    # return True  is n%2==0 else False  ((it would work perfectly))
    # we can also use : return % 2 == 0 ((it would also work))
     
# 5 match case

"""  name=input("what's your name: ")

match name:
    case "Harry"| "Hermione" | "ron":
        print("Gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("who?")  """

