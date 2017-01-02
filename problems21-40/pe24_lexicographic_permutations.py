# -------------------------------------EXECUTION TIME: 10 MICROSEC---------------------

import time
start_time=time.time()

# ###############################UNCOMMENT THE LINES TO GET BETTER IDEA OF WHAT THE CODE IS DOING############## 

fact=[1,1,2,6,24,120,720,5040,40320,40320*9]

def start_number(under):
	t_sum=0
	i=9
	lst=[]

	while i>0:
		n=-1
		while t_sum<under:
			t_sum+=fact[i]
			n+=1
			while n in lst:
				n+=1
			# print n, t_sum
		
		lst.append(n)

		t_sum-=fact[i]
		# print "-------------",t_sum,"-----------------"
		i-=1

	for i in xrange(10):
		if i not in lst:
			lst.append(i)
			break

	return ''.join(map(str,lst))

print start_number(100)
print time.time()-start_time




############################################################################################