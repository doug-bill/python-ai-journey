# For Loops

# Range-based
for i in range(5):
	print(i)

# Iterating over list
fruits = ["apple","banana","Mango"]
for fruit in fruits:
	print(fruit)

# With index
for i, fruit in enumerate(fruits, 1):
	print(f"{i}: {fruit}")
 
 # While Loops
 
counter = 0
while counter < 5:
	print(counter)
	counter += 1
 
#**Ruby difference:**

# Python: `for item in collection`
# Ruby: `collection.each { |item| conditional }`
# Python uses `range()` instead of Ruby's `(1..5).each`
# No `loop do` construct in Python