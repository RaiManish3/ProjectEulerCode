import math
import time
start=time.time()

# =====================================execution time: 4s============================

"""
	Think over the limits. Try to justify it.
"""


def main(lim):

	for k in xrange(1,lim):
		for j in xrange(k+1,lim):
			n1=(1+math.sqrt(1+12*(3*(j**2+k**2)-(j+k))))/6
			if n1==int(n1):
				n2=(1+math.sqrt(1+12*(3*(j**2-k**2)-(j-k))))/6
				if n2==int(n2):
					print j,k,n1,n2
					print (n2*(3*n2-1))/2
					return


main(5000)
print time.time()-start
# main(int(raw_input("enter the limit: ")))
# lim=5000