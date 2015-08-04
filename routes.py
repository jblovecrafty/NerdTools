from flask import Flask, render_template, redirect, request, flash
from forms import  TwilightImperiumRaceRandomizer
from forms import  DiceRollerForm
from forms import TwilightImperiumBattleCalculator
from forms import DuneDiceRollerForm
from forms import WhatShouldIPlay

import twilightImperium
import whatShouldIPlaySearch
import wtfFormUtils
import diceRoller
import shipName
 
app = Flask(__name__)      
app.config.from_object('config')
 
@app.route('/')
def home():
  return render_template('home.html')

#Twilight Imperium Race Picker
#
@app.route('/twilightImperiumRaceRandomizer', methods=['GET', 'POST'])
def twilightImperiumRaceRandomizer():
	form = TwilightImperiumRaceRandomizer(request.form)
	if request.method == "POST" and form.validate_on_submit():
		
		#ok lets get the list of players
		#
		listOfTIPlayers = wtfFormUtils.getListOfFormData(form)
		
		#now lets get those player's races
		#	
		listOfTIPlayersAndRaces =  twilightImperium.getRandomizedRacesForTwilightImperium(listOfTIPlayers)
		
		#now send that info to the correct template
		#
		return render_template('twilightImperiumRaceRandomizerResults.html', listOfPlayers = listOfTIPlayersAndRaces)
	elif request.method == 'GET':
		print 'Get'
		return render_template('twilightImperiumRaceRandomizerForm.html', form=form)
	else:
		flash('At Least three players are required.')
		return render_template('twilightImperiumRaceRandomizerForm.html', form=form)
		
#Twilight Imperium Battle Dice Roller
#
@app.route('/twilightImperiumBattle', methods=['GET', 'POST'])
def twilightImperiumBattleCalculator():
	form = TwilightImperiumBattleCalculator(request.form)
	if request.method == "POST" and form.validate_on_submit():
		print 'OK we are good'
		#print wtfFormUtils.getListOfFormData(form)
		return 'OK'
		
	elif request.method == 'GET':
		print 'Get'
		return render_template('twilightImperiumBattlePart1.html', form=form)
	
	else:
		print 'OK failing validation'
		print form.errors
		print form.defenderDreadNoughtBonus
		return 'OK'
		
#dice roller
#		
@app.route('/diceRoller', methods=['GET', 'POST'])
def diceRollerTask():	
	form = DiceRollerForm(request.form)
	if request.method == "POST":
		
		#ok roll them dice
		#	
		listOfDiceResults = diceRoller.rollDice(int(form.numberOfDice.data), int(form.diceType.data))
		
		#now send that info to the correct template
		#
		return render_template('diceRollerResults.html', listOfResults = listOfDiceResults, totalResults = sum(listOfDiceResults))
	elif request.method == 'GET':
		print 'Get'
		return render_template('diceRollerForm.html', form=form)
		
#create culture ship names
#		
@app.route('/cultureShipName', methods=['GET', 'POST'])
def cultureShipNameTask():	
	cultureShipName = shipName.cultureShipName()
	if request.method == "POST":
		return render_template('cultureShipNameMaker.html', cultureShipNameResult = cultureShipName)
	elif request.method == 'GET':
		return render_template('cultureShipNameMaker.html', cultureShipNameResult = cultureShipName)
		

#Dune dice game roller
#
@app.route('/duneDiceRoller', methods=['GET', 'POST'])
def duneDiceRollerTask():
	form = DuneDiceRollerForm(request.form)
	
	#ugly if statements FIX THIS SON
	#
	if(form.factionDice1Freeze.data != True):
		form.factionDice1 = diceRoller.rollDice(1, 6)[0]
		form.factionDice1Hidden.data = form.factionDice1
	else:
		form.factionDice1 = form.factionDice1Hidden.data
		
	if(form.factionDice2Freeze.data != True):
		form.factionDice2 = diceRoller.rollDice(1, 6)[0]
		form.factionDice2Hidden.data = form.factionDice2
	else:
		form.factionDice2 = form.factionDice2Hidden.data
	
	if(form.factionDice3Freeze.data != True):
		form.factionDice3 = diceRoller.rollDice(1, 6)[0]
		form.factionDice3Hidden.data = form.factionDice3
	else:
		form.factionDice3 = form.factionDice3Hidden.data
			
	if(form.factionDice4Freeze.data != True):
		form.factionDice4 = diceRoller.rollDice(1, 6)[0]
		form.factionDice4Hidden.data = form.factionDice4
	else:
		form.factionDice4 = form.factionDice4Hidden.data
			
	if(form.kanlyDiceFreeze.data != True):
		form.kanlyDice = diceRoller.rollDice(1, 6)[0]
		form.kanlyDiceHidden.data = form.kanlyDice
	else:
		form.kanlyDice = form.kanlyDiceHidden.data
	
	if(form.spiceDiceFreeze.data != True):
		form.spiceDice = diceRoller.rollDice(1, 6)[0]
		form.spiceDiceHidden.data = form.spiceDice
	else:
		form.spiceDice = form.spiceDiceHidden.data
			
	if(form.regionDiceFreeze.data != True):
		form.regionDice = diceRoller.rollDice(1, 6)[0]
		form.regionDiceHidden.data = form.regionDice
	else:
		form.regionDice = form.regionDiceHidden.data
	
	if request.method == "POST":
		return render_template('duneDiceRoller.html', form=form)
	elif request.method == 'GET':
		return render_template('duneDiceRoller.html', form =form)

#what should I play
#	
@app.route('/whatShouldIPlay', methods=['GET', 'POST'])
def whatShouldIPlay():
	form = WhatShouldIPlay(request.form)
	if request.method == "POST":
		
		#now send that info to the correct template
		#
		
		#ok right now we are going to pass in the objects and get a set of games to play the ugly way
		#
		listOfGame = whatShouldIPlaySearch.whatShouldIPlaySearch(int(form.timeSpanToPlay.data), form.themeToPlay.data, int(form.numberOfPlayer.data), form.gameMechanics.data , form.levelOfRulesDifficulty.data, "dontCare")
		
		return render_template('whatShouldIPlayResults.html', listOfGames = listOfGame)
	else:
		print 'Get'
		return render_template('whatShouldIPlayForm.html', form = form)
 
if __name__ == '__main__':
  app.run(debug=True)