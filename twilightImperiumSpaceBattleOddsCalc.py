#Calculate the odds for a space battle given a fleet and number of hits in Twilight Imperium
#
import os 
from operator import itemgetter
from decimal import *
from flask import Flask, url_for, json

#decimal precision
#
getcontext().prec = 1

#constants for the odds of various ships in Twilight Imperium
#
dreadNoughtOdds = .6
warSunOdds = .8
crusierOdds = .4
carrierOdds = .2
destroyerOdds = .2
fighterOdds = .2

#number of hits per ship
#
dreadNoughtHits = 1
warSunHits = 3
crusierHits = 1
carrierHits = 1
destroyerHits = 1
fighterHits = 1

def calculateBattleOdds(passedNumberOfDreadnoughts, passedDreadNoughtBonus, passedNumberOfWarSuns, passedWarSunBonus, passedNumberOfCruisers,
						passedCruiserBonus, passedNumberOfCarriers, passedCarrierBonus, passedNumberOfDestroyers, passedDestroyerBonus,
						passedNumberOfFighters, passedFighterBonus, passedNumberOfHitsNeeded):

	odds = 1

	#first get number of hits needed
	#
	totalPotentialHits = passedNumberOfDreadnoughts + (passedNumberOfWarSuns * warSunHits) + passedNumberOfCruisers + passedNumberOfCarriers + passedNumberOfDestroyers + passedNumberOfFighters 
	
	if(totalPotentialHits < passedNumberOfHitsNeeded):
		return 0
	
	fleetOddsList = buildOddsList(passedNumberOfDreadnoughts, passedDreadNoughtBonus, passedNumberOfWarSuns, passedWarSunBonus, passedNumberOfCruisers,
						passedCruiserBonus, passedNumberOfCarriers, passedCarrierBonus, passedNumberOfDestroyers, passedDestroyerBonus,
						passedNumberOfFighters, passedFighterBonus, passedNumberOfHitsNeeded)

	hitCount = 0

	for k in fleetOddsList:
		if(k[2] > 0 and (passedNumberOfHitsNeeded > hitCount)):
			for x in range(0, k[2]):
				if(passedNumberOfHitsNeeded > hitCount):
					odds = (odds * k[1])
					hitCount = hitCount + 1

	Decimal(odds)
	output = round(odds,2)
	return output


def calculateOddsOfAllHitting(passedNumberOfDreadnoughts, passedDreadNoughtBonus, passedNumberOfWarSuns, passedWarSunBonus, passedNumberOfCruisers,
						passedCruiserBonus, passedNumberOfCarriers, passedCarrierBonus, passedNumberOfDestroyers, passedDestroyerBonus,
						passedNumberOfFighters, passedFighterBonus, passedNumberOfHitsNeeded):

	odds = 1

	fleetOddsList = buildOddsList(passedNumberOfDreadnoughts, passedDreadNoughtBonus, passedNumberOfWarSuns, passedWarSunBonus, passedNumberOfCruisers,
						passedCruiserBonus, passedNumberOfCarriers, passedCarrierBonus, passedNumberOfDestroyers, passedDestroyerBonus,
						passedNumberOfFighters, passedFighterBonus, passedNumberOfHitsNeeded)

	for k in fleetOddsList:
		if(k[2] > 0):
			for x in range(0, k[2]):
				odds = (odds * k[1])

	Decimal(odds)
	output = round(odds,2)
	return output




def buildOddsList(passedNumberOfDreadnoughts, passedDreadNoughtBonus, passedNumberOfWarSuns, passedWarSunBonus, passedNumberOfCruisers,
						passedCruiserBonus, passedNumberOfCarriers, passedCarrierBonus, passedNumberOfDestroyers, passedDestroyerBonus,
						passedNumberOfFighters, passedFighterBonus, passedNumberOfHitsNeeded):
	#starting from the best odds (with bonus) start adding up..once done matching ship to hits stop
	#
	dreadNoughtTotalOdds = dreadNoughtOdds + (passedDreadNoughtBonus * .1)
	warSunTotalOdds = warSunOdds + (passedWarSunBonus * .1)
	crusierTotalOdds = crusierOdds + (passedCruiserBonus * .1)
	carrierTotalOdds = carrierOdds + (passedCarrierBonus * .1)
	destroyerTotalOdds = destroyerOdds + (passedDestroyerBonus * .1)
	fighterTotalOdds = fighterOdds + (passedFighterBonus * .1)

	#now build and sort a dictionary so we can loop thru it
	#
	fleetOddsList  = [('Dreadnoughts', dreadNoughtTotalOdds, passedNumberOfDreadnoughts), ('Warsuns', warSunTotalOdds, (passedNumberOfWarSuns* warSunHits)), ('Cruiser', crusierTotalOdds, passedNumberOfCruisers), ('Carrier', carrierTotalOdds, passedNumberOfCarriers), ('Destroyer', destroyerTotalOdds, passedNumberOfDestroyers), ('Fighter', fighterTotalOdds, passedNumberOfFighters)]
	fleetOddsList.sort(key=lambda tup: tup[1],reverse=True)

	print fleetOddsList
	return fleetOddsList 



