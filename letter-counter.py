#!/bin/python

text = input()
dict = {}
for i in text:

    if i in dict: 

        dict[i] += 1

    else: 

        dict[i] = 1
print (dict)

