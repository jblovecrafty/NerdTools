import os 
import random
from flask import Flask, url_for, json

#
#handles the twilight imperium race randomization
#

#get json for the names and sets
#
def getJsonForTwilightImperiumRaces():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/data", "twilightImperiumRaces.json")
	data = json.load(open(json_url))
	return data

#function that takes list and returns a randomized race and name
#
def getRandomizedRacesForTwilightImperium(passedListOfPlayers):
	raceData = getJsonForTwilightImperiumRaces()
	listOfRacesAndPlayers = []
	listOfRacesAlreadyChosenByIndex = []
	randomIndexValue = 0
	
	for field in passedListOfPlayers:
		
		hasNewRandomBeenChosen = False
		
		#make sure we only get one choice of race for each player
		#
		while(not hasNewRandomBeenChosen):
			randomIndexValue = random.randint(0, len(raceData)-1)
			
			#ok only add to the list if we have a random
			if(not (randomIndexValue in listOfRacesAlreadyChosenByIndex)):
				raceChoice = raceData[randomIndexValue]["race"]
				raceImage = raceData[randomIndexValue]["imageName"]
				hasNewRandomBeenChosen = listOfRacesAlreadyChosenByIndex
				hasNewRandomBeenChosen = True
				
		playerAndRace = (raceChoice, raceImage, field)
		listOfRacesAlreadyChosenByIndex.append(randomIndexValue)
		listOfRacesAndPlayers.append(playerAndRace)

	return listOfRacesAndPlayers