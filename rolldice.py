import random
import sys

def printusage():
	print("rolldice.py [dice count] [dice size]")
	print("For usage with GURPS type in 'rolldice.py 3 6'")
	print("Please use whole, positive numbers")

if len(sys.argv) != 3:
	printusage()
	exit(1)

if sys.argv[1] == "hello":
	print("Hello!")
	print("Please insert dice!")
	exit(1)

dice_size = 0
dice_count = 0
sum = 0

try: 
	dice_size = int(sys.argv[2])
	dice_count = int(sys.argv[1])
except:
	printusage()
	exit(1)

if dice_size < 1:
	printusage()
	exit(1)

if dice_count < 1:
	printusage()
	exit(1)

for i in range(dice_count):
	roll = random.randint(1, dice_size)
	print(roll)
	sum = sum + roll
print("sum: "+str(sum))


