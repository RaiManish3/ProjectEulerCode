import time
start_time=time.time()

# ===============================EXECUTION TIME: 0.1s===================================

fact_dic={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}

def digit_fact():
	sum_digit_fact=0
	for i in xrange(10,50000):           #this range matters
		sum_indi=0
		number=i
		while number!=0:
			sum_indi+=fact_dic[number%10]
			number/=10
			
		if sum_indi==i:
			sum_digit_fact+=i

	return sum_digit_fact


print digit_fact()
print time.time()-start_time
