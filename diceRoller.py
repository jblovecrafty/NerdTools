#dice roller class
#
import random
from flask import Flask

#random dice roller
#
def rollDice(passedNumberOfDice, passedDiceType):
	
	#list of dice results
	#
	listOfDiceResults = []
	
	#loop thru the passedNumberDice 
	#
	for i in xrange(0, passedNumberOfDice):
	
		randomNumber = 0
		
		#now roll number and add to list
		#
		randomNumber = random.randint(1, passedDiceType)

		listOfDiceResults.append(randomNumber)
	
	#return list
	#
	return listOfDiceResults