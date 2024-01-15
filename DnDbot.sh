#!/bin/bash
roll=$((RANDOM % $1 + 1))
echo $roll
if [[ "$roll" == "1" ]]
then
	cowsay -f hellokitty Shits Fucked
fi
if [[ "$roll" == "$1" ]]
then
	cowsay -f stegosaurus Hell Yea
fi
