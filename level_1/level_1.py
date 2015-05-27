import sys
import re

nextLevelPassword = "abc" #change this

sys.stdout.write("Welcome to The Network Game!\n")
sys.stdout.write("Try 'help'.\n")

sys.stdout.write("USER@TNG:LEVEL_1>")

userInput = sys.stdin.readline()

while userInput is not "":
	if re.match(r'^help|\?$', userInput):
		sys.stdout.write("help/?\t\t-\tshow help\n")
		sys.stdout.write("rules\t\t-\tshow rules\n")
		sys.stdout.write("nextlevel\t-\tgo to next level\n")
		sys.stdout.write("echo\t\t-\tsend input back\n")
		sys.stdout.write("quit/exit\t-\tdisconnect from the server")
	elif re.match(r'^rules$', userInput):
		sys.stdout.write("1) Do not distribute/seek passwords.\n")
		sys.stdout.write("2) Do not distribute/create/seek walkthroughs, tutorials, etc.")
	elif re.match(r'^nextlevel$', userInput):
		sys.stdout.write("The next level password is '" + nextLevelPassword + "'")
	elif re.match(r'^echo', userInput):
		sys.stdout.write("Server says: " + userInput[4:])
	elif re.match(r'^quit|exit$', userInput):
		break
	else:
		sys.stdout.write("Invalid command.")

	sys.stdout.write("\nUSER@TNG:LEVEL_1>")
	sys.stdout.flush()
	userInput = sys.stdin.readline()
