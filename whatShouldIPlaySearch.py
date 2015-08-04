#what should I play search class
#
import os 
from flask import Flask, url_for, json

#get json for the games
#
def getJSONForWhatShouldIPlayListOfGames():
	SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
	json_url = os.path.join(SITE_ROOT, "static/data", "gamesToPlay.json")
	data = json.load(open(json_url))
	return data

#what should I play search method
#
def whatShouldIPlaySearch(passedGameTimeMax, passedGenre, passedNumberOfPlayers, passedGameMechanic, passedRulesDifficulty, passedNoOpString):
	
	gameData = getJSONForWhatShouldIPlayListOfGames()
	
	listOfPlayAbleGames = []
	
	#hinky until we get a better way
	#
	for game in gameData:

		addGame = False
		
		if((int(game["playTimeMax"]) <= passedGameTimeMax) and (passedGenre == passedNoOpString or game["genre"] == passedGenre)  and (( passedNumberOfPlayers >= int(game["numberOfPlayersMin"])) and (int(game["numberOfPlayersMax"]) >= passedNumberOfPlayers)) and (passedGameMechanic == passedNoOpString or game["gameMechanic"] == passedGameMechanic) and (passedRulesDifficulty == passedNoOpString or game["rulesDifficulty"] == passedRulesDifficulty)):
			addGame = True			
		
		if(addGame):
			listOfPlayAbleGames.append(game)
			print game["gameTitle"]
			
	return listOfPlayAbleGames
