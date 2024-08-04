#!/bin/bash

clear
echo "Welcome to the Interactive Story!"
echo "You find yourself in a dark forest. Do you go left or right?"
echo "Type left or right to choose your path."
read choice
if [ "$choice" == "left" ]; then
echo "You encounter a dragon. Do you fight or flee?"
echo "Type fight or flee to choose your action."
read action
if [ "$action" == "fight" ]; then
echo "You bravely fight the dragon and win!"
else
echo "You flee safely, but the adventure ends here."
fi
else
echo "You find a hidden treasure. Do you take it or leave it?"
echo "Type take or leave to choose your action."
read action
if [ "$action" == "take" ]; then
echo "You take the treasure and become rich!"
else
echo "You leave the treasure and continue your journey."
fi
fi
