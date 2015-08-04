from flask.ext.wtf import Form
from wtforms import StringField
from wtforms import SelectField
from wtforms import IntegerField
from wtforms import BooleanField
from wtforms import HiddenField
from wtforms.validators import DataRequired
from wtforms.validators import NumberRange

class WhatShouldIPlay(Form):
	timeSpanToPlay = SelectField(u'Amount of Time', choices=[('30', '30 minutes or less'), ('60', '60 minutes or less'), ('90', '90 minutes or less'), ('120', '120 minutes or less'), ('150', '150 minutes or less'), ('180', '180 minutes or less'), ('600', '181 minutes or more')])
	
	themeToPlay  		= SelectField(u'Theme of Game', choices=[('dontCare', 'Dont Care'), ('fantasy', 'Fantasy'), ('scifi', 'Sci Fi'), ('horror', 'Horror'), ('superHero', 'Super Hero'), ('contemporary', 'Contemporary')])
	
	numberOfPlayer  	= SelectField(u'Number of Players', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),('7', '7'), ('8', '8')])
	
	gameMechanics  		= SelectField(u'Game Mechanic', choices=[('dontCare', 'Dont Care'),('deckBuilder', 'Deck Builder'), ('areaControl', 'Area Control'), ('traitor', 'Traitor'), ('victoryPoints', 'Victory Points'), ('warGame', 'War Game'), ('pickUpAndDeliver', 'Pick up and Delivery'), ('thematic', 'Thematic'), ('cooperative', 'Coopreative')])
	
	levelOfRulesDifficulty	= SelectField(u'Level of Rules Difficulty', choices=[('dontCare', 'Dont Care'), ('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard'), ('superHard', 'Super Hard')])
	
	searchHashes = StringField('searchHashes')

class TwilightImperiumRaceRandomizer(Form):
	player1 = StringField('player1', validators=[DataRequired()])
	player2 = StringField('player2', validators=[DataRequired()])
	player3 = StringField('player3', validators=[DataRequired()])
	player4 = StringField('player4')
	player5 = StringField('player5')
	player6 = StringField('player6')
	player7 = StringField('player7')
	player8 = StringField('player8')

class TwilightImperiumBattleCalculator(Form):	
	#attacker form elements
	#
	attackerNumberOfDreadNoughts = SelectField(u'Number of Dreadnoughts', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
	attackerDreadNoughtBonus = IntegerField('attackerDreadNoughtBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	attackerNumberOfCarriers = SelectField(u'Number of Carriers', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])
	attackerCarrierBonus = IntegerField('attackerCarrierBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	attackerNumberOfCruisers = SelectField(u'Number of Cruisers', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),('7', '7'), ('8', '8')])
	attackerCruiserBonus = IntegerField('attackerCruiserBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	attackerNumberOfDestroyers= SelectField(u'Number of Destroyers', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),('7', '7'), ('8', '8')])
	attackerDestroyerBonus = IntegerField('attackerDestroyerBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	attackerNumberOfWarSuns = SelectField(u'Number of WarSuns', choices=[('0', '0'), ('1', '1'), ('2', '2')])
	
	attackerNumberOfFighters = IntegerField('attackerNumberOfFighters', validators=[NumberRange(min=0, max=30)], default='0')
	attackerFighterBonus = IntegerField('attackerFighterBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	attackerNumberOfSoldiers = IntegerField('attackerNumberOfSoldiers', validators=[NumberRange(min=0, max=30)], default='0')
	attackerSoldierBonus = IntegerField('attackerSoldierBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	#defender form elements
	#
	defenderNumberOfPDS = SelectField(u'Number of PDS', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')])		
	defenderPDSBonus = IntegerField('defenderPDSBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	defenderNumberOfDreadNoughts = SelectField(u'Number of Dreadnoughts', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
	defenderDreadNoughtBonus = IntegerField('defenderDreadNoughtBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	defenderNumberOfCarriers = SelectField(u'Number of Carriers', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')])
	defenderCarrierBonus = IntegerField('defenderCarrierBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	defenderNumberOfCruisers = SelectField(u'Number of Cruisers', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),('7', '7'), ('8', '8')])
	defenderCruiserBonus = IntegerField('defenderCruiserBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	defenderNumberOfDestroyers= SelectField(u'Number of Destroyers', choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),('7', '7'), ('8', '8')])
	defenderDestroyerBonus = IntegerField('defenderDestroyerBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	defenderNumberOfWarSuns = SelectField(u'Number of WarSuns', choices=[('0', '0'), ('1', '1'), ('2', '2')])
	
	defenderNumberOfFighters = IntegerField('defenderNumberOfFighters', validators=[NumberRange(min=0, max=30)], default='0')
	defenderFighterBonus = IntegerField('defenderFighterBonus', validators=[NumberRange(min=0, max=3)], default='0')
	
	defenderNumberOfSoldiers = IntegerField('defenderNumberOfSoldiers', validators=[NumberRange(min=0, max=30)], default='0')
	defenderSoldierBonus = IntegerField('defenderSoldierBonus', validators=[NumberRange(min=0, max=3)], default='0')	

class DiceRollerForm(Form):
	numberOfDice  	= SelectField(u'Number of Dice', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'),('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')])
	diceType  		= SelectField(u'Dice Type', choices=[('4', 'd4'), ('6', 'd6'), ('8', 'd8'), ('10', 'd10'), ('12', 'd12'), ('20', 'd20'),('100', 'd100')])
	

class DuneDiceRollerForm(Form):
	factionDice1 = 'TestfactionDice1'
	factionDice1Hidden = HiddenField("")
	
	factionDice2  = 'TestfactionDice2'
	factionDice2Hidden = HiddenField("")
	
	factionDice3  = 'TestfactionDice3'
	factionDice3Hidden = HiddenField("")
	
	factionDice4  = 'TestfactionDice4'
	factionDice4Hidden = HiddenField("")
	
	kanlyDice  = 'TestkanlyDice'
	kanlyDiceHidden = HiddenField("")
	
	spiceDice  = 'TestspiceDice'
	spiceDiceHidden = HiddenField("")
	
	regionDice  = 'TestregionDice'
	regionDiceHidden = HiddenField("")
	
	factionDice1Freeze = BooleanField('factionDice1Freeze', default=False)
	factionDice2Freeze = BooleanField('factionDice2Freeze', default=False)
	factionDice3Freeze = BooleanField('factionDice3Freeze', default=False)
	factionDice4Freeze = BooleanField('factionDice4Freeze', default=False)
	
	kanlyDiceFreeze = BooleanField('kanlyDiceFreeze', default=False)
	spiceDiceFreeze = BooleanField('spiceDiceFreeze', default=False)
	regionDiceFreeze = BooleanField('regionDiceFreeze', default=False)
	
	
	
	
	
	

	