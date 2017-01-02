import time
begin=time.time()

######################################################################
# ====================EXECUTION TIME: 1ms=============================

"""
	APPLIED DP ALGORITHM
"""

def main(target):
	lst=[1 for i in xrange(target+1)]

	for i in xrange(2,target):        #	 i IS LIKE PICK A NUMBER j AND DISTRIBUTE 
		for j in xrange(i,target+1):  #  j INTO i+SOMETHING ELSE
			lst[j]+=lst[j-i]					#WHEN j DISTRIBUTED INTO i AND SAY x
												#UPDATE NO OF WAYS j IS DISTRIBUTED
	# print lst									#TO THE x'S WAYS + ITS OLDER ONE
	return lst[target]

# print main(100)
# print time.time()-begin
