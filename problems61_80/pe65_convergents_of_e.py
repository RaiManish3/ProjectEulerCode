import time
start=time.time()

######################################################################################
# =================================EXECUTION TIME:0.1ms==============================

"""
	IDEA IS SAME AS THAT FOLLOWED IN PE57_SQUARE_ROOT_CONVERGENTS.PY, ONLY DIFFERENCE
	IS THAT I HAVE WORKED UPON BOTTOM UP APPROACH AS THE TERMS IN FRACTION KEPT
	ON CHANGING;
	OBSERVATION LED ME AHEAD: 
		DECLARE FIRST FRACTION (THAT IS THE BOTTOM-MOST ONE); 
		THEN GENERATE THE TERM YOU ARE GOING TO ADD THIS FRACTION TO; CALL THIS FRACTION2
		RECIPROCAL FRACTION2 AND REPEAT STEP 2 AND 3
		FINALLY WHEN YOU REACH THE TOP OF FRACTIONAL ANALYSIS, ADD THIS TO 2
		OVER

	NOTE: MAIN(0) CORRESPONDS TO 3, THE SECOND CONVERGENT IN SEQUENCE.
"""

def main(first_fraction):
	if first_fraction%3==1:
		num=1
		denom=2*(first_fraction+2)/3
	else:
		num=1
		denom=1

	for i in xrange(first_fraction,0,-1):
		if i%3==2:
			a=2*(i+1)/3
		else: a=1

		num_tmp=num+denom*a
		num=denom
		denom=num_tmp

	num=2*denom+num
	# return num,denom
	sum_num=0
	while num!=0:
		sum_num+=num%10
		num/=10
	return sum_num


print main(98)
print time.time()-start

# for i in xrange(10):
# 	print main(i)