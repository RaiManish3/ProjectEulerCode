import time
start_time=time.time()
import itertools

# ==============================EXECUTION TIME : 0.25 S================================

set_1=[]

def calc_power(i,tmp):
	l=len(tmp)
	
	carry=0

	for n in xrange(l):
		tmp2=tmp[n]*i+carry
		tmp[n]=(tmp2)%10
		carry=(tmp2)/10

	while carry!=0:
		tmp.append(carry%10)
		carry/=10
	
	return tmp




def gen_base(a,b):
	for i in xrange(2,a+1):
		tmp=[i]
		
		for j in xrange(2,b+1):
			tmp=calc_power(i,tmp)
			set_1.append(tmp[:])
			

	# ------------------Now remains removing duplicates records-----------------#
	# ------ we can do that by first sorting and then having comparison---------#
	# -------itertools provide us with one liner of the above said--------------#
	# more info at--http://stackoverflow.com/questions/2213923/python-removing-duplicates-from-a-list-of-lists--#

	set_1.sort()
	return len(list(k for k,_ in itertools.groupby(set_1)))
	

print gen_base(100,100)
print time.time()-start_time