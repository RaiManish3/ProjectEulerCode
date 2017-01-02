# from decimal import *
# getcontext().prec=50

# ###############################----USE ELEMETARY DIVISION--------####################

"""WHEN WE DIVIDE SAY 1 BY 13, WHAT WE USUALLY DO IS NOTE ITS REMAINDER THEN MULTIPLY THAT BY 10 AND CARRY THAT FORWARD
   LIKE 1%13=1 => 10%13=10 => 100%13=9 => 90%13=12 => 120%13=3 => 30%13=4 =>40%13=1
   SO THERE IS 6 LENGTH REPETITION OF SEQUENCE OF NUMBER.
   NOTICE THAT THE MAX LENGTH FOR NUMBER 'M' CAN GOTO 'M-1' AS THERE ARE MAX 'M-1' REMAINDERS. 
"""


# ========================================================================================

def max_repeat(upto):
	
	for i in xrange(upto,1,-1):
		part_length=0
		r,tmp=1,0
		while tmp!=1:
			r=(r*10)%i
			tmp=r
			print i,r
			part_length+=1
			if part_length==i-1:
				if tmp==1:
					return i,part_length
				else : break
			

# print max_repeat(1000)

# ========================================================================================