import time
begin=time.time()

##################################################################
# =====================EXECUTION TIME:0.3ms=======================

"""
	SOURCE : DREAMSHIRE
	BASICALLY WE FIRST FIND THE INITIAL 10 TERMS OF THE POLYNOMIAL SEQUENCE.
	THEN APPLY THE SUBTRACTION METHOD
		FOR EXAMPLE: 
							1  8  27
							  7  19
							  	12
			ADD ALL THESE TO GET TO THE RESULT
"""

tmp_list=[]
t_sum=0
lst=[]

def generate_given_seq(upto):
	global t_sum,lst
	for n in xrange(1,upto+1):
		tmp=1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
		tmp_list.append(tmp)
	lst=tmp_list[:]
	t_sum+=sum(tmp_list)
	del tmp_list[:]

def sum_next(upto):
	global t_sum,lst
	generate_given_seq(upto)
	for i in xrange(upto-1):
		for j in xrange(len(lst)-1):
			tmp_list.append(lst[j+1]-lst[j])
		t_sum+=sum(tmp_list)
		lst=tmp_list[:]
		del tmp_list[:]

sum_next(10)
print t_sum
print time.time()-begin