import random
import sys

if len(sys.argv) != 3:
	print("rolldice.py [dice count] [dice size]")
	print("For usage with GURPS type in 'rolldice.py 3 6'")
	exit(1)

dice_size = int(sys.argv[2])
dice_count = int(sys.argv[1])
sum = 0

for i in range(dice_count):
	roll = random.randint(1, dice_size)
	print(roll)
	sum = sum + roll
print("sum: "+str(sum))


