#!/bin/bash

clear
echo "Welcome to the Advanced Interactive Story!"
echo "You find yourself in a dark forest. Do you go left or right?"
echo "Type left or right to choose your path."
read choice
if [ "$choice" == "left" ]; then
echo "You encounter a dragon. Do you fight, flee, or negotiate?"
echo "Type fight, flee, or negotiate to choose your action."
read action
if [ "$action" == "fight" ]; then
echo "You bravely fight the dragon and win!"
elif [ "$action" == "flee" ]; then
echo "You flee safely, but the adventure ends here."
else
echo "You negotiate with the dragon and become friends!"
fi
else
echo "You find a hidden treasure. Do you take it, leave it, or share it with a friend?"
echo "Type take, leave, or share to choose your action."
read action
if [ "$action" == "take" ]; then
echo "You take the treasure and become rich!"
elif [ "$action" == "leave" ]; then
echo "You leave the treasure and continue your journey."
else
echo "You share the treasure with a friend, and you both become rich!"
fi
fi
