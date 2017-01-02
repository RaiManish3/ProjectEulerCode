import max_prime_under as mp
import time
start=time.time()


# ################################  MY ATTEMPT #####################################
# =============================== EXECUTION TIME: 18s===============================

"""
	THIS IS A KIND OF A BRUTE FORCE WHERE I GENERATE PRIME LIST UPTO A MILLION
	AND THEN ITERATE OVER THEM TO SEE MAX TERMS IN SUMMATION.

	MUCH BETTER APPROACH I FOUND IS ON 'MATHBLOG' WHERE THE GUY MAKES USE OF CUMMULATIVE
	ADDITION AND SLIDES OVER THEM AT THE TIME OF SEARCHING.

"""

# prime_list=[]
# prime_list.append(2)

# def gen_prime_list(upto):
# 	for i in xrange(3,upto-1,2):
# 		if mp.isPrime(i):
# 			prime_list.append(i)

# def main(upto):
# 	gen_prime_list(upto)
# 	l=len(prime_list)
# 	l-=1
# 	number=prime_list[l]
# 	max_dic={'number':1,'terms':0}

# 	while number>upto/10:
# 		num=number
# 		count1,count2=0,0

# # --------------------------------------------------------------
# 		i=0
# 		while num>0:
# 			count1+=1
# 			num-=prime_list[i]
# 			i+=1

# 		if num==0:
# 			if count1>max_dic['terms']:
# 				max_dic['terms']=count1
# 				max_dic['number']=number

# 		num=-num

# 		i=0
# 		while num>0:
# 			num-=prime_list[i]
# 			count2+=1
# 			i+=1

# 		if num==0:
# 			if count1-count2>max_dic['terms']:
# 				max_dic['terms']=count1-count2
# 				max_dic['number']=number

# # ----------------------------------------------------------------

# 		l-=1
# 		number=prime_list[l]

# 	return max_dic

# ======================================================================

# print main(1000000)
# print time.time()-start

#######################################################################################


# BETTER SOLUTION

######################################################################################
# ================================EXECUTION TIME: 7s==================================

prime_list=[]
prime_list.append(2)
cum_sum=[]
cum_sum.append(2)

def gen_prime_list2(upto):
	for i in xrange(3,upto-1,2):
		if mp.isPrime(i):
			prime_list.append(i)
			cum_sum.append(i+cum_sum[-1])


def main2(upto):
	gen_prime_list2(upto)
	max_distance=0
	number=0
	l=len(prime_list)

	for i in xrange(l):
		num1=cum_sum[i]
		for j in xrange(i+max_distance+1,l):
			num2=cum_sum[j]

			if num2-num1>upto:
				break
			if num2-num1 in prime_list:
				distance=j-i
				if distance>max_distance:
					max_distance=distance
					number=num2-num1

	print max_distance, number


# main2(1000000)
# print time.time()-start

#######################################################################################