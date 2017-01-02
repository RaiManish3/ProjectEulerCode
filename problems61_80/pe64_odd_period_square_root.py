import math
import time
start=time.time()

##################################################################################
# =============================EXECUTION TIME:0.1s================================

"""
	NOT MUCH TO SAY; BEEN STUCK FOR DAYS SOLVING THIS PROBLEM ALL BY MYSELF;
	MY FIRST DESIGN WAS ABLE COMPLETELY BRUTE FORCE AND TOOK A GOOD AMOUNT OF
	TIME TO EXECUTE IT.
	SO I JUST SEARCHED THE NET THEN, FOUND THIS AMAZING ALGORITHM ON THE INTERNET.
						"SQUARE ROOT BY CONTINUED FRACTIONS"
"""

def main(upto):
	t_count=0
	for i in xrange(2,upto):
		sqrt_i=math.sqrt(i)
		decimal=sqrt_i-int(sqrt_i)
		if decimal==0:
			continue
		a_i=a_0=int(sqrt_i)
		m_0=0
		d_0=1
		p_count=0

		while 1:
			m_0=d_0*a_i-m_0
			d_0=(i-m_0**2)/d_0
			a_i=int((a_0+m_0)/d_0)
			p_count+=1

			# print i,a_0,a_i

			if a_i==2*a_0:
				if p_count%2==1:
					t_count+=1
				break

			

	return t_count


# print main(10000)
# print time.time()-start
