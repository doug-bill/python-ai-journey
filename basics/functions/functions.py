#Functions in python are really simple to create we need to use def( definition) 
# to define the method/function that we are creating and the amount of arguments 
# we want this method to receive. to close this line and start 
# the function we need the “ : ” otherwise it won’t work.

#There is no need for “end” like in Ruby, just have all the code that belongs
# to the method/function indented with 2 tabs below the function and to end 
# and just have the next code without indentation.

def greetings(name):# you can also create a function that don't receive an argument.
		return f"Hello, {name}!"
		
print(greetings("Douglas"))

#Python already got internal methods/functions for simple math but this is just an example.
def sum(a,b):
		c  = a + b
		return c
		
resultado = (sum(1,2))
print(resultado)

def sub(a,b):
		return a - b

int1 = int(input("Type an interger number!"))
int2 = int(input("Type another interger number!"))
result_sum = sum(int1, int2)
result_sub = sub(int1,int2)

print(f"The sum is: {result_sum} and the subtraction is {result_sub}") 