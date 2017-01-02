import time
begin=time.time()
combinations=0

########################################################################
# ==========================EXECUTION TIME: 0.3s========================

"""
	BRUTE FORCE BASICALLY;
	create_list1 makes a list for us and then calls out
	for check_list which creates list2 with the help of
	make_list2. Then when the l_all is constructed
	we count for the 'squares' and then conclude the
	result by dividing it by two because we have overcounted
	the cases where die 1 aand 2 switch.

	therefore we can reduce these unnescessary iterations
	to reduce the time by half.
"""

def make_list2(lst,x):
	tmp=[]
	for e in lst:
		tmp.append(e+x)
		tmp.append(x+e)
	return tmp[:]

def count_it(l_all):
	count=0
	for e in ['01','04','25','81']:
		if e not in l_all:
			return 0
	count+=4
	for e in ['06','09']:
		if e in l_all:
			count+=1
			break

	for e in ['16','19']:
		if e in l_all:
			count+=1
			break

	for e in ['36','39']:
		if e in l_all:
			count+=1
			break

	for e in ['46','49']:
		if e in l_all:
			count+=1
			break

	for e in ['64','94']:
		if e in l_all:
			count+=1
			break
	return count


# OVERLAPPING CASES HERE.
# IMPROVE HERE.

def check_list(lst):
	global combinations
	for a in xrange(5):
		l_a=make_list2(lst,str(a))
		for b in xrange(a+1,6):
			# if a==int(lst[0]) and b<int(lst[1]):
			# 	continue
			l_b=make_list2(lst,str(b))
			for c in xrange(b+1,7):
				# if a==int(lst[0]) and c<int(lst[2]):
				# 	continue
				l_c=make_list2(lst,str(c))
				for d in xrange(c+1,8):
					# if a==int(lst[0]) and d<int(lst[3]):
					# 	continue
					l_d=make_list2(lst,str(d))
					for e in xrange(d+1,9):
						# if a==int(lst[0]) and e<int(lst[4]):
						# 	continue
						l_e=make_list2(lst,str(e))
						for f in xrange(e+1,10):
							# if a==int(lst[0]) and f<int(lst[5]):
							# 	continue
							l_f=make_list2(lst,str(f))
							l_all=l_a+l_b+l_c+l_d+l_e+l_f
							if count_it(l_all)==9:
								combinations+=1



def create_list1():
	for a in xrange(5):
		for b in xrange(a+1,6):
			for c in xrange(b+1,7):
				for d in xrange(c+1,8):
					for e in xrange(d+1,9):
						for f in xrange(e+1,10):
							lst=[str(a),str(b),str(c),str(d),str(e),str(f)]
							check_list(lst)

# create_list1()
# print combinations/2
# print time.time()-begin