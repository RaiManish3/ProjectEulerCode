import time
start=time.time()

#####################################################################################
# ===============================EXECUTION TIME: 0.01s===============================

"""
	THE IDEA ALTHOUGH SIMPLE, IS RATHER NON-TRIVIAL.
	FOR EACH ITERATION I PLANNED TO CALCULATE ( 2+ RECIPROCAL OF PREVIOUS FRACTION )
	EXAMPLE: FIRST ITERATION: 2+ 1/2 = 5/2  | MAIN FRACTION IS OBTAINED BY ADDING RECIPROCAL OF THIS TO 1 = 7/5
			 SECOND ITERATION: 2+ 2/5=12/5 | MAIN FRACTION = 1+5/12=17/12
			 THIRD ITERATION: 2+5/12= 29/12 | MAIN FRACTION = 1+ 12/29 =41/29
			 AND SO ON...

	THE CODE CAN BE MADE EFFECTIVE FOR HIGHER ITERATIONS IF WE USE LISTS ADDITION.
"""

def main(no_of_iterations):
	num,denom=1,2
	count=0
	# lst=[]
	for x in xrange(1,no_of_iterations):
		tmp_num=2*denom+num
		tmp_denom=denom

		fraction_num=str(tmp_num+tmp_denom)
		fraction_denom=str(tmp_num)

		if len(fraction_num)>len(fraction_denom):
			count+=1
			# lst.append([fraction_num,fraction_denom])

		denom=tmp_num
		num=tmp_denom

	return count

# print main(1000)
# print time.time()-start