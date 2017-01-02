###################################################################################

"""
	OBSERVE THE PATTERN IN WHICH THE NUMBERS ARE GENERATED IN THE SPIRAL.
	START FROM 1 THEN ADD 2 TO GET 3 THEN 2 GIVES 5 THEN 2 GIVES 7 AND SO IS 9 GENERATED
	THEN WE ADD 2*2 TO 9 TO GET 13 AND SO ON FOR FOUR VERTICES.	
"""

####################################################################################

# --------------------------------------execution time 1 ms------------------------------4



# =====================================================================================

import time
start_time=time.time()

upto=1001
i=1
lst=[1,1,1,1]
t_sum=1

while i<=upto/2:
	j=2*i
	lst[0]=lst[3]
	lst[0]+=j

	for x in xrange(1,4):
		lst[x]=lst[x-1]+j

	t_sum+=sum(lst)
	i+=1

print t_sum
print time.time()-start_time

# ======================================================================================
		