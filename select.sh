#!/bin/bash

echo "Choose option"
ch="Bla Dla"
select dj in $ch; do
	case $dj in
		[1])
			echo "Bla Bla Bla"
			;;
		[2])
			echo "Dla Dla Dla"
			;;
		*)
			echo "Invalid"
			;;
	esac
done
exit 0
