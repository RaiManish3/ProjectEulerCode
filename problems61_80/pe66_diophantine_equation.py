import math
import time
start=time.time()

####################################################################################
# ===========================EXECTION TIME: 0.021s======================================

"""
	IN CONTINUED FRACTION FUNCTION, WE GENERATE THE THE i'th CONVERGENT TERM (a_i)
	AND SEE THE OVERALL FRACTION (p_i,q_i). WHEN a_i==2*a_0 , we have a periodicity.
	then two conditions follow:
	If p_count as in a_i=a_(p_count+1) is odd we return the previous values,
	otherwise we return a_(2*p_count+1).
"""

def continued_fraction(i):

	sqrt_i=math.sqrt(i)
	decimal=sqrt_i-int(sqrt_i)
	if decimal==0:
		return 0,0
	a_i=a_0=int(sqrt_i)
	m_0=0
	d_0=1
	p_i,p_j,q_i,q_j=a_0,1,1,0

	p_new,q_new=0,0
	p_count,flag=-1,0

	while 1:
		m_0=d_0*a_i-m_0
		d_0=(i-m_0**2)/d_0
		a_i=int((a_0+m_0)/d_0)

		p_new=a_i*p_i+p_j
		q_new=a_i*q_i+q_j

		# print p_new,q_new,a_i

		p_j,q_j=p_i,q_i
		p_i,q_i=p_new,q_new

		p_count+=1

		if a_i==2*a_0:
			if p_count%2:
				return p_j, q_j
			if flag==0:
				r_p=2*p_count+1
				flag=1
			if flag and p_count==r_p:
				return p_j, q_j


def main(upto):
	dic={'D':5,'x':9}
	for i in xrange(2,upto+1):
		x, y=continued_fraction(i)
		if x>dic['x']:
			dic['x']=x
			dic['D']=i

	print dic



main(1000)
print time.time()-start