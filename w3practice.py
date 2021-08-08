import datetime
j=datetime.datetime.now()
print(j)

print("Hello Vau")

a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
txt=str("{} is greater than {}")
if a>b:
	print(txt.format(a,b))
else: pass

import random
def dice():
	print(random.randrange(1,6)) #dice function
x=str(input("Do you want to roll dice? (Y/N)"))
if x=="y" or x=="Y":
	dice()
elif x=="n" or x=="N":
	print("Puk U \n Bye")
else:
	print("Invalid option")

fruits=["apple","banana","orrange","pineapple","grape"]
import json #learning JSON via Python
def frt():
	print(fruits)
y=str(input("Enter your favourite fruit's name: "))
if y in fruits:
	print("Congrats!! Your favourite fruit is also my favourite.")
else:
	print("Sorry!! Your favourite fruit is not my favourite.My favourites are:")
	print(json.dumps(fruits))
	

i=0
while i<=10:
	print("While Loop")
	i+=1

def coco(name):
	print("I am "+name+" Chowdhury")
coco("Joydip")

country=input("Where are you from? \n ")
txt4u="Ooh {} !! I am from Bangladesh"
print(txt4u.format(country))

g=open("file:////storage/emulated/0/My/Web-Design/pjp.html","r")
print(g.read())