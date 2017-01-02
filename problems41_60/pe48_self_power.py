import time
start=time.time()

#######################################################################################
# ================================EXECUTION TIME: 3s===================================

"""
	Type of a brute force method applied;
	Basically i am creating a list of 10 digit product for each number except multiples
	of 10 as they will only result in all 10 places occupied by 0's which dont affect the
	addition overall.

	And then adding the corresponding digits for all elements in the list.

	------------------------------BETTER APPROACH--------------------------------
	A knowledge of modulo arithematic would make it a further simple problem to deal
	with.
	I haven't implemented it here but go for that solution if you want to improve 
	the performance.

"""

lst=[]

def self_power(a):
	num=a

	if a%10==0:
		return

	l1=[]
	while num!=0:
		l1.append(num%10)
		num/=10

	tmp,carry=0,0

	for x in xrange(a-1):
		l=len(l1)
		for j in xrange(l):
			tmp=l1[j]*a
			l1[j]=(tmp+carry)%10
			carry=(tmp+carry)/10
		if len(l1)>=10:
			carry=0
		else:
			while carry!=0:
				l1.append(carry%10)
				carry/=10

	
	while len(l1)<10:
		l1.append(0)
	lst.append(l1)


def add_list_elements():
	l=len(lst)
	carry=0
	sum_lst=[]

	for x in xrange(10):
		p_sum=0
		for i in xrange(l):
			p_sum+=lst[i][x]

		sum_lst.append((p_sum+carry)%10)
		carry=(p_sum+carry)/10

	return sum_lst





def main(upto):
	for i in xrange(1,upto):
		self_power(i)

	l2=add_list_elements()
	l2.reverse()
	str1=''.join(map(str,l2))
	return str1



# print main(1000)
# # print lst
# print time.time()-start
