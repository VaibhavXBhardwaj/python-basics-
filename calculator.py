#1 int
"""  x = int(input("what's x? "))
y = int(input("what's y? "))

print(x+y)  """
# it can be '-' '/' '*' '%'


#2 float
 
"""  x=float(input("whats x? "))
y=float(input("what's y? "))

print(x+y)  """


#rounded result
"""  x= float(input("whats x?"))
y= float(input("whats y?"))

z= round(x+y)   # or print(round(x+y))
print(z)    """


# using return function in program
def main():
    x= int(input("what's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n    # we can use pow(for power) or "**" for using power)

main() 