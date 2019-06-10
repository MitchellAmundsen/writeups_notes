from sys import exit
import random

calm = False

def begin():
	print "You're walking down an alley."
	print "A man in a trenchcoat approaches you."
	print "1) Run away"
	print "2) Talk to him"
	print "3) Pull out a weapon"

	choice = raw_input("> ")

	if choice == "1":
		print "You trip on the flat ground and break your neck."
		exit(0)
	elif choice == "2":
		conversation()
	elif choice == "3":
		"You have a different weapon in each of your 4 pockets."
		"Which pocket do you choose?"
		choice2 = int(raw_input("> "))
		if choice2 > 4:
			print "You miss your pocket"
			conversation()
		else:
			battle(choice2)
	else:
		print "You freeze up and the stranger stabs you."

def conversation():
	"The man wants to play Rock, Paper, Scissors."
	game = "tie"

	gamechoice = ["rock", "paper", "scissors"]
	while game == "tie":
		strangerchoice = int(random.random()*3)
		strangerchoiceword = gamechoice[strangerchoice]
		print "1) Rock"
		print "2) Paper"
		print "3) Scissors"
		
		choice = int(raw_input("> ")) - 1
		if choice > 2:
			"You do nothing and get rekt"
			exit(0)
		else:
			choiceword = gamechoice[choice]

		if choice == strangerchoice:
			game = "tie"
		elif (strangerchoice != 0 or choice != 2) and choice > strangerchoice:
			game = "win"
		else:
			game = "lose"

		print "You chose %s and the stranger chose %s... You %s" % (choiceword, strangerchoiceword, game)

begin()


