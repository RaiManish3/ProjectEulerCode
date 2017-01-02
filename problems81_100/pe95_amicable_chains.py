import pe21_amicable_number as ami
import time
start=time.time()

#############################################################
# ====================EXECUTION TIME:14s=====================

"""
	METHOD USED: BRUTE FORCE.
	WE ARE JUST DOING THE FOLLOWING:
	PICK AN INDEX, CHECK IF IT EQUALS LST[INDEX]
	IF NOT MAKE THAT LST[INDEX] AS YOUR NEW INDEX
	UNTIL TARGET IS REACHED{WHAT WE WANT},
	OR IS SAME AS AN ELEMENT IN THE LIST 'LL'
	OR IS GREATER THAN A MILLION.
"""

def check_chains(upto):
	ami.data_list(upto)
	l=len(ami.lst)
	longest_chain={'begin':1,'max_count':1}
	for i in xrange(2,l):
		target=i
		count,flag=0,0
		ind=i
		ll=[]
		while 1:
			count+=1
			if ind>10**6 or ind in ll:
				flag=0
				break
			if ami.lst[ind]==target:
				flag=1
				break
			ll.append(ind)
			ind=ami.lst[ind]
			# print "####",ind
		# print "---------------",i
		del ll[:]
		if flag and count>longest_chain['max_count']:
			longest_chain['max_count']=count
			longest_chain['begin']=i
	return longest_chain



print check_chains(10**6)
print time.time()-start