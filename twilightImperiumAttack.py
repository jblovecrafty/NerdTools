#Twilight Imperium Battle Class
#
import random
from flask import Flask
import diceRoller

#constants for to hit for various craft
#
dreadnoughtToHitBase = 5
carrierToHitBase = 9
cruiserToHitBase = 7
destroyerToHitBase = 9
warSunToHitBase = 3
fighterToHitBase = 9
soldierToHitBase = 8
pdfToHitBase = 6

#members for the attacker
#
attackerNumberOfDreadNoughts = 0
attackerDreadNoughtBonus = 0

attackerNumberOfCarriers = 0
attackerCarrierBonus = 0

attackerNumberOfCruisers = 0
attackerCruiserBonus = 0

attackerNumberOfDestroyers = 0
attackerDestroyerBonus = 0

attackerNumberOfWarSuns = 0
attackerWarSunsBonus = 0

attackerNumberOfFighters = 0
attackerFighterBonus = 0

attackerNumberOfSoldiers = 0
attackerSoldierBonus = 0

attackerNumberOfHits = 0

#memebers for the defender
#
defenderNumberOfPDS = 0
defenderPDSBonus = 0

defenderNumberOfDreadNoughts = 0
defenderDreadNoughtBonus = 0

defenderNumberOfCarriers = 0
defenderCarrierBonus = 0

defenderNumberOfCruisers = 0
defenderCruiserBonus = 0

defenderNumberOfDestroyers = 0
defenderDestroyerBonus = 0

defenderNumberOfWarSuns = 0
defenderWarSunsBonus = 0

defenderNumberOfFighters = 0
defenderFighterBonus = 0

defenderNumberOfSoldiers = 0
defenderSoldierBonus = 0

defenderNumberOfHits = 0

#base method to roll to hit
#
def rollToHit(passedChance, passedNumberOfRolls):
	
	listOfDiceRolls = diceRoller.rollDice(passedNumberOfRolls, 10)
	
	numberOfHits = 0
	
	#check if a list element is above a certain number
	#
	for i in xrange(0, listOfDiceRolls):
	
		if(listOfDiceRolls[i] >= passedChance):
			numberOfHits += 1
			
	return numberOfHits
	

def pdsRollToHit(passedNumberOfRolls, passedBonus):
	return rollToHit(pdfToHitBase-passedBonus, passedNumberOfRolls)
	
def destroyerRollToHit(passedNumberOfRolls, passedBonus)::
	return rollToHit(destroyerToHitBase-passedBonus, passedNumberOfRolls)

def dreadnoughtRollToHit(passedNumberOfRolls, passedBonus)::
	return rollToHit(dreadnoughtToHitBase-passedBonus, passedNumberOfRolls)
	
def carrierRollToHit(passedNumberOfRolls, passedBonus)::
	return rollToHit(carrierToHitBase-passedBonus, passedNumberOfRolls)
		
def cruiserRollToHit(passedNumberOfRolls, passedBonus)::
	return rollToHit(cruiserToHitBase-passedBonus, passedNumberOfRolls)
		
def warsunRollToHit(passedNumberOfRolls, passedBonus)::
	return rollToHit(warSunToHitBase-passedBonus, passedNumberOfRolls)
		
def fighterRollToHit(passedNumberOfRolls, passedBonus)::
	return rollToHit(fighterToHitBase-passedBonus, passedNumberOfRolls)	
		
def soldierRollToHit(passedNumberOfRolls, passedBonus)::
	return rollToHit(soldierToHitBase-passedBonus, passedNumberOfRolls)		
			
