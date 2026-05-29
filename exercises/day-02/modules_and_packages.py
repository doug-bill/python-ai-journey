import sys
print (sys.executable)

import math #By using import "package_name" you can import user created packages with useful funcitons to help in your program
print(math.sqrt(16)) # sqrt to calculate the square root of a number.

result = math.pow(2,3) #pow for potency/power

#importing with nickname/ aliases 

import math as m 
print(m.sqrt(16))

# You can also import everything from the package at once 
# but is often not recommeded cuz it can give erros when there are functions with similar names in your code base.

from math import *
print(pi) # This works here but if you have a function or another thing named pi the code won't know what are you refering to.

from pyfiglet import figlet_format

text = figlet_format("Hi there, Hello")
print(text)

# With this litte exercise I could test importing some packages using python,
# And also had to resolve the conflit to having 2 pythons installs on my system so I had to change the default on bash and on Vscode in order for the figlet
# import to work.

