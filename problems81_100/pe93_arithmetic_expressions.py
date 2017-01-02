import time
begin=time.time()

###############################################################################################
# ===============================EXECUTION TIME:1s=============================================

"""
	BRUTE FORCE BASICALLY.
	THE combination_generator FUNCTION SELECTS A OPERAND AND OPERATOR FROM THE LISTS AND
	CALCULATES THE SUM. WE HAVE USED SET() HERE TO AVOID DUPLICACY.
	THEN THIS SET IS SENT TO Fn check_continuous WHICH SEEKS FOR THE LONGEST NATURAL NUMBER
	SEQUENCE.

"""


num_lst=set()
max_count=0
# count=0    
# ------------dummy variable to check iterations: the "count" is nearly 500 for single execution

def combination_generator(initial,in_list):
	# global count
	# count+=1
	if not in_list:
		if initial>0 and initial==int(initial):
			num_lst.add(int(initial))
		return

	for x in in_list:
		for y in xrange(4):
			if y==0:
				index=in_list.index(x)
				in_list.remove(x)
				combination_generator(initial+x,in_list)
				in_list.insert(index,x)

			elif y==1:
				index=in_list.index(x)
				in_list.remove(x)
				combination_generator(initial-x,in_list)
				in_list.insert(index,x)

			elif y==2:
				index=in_list.index(x)
				in_list.remove(x)
				combination_generator(initial*x,in_list)
				in_list.insert(index,x)

			elif y==3:
				index=in_list.index(x)
				in_list.remove(x)
				combination_generator(initial/float(x),in_list)
				in_list.insert(index,x)


def check_continuous():
	global max_count
	i,p_count=1,0
	for e in num_lst:
		if e==i:
			p_count+=1
		else: break
		i+=1
	if p_count> max_count:
		max_count=p_count
	# print p_count
	# print num_lst


def list_gen():
	global max_count
	last_count=0
	strx=""

	for a in xrange(1,7):
		for b in xrange(a+1,8):
			for c in xrange(b+1,9):
				for d in xrange(c+1,10):
					# print "a,b,c,d",a,b,c,d
					combination_generator(a,[b,c,d])
					combination_generator(d,[a,b,c])
					combination_generator(c,[a,b,d])
					combination_generator(b,[a,c,d])

					combination_generator(-a,[b,c,d])
					combination_generator(-d,[a,b,c])
					combination_generator(-c,[a,b,d])
					combination_generator(-b,[a,c,d])

					check_continuous()
					if last_count<max_count:
						last_count=max_count
						strx=str(a)+str(b)+str(c)+str(d)

					num_lst.clear()
	return max_count,strx


# print list_gen()
# print time.time()-begin