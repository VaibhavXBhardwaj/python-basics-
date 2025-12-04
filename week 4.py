# MODULES

# IMPORT
"""
import random
coin = random.choice(["Heads","Tails"])   # random.choice is a pre-defined function which can be foun on python official website
print(coin)

"""

# FROM (KEYWORD)
"""
from random import choice
coin = choice(["Heads", "Tails"])
print(coin)

"""

# random.randit(a,b)  (predefined fxn from website)
"""

import random
number = random.randint(1,10)
print(number)

"""
# random.shuffle(x)
"""

import random
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card) 

"""

# STATISTICS
"""

import statistics
marks = statistics.mean([90,100])
print(marks)

"""

# COMMAND-LINE ARGUMENT (FEATURE)
# 1 SYS
# sys.argv (variable) = argument vector
"""

import sys
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many Arguments")
else:
    print("Hello my name is", sys.argv)

"""

# Sys.exit
"""

import sys
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too few arguments")
else:                                       # we can remove else also and just write print statement 
     print("hello my name is", sys.argv[1])
 
"""

# SLICES (40:00)

# COWSAY
"""

import cowsay
import sys
if len(sys.argv)==2:
    cowsay.cow("hello " + sys.argv[1])

    """

# APIs, REQUESTS, JSON     # 1:02:38

 
 

