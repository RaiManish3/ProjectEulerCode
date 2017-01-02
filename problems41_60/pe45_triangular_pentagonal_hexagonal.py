import math
import time
start=time.time()

###################################################################################
# =============================EXECUTION TIME:0.08s================================

def main():
	n=200
	count=0
	while 1:
		t=(n*(n+1))/2
		n1=(1+math.sqrt(1+24*t))/6
		if n1==int(n1):
			n2=(1+math.sqrt(1+8*t))/4
			if n2==int(n2):
				count+=1
				print t
				if count==2:
					return

		n+=1

main()
print time.time()-start