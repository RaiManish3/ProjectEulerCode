import time
start_time=time.time()

######################################################################################

# ==================================EXECTUTION TIME 1s==================================


# make_list coverts integer into a list of digits------------------------- 

def make_list(number):
	lst=[]

	while number!=0:
		lst.append(number%10)
		number/=10

	return lst

# in_this_list checks for duplicacy in two list

def in_this_list(l1,l2):
	for x in l1:
		if x in l2:
			return 1
	return 0

# not_all_distinct_elements checks for duplicacy in same list

def not_all_distinct_elements(l):
	len1=len(l)
	len2=len(set(l))
	if len1==len2:
		return 0
	return 1


# -------------------------------------------------------------------------------
# at some point i and j will interchange values so to avoid repetition we can limit the values 
# i and j take. let i take 1 digit number then j has to take 4 digit number while when i takes
# a two digit number then j has to take three digit number for the requirement to be fulfilled.
# -------------------------------------------------------------------------------------


def pandigital():
	# sum_product=0
	prod_list=set()

	for i in xrange(1,100):              
		lst1=make_list(i)

		if not_all_distinct_elements(lst1) or 0 in lst1:
			continue

		for j in xrange(100,5000):
			lst2=make_list(j)
			if not_all_distinct_elements(lst2) or 0 in lst2:
				continue

			if in_this_list(lst2,lst1):
				continue

			prod=i*j
			lst3=make_list(prod)
			lst=lst2+lst1
			if not_all_distinct_elements(lst3) or 0 in lst3:
				continue

			if in_this_list(lst3,lst):
				continue

			lst+=lst3

			if len(set(lst))==9:

				prod_list.add(prod)
				# sum_product+=prod
				# print "product=%d, i=%d, j=%d "%(prod,i,j)

	return sum(prod_list)		


print pandigital()
print time.time()-start_time

##########################################################################################

# =======================================Testing==========================================

# print not_all_distinct_elements([6,8,1])
# print in_this_list([9,3],[6,8,1])
# lm=[1,6,8]
# print lm , list(set(lm))
# l1=[1,3,0,4]
# print 0 in l1
