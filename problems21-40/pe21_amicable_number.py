# ------------------------------------------------------
##############################OLDER CODE FOR DIVISION SUM
# import math

# def divisor_sum(number):
# 	d_sum=1
# 	stop= int(math.sqrt(number))
# 	for i in xrange(2,stop+1):
# 		if number%i==0:
# 			d_sum+=i+(number/i if i*i!=number else 0)
# 	return d_sum

# def data_list(upto):
# 	for i in xrange(1,upto):
# 		lst.append(divisor_sum(i))

# ---------------------------------------------------------

lst=[]
# lst.append(0)

#  MADE THIS CHANGE FOR PE95_AMICABLE CHANGE
#  VERY EFFICIENT
def data_list(upto):
	for i in xrange(upto):
		lst.append(1)
	for i in xrange(2,upto):
		for j in xrange(2*i,upto,i):
			lst[j]+=i

def amicable(upto):
	t_sum=0
	data_list(upto)
	for i in xrange(1,upto):
		if lst[i]<upto and i==lst[lst[i]] and lst[i]!=i:
			t_sum+=i

	return t_sum


# print amicable(int(raw_input("Enter a number: ")))
# data_list(13)
# print lst	