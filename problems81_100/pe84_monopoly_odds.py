import random
import time

begin=time.time()

########################################################################
# ===========================EXECUTION TIME: 2s=========================

"""
	I MUST ADMIT THAT WHEN I FIRST RECIPROCATED THE QUESTION, I WASN'T SURE
	WHAT THE QUESTION ASKS FOR (ABOUT THE NUMBER OF ROLLS). SO I SEARCHED FOR THE SAME.
	SOURCE: MATHBLOG.

	THE IDEA OF ""SIMULATION"" IS A GOOD WAY TO JUDGE STATISTICS AND PROBABILITY
	ACTUALLY WE HAVE TO SORT OF PLAY THE GAME STARTING THE NEXT TURN FROM WHERE WE LEFT.

	FUNCTION "CC()" ASSINGS CURRENT POSITION OF PLAYER AS PER THE INSTRUCTION GIVEN
	PLUS THOSE SELECTIVE CARDS OCCUR ONLY WHEN WE PICK THEM UP FROM THE SEQUENCE OF PILES
	SAME IS TRUE FOR THE FUNCTION "CHANCE()"
	
	THE MAIN() DOES THE JOB OF INCREAMENTING THE LIST OF SQUARE VISITED THE PLAYER IS ON
	THROUGH PSEUDORANDOM GENERATION OF DIE NUMBERS AND FOLLOWING THE RULE FOR DOUBLES
	AND G2J.
"""

# global variables
currentPos=0
ccPos=0
chancePos=0
finish_square_list=[0 for i in xrange(40)]

def CC():
	global currentPos,ccPos,chancePos
	cc_options=[0,10]
	ccPos=(ccPos+1)%16
	if ccPos<2:
		currentPos=cc_options[ccPos]

def chance():
	global currentPos,ccPos,chancePos
	chance_options=[0,10,11,24,39,5]
	chancePos=(chancePos+1)%16

	if chancePos<6:
		currentPos=chance_options[chancePos]
		return

	if chancePos in [6,7]:
		if currentPos==7:currentPos=15
		elif currentPos==22:currentPos=25
		elif currentPos==36:currentPos=5
		return

	if chancePos==8:
		currentPos=28 if currentPos==22 else 12
		return

	if chancePos==9:
		currentPos-=3


def main(rolls):
	global currentPos,ccPos,chancePos
	doubles=0
	for i in xrange(rolls):
		die1=random.randint(1,4)
		die2=random.randint(1,4)

		if die1==die2:
			doubles+=1
		else: doubles=0

		currentPos=(currentPos+die1+die2)%40 if doubles<3 else 10
		if doubles<3:
			if currentPos in [2,17,33]:
				CC()
			elif currentPos in [7,22,36]:
				chance()
			elif currentPos==30: currentPos=10
		else : doubles=0

		finish_square_list[currentPos]+=1


main(10**6)
strx=""
for i in xrange(3):
	ind1=finish_square_list.index(max(finish_square_list))
	if ind1<10: strx+="0"+str(ind1)
	else : strx+=str(ind1)
	finish_square_list[ind1]=-1

# print strx
# print time.time()-begin