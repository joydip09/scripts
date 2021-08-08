#!$PREFIX/bin/bash

echo "This is a simple password generator.
You can generate password of any length with this tool"
read -p "Enter the length of your password: " passl

echo "To generate password with hexadecimal algorithm type hex.
To generate password with base64 algorithm type base64."
echo "To know the difference between hex & base64 visit README.md"
read -p "Which algorithm you wanna use?: " alg

read -p "How many passsword you wanna generate?: " itm

for p in $(seq 1 $itm);
do
	openssl rand -$alg 48 | cut -c1-$passl
done

echo "Thanks for using my tool"