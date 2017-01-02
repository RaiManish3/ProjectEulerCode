
###################################################################################
# ==========================USING ALREADY EXISTED LIBRARY==========================
from decimal import *

getcontext().prec=102

def sqrt_100_decimals():
	t_sum=0
	for i in xrange(2,100):
		if i in [4,9,16,25,36,49,64,81]:
			continue
		str1=str(Decimal(i).sqrt())
		ll=list(map(int,str1[2:-2]))
		ll.append(int(str1[0]))
		t_sum+=sum(ll)
	return t_sum

# print sqrt_100_decimals()

# this is something interesting
# http://www.afjarvis.staff.shef.ac.uk/maths/jarvisspec02.pdf