# 1 TRY, EXCEPT 
"""
try:
    x=int(input("what's x: "))
    print(f"x is {x}")

except ValueError:
    print("x is not integer")  
"""  

# 2 NAME ERROR



# 3 ELSE  

"""
try:
    x=int(input("what's x: "))
    
except ValueError:
    print("x is not integer")

else:
    print(f"x is {x}") 

"""

# 4 REPROMPTING,BREAK
""" 
while True:
    try:
        X=int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {X}")

"""

# 5 GET_INT
"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what's x? "))
        
        except ValueError:
            print("x is not an integer")
    
    
main()

"""

# 6 PASS
"""
def main():
    x=get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("what's x? "))
        except ValueError:
            pass             # used just to pass day nothing just pass...

main()

"""

