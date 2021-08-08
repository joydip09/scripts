#!/bin/bash

echo "To ping an IP type ip
To scan a Subnet type subnet" 
echo "What do you wana do? : "
read cnfrm

case "$cnfrm" in
	[sS][uU][bB][nN][eE][tT])
		echo "Enter the subnet: "
		read sb
		for ipw in $(seq 1 254); do
		ping -c 1 $sb.$ipw 
		done
		echo "Thanks for using my tool"
		;;
	[iI][pP])
		echo "Enter your ip: "
		read ip
		ping -c 1 $ip
		echo "Thanks for using my tool"
		;;
	*)
		echo "Invalid Options"
		;;
esac
