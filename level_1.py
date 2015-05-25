import sys

userInput = sys.stdin.readline()

while userInput is not "":
	sys.stdout.write("Server says: " + userInput + "\n")
	sys.stdout.flush()
	sys.stderr.write("Server says: " + userInput + "\n")
	userInput = sys.stdin.readline()

'''
for string in sys.stdin:
	sys.stdout.write("Server says: " + string)
'''
