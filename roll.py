from random import randint

def roll():
	while True:
		die = randint(1,6)
		print die
		answer = raw_input("Roll again?\n")
		if answer == "y": # lazy
			roll()
		else:
			quit()
roll()
