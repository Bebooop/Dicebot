#!/bin/bash
counter=1
sum=0
while [ $counter -le $2 ]
do
	roll=$((+RANDOM % $1 + 1))
	echo $roll
	sum=$(($sum + $roll))
	((counter++))
done

echo sum is $sum
