#!$PREFIX/bin/bash

echo "Hello World! " | lolcat -as 50
name="Joydip" #there can't be any whitespace among variables,=,values
echo "My name is $name" #to call a variable I have to use '$'

echo "Enter your full name: " #prompt for user input
read Fname Lname #reads user input differed by space
echo "Your first name is $Fname"
echo "Your last name is $Lname"

read -p "Enter your age: " age #prompt for user input and at last part declare the variable
echo "Your age is $age" 

if [ "$Fname" = "joydip" ]; #must give a whitespace after and before everything in conditon and put a ; at the end 
then 
	echo "Welcome Joydip" | lolcat -as 10 #whitespace is not neccessary
else
	echo "Welcome $Fname"
fi #ends if conditon

for hero in $(cat hero.txt); do
	echo "Marvel heroes are $hero"
done