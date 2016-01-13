#!/usr/bin/env python

import random

count = 0
check = 0
list = []
while check == 0:
	endCount = raw_input("How many words do you want to enter? ")
	try:		
		endCount = int(endCount)
		check = 1

	except:
		print "Incorrect value. Try again"	
		
while (count < endCount):
	word = raw_input("Please enter a word: ")
	if word not in list:
		list.append(word)
		count = count+1
	else:
		print "You have already entered this word. Try again"

#print list
rand = random.randint(0,endCount-1)
pyWord = list[rand]
#print pyWord
print "Ok now you have to guess which word out of all you have entered is my favourite"
myWord = raw_input("Make your guess ")
while myWord != pyWord:
	print "Wrong.Try again"
	myWord = raw_input("Make another guess ")

print "Good guess"

