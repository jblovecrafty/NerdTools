#sci fi ship name generator class
#
import random
from flask import Flask


#culture list of joins
#
listOfCulturePreFixes = ["The ", "", "A ", "For ", "So Much For ", "Just ", "Very Little ", "Only Slightly ", "I Thought ", "A Series Of ", "Never "]
listOfCultureJoins = [" and ", " of the ", " ", " and the ", " is ", " but ", " this ", " in ", " out of ", " of ", " or ", " or the ", " my ", " full of ", " makes ", " amidst ", " in the "]
listOfCultureNamePieces = ["Truth", "Autumn", "Pillar", "Winter", "Close", "Nervous", "Energy", "Prosthetic", "Conscience", "Determinist", "Eschatologist", "Irregular", "Apocalypse", "No More", "Mr. Nice Guy", "Profit", "Margin", "Revisionist", "Ends", "Invention", "Clear Air ", "Turbulence", "Hand", "Screw", "Loose", "Flexible", "Demeanor", "Just Read", "Instructions", "Limiting", "Factor", "Little", "Big", "Rascal", "Subtlety", "Unfortunate", "Conflict", "Evidence", "Youthful", "Indiscretion", "Gunboat", "Diplomat", "Zealot", "Prime", "Mover", "Testing", "Xenophobe", "Gravitas", "Civilian", "Applications", "Congenital", "Optimist", "Everything", "Grace", "Business", "Arbitrary", "Cantankerous", "Bent", "Space", "Monster", "Unlikely", "Explanation", "Strangers", "Boo", "Talk", "Credibility", "Issue", "Dramatic", "Exit", "Halation", "Effect", "Superposition", "Ambient", "Morality", "Report", "Voyage", "Perfidy", "Myself", "Synchronize", "Dogma", "Precise", "Unwitting", "Accomplice", "Undesirable", "Alien", "Neighbourhood", "Amenable", "Fate", "Character", "Forming", "Jaundiced", "Outlook", "Child", "Excuse", "Recent", "Convert", "Tactical", "Grace", "Steely", "Glint", "Highpoint", "Fair", "Adjuster", "Frank Exchange", "Gradient", "Ethics", "Mistake", "Honest", "Abode", "Fixed", "Sly", "Quietly", "Confident", "Wisdom", "Silence", "Yawning", "Angel", "Zero", "Null", "Gravitas", "Invented", "Here", "There", "Appeal", "Reason", "Logic", "Peace", "Plently", "Sober", "Counsel", "Sanctioned", "Parts", "Resistance", "Niceness", "Negotiation", "Germane", "Riposte", "Last", "First", "Determined", "Nonsense", "Awkward", "Awkward", "Pacifist", "Pride", "Liveware", "Phenomenon", "Transient", "Atmospheric", "Naughty", "Fortress", "Sense", "Madness", "Wit", "Folly", "Constraints", "Rubric", "Pressure", "Empiricist", "Vulgar", "Veracity", "Displacement"]



#culture ship name genarator class
#
def cultureShipName():
	
	#ship name result
	#
	shipNameResult = []
	shipNameResult.append(listOfCulturePreFixes[random.randint(0, len(listOfCulturePreFixes)-1)])
	
	#usimple weighted list
	#
	weightedListForNumberOfJoinsAndNames = [(1,.90), (2,.05), (3,.05)]
	
	numberOfNameJoinNames = weightedRandomNumbers(weightedListForNumberOfJoinsAndNames)
	
	#ship names can take the form of prefix + name piece + join + name piece or a chain of name piece + join + name piece
	#
	for i in xrange(0, numberOfNameJoinNames):
		
		#TODO: do something smart with plural name pieces and joins and a and an
		#
		
		#build the ship name
		#
		if(i != 0):
			shipNameResult.append(listOfCultureJoins[random.randint(0, len(listOfCultureJoins)-1)])
			
		shipNameResult.append(listOfCultureNamePieces[random.randint(0, len(listOfCultureNamePieces)-1)])
		shipNameResult.append(listOfCultureJoins[random.randint(0, len(listOfCultureJoins)-1)])
		shipNameResult.append(listOfCultureNamePieces[random.randint(0, len(listOfCultureNamePieces)-1)])
	
	#return name
	#
	return ''.join(shipNameResult)
	
#method for weighted random numbers needs to be a list of index weight pairings...MUST ADD UP TO 1
#
def weightedRandomNumbers(passedListOfTuples):
	
	#keep a running count of the percentage total 
	#
	runningPercentage = 0
	
	randomNumberChosen = random.random()
	
	for randomTuple in passedListOfTuples:
		 
		#first add the new percent to the runningPercentage
		#
		runningPercentage += randomTuple[1]
		
		if(randomNumberChosen <= runningPercentage):
			return randomTuple[0]
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
		