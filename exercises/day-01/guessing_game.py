secret_number = 42
tries = 6

while tries > 0:
	guess = int(input("Guess a number between 0 to 100: "))
	if guess == secret_number:
		print("You did it !!!! AWESOME")
		break
	elif guess > secret_number:
		print("guess a lower number")
		tries -= 1
		print(f"Remaining tries = {tries}")
	else:
		print("guess a higher number")
		tries -= 1
		print(f"Remaining tries = {tries}")

if  tries == 0:
	print("Game Over")