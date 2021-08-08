num = [0,1,2,5,6,2,5,7,3, 2,2,3,4,3,4,4,2,7,8,8,8,9,0,0,0,3,5,4,5,6]
nums=[range(10)]
if 9 in num:
	print("yeah")
num [4] = 8 #sets the 5th[4] component's value 8
print (num[4]) #prints 5th[4] component on list
if 8 in num:
	print ("yes") #command in checks if the component is in the list
if 12 not in num:
		print ("no") #command not in checks if the component is not in the list
num.insert (0,4) #insets 4 in the 1st[0] place in the list
num.append (4) #inserts 4 in the end of the list
print (len(num)) #counts the number of components in the list
print (num.index(4)) #finds 1st occurance of 4 in the list
print (max(num)) #finds the max value in the list
print (min(num)) #finds the minimun value in the list
def func():
	print("That was list operation")
func()