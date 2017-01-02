import math
import time
start=time.time()

#######################################################################################
# ==================================execution time: 0.1s==============================

"""
							THE ARITHMETIC APPROACH
	solving  the equation a^2+b^2=c^2
					and		a+b+c=p
					gives value of b in terms of p
					Use the fact that b  is int and >0
			limits:
			p=100 to 1000 ; intuitively more number of solutions are more likely to occur
							at high value of p
			p should be even; check yourself

			a=1 to p/3; a<=b<c => a<p/3

"""

soln_dic={'no_of_sol':0,'p_value':100}

for p in xrange(100,1000,2):
	count=0
	for a in xrange(1,p/3):
		b=float(p*(p-2*a))/(2*(p-a))
		if b==int(b) and b>0:
			count+=1
			# print a,b


	if count>soln_dic['no_of_sol']:
		soln_dic['no_of_sol']=count
		soln_dic['p_value']=p

print soln_dic
print time.time()-start


#####################################################################################