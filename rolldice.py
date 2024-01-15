import random
import sys

dice_size = int(sys.argv[1])
dice_count = int(sys.argv[2])
sum = 0

for i in range(dice_count):
	roll = random.randint(1, dice_size)
	print(roll)
	sum = sum + roll
print("sum: "+str(sum))
