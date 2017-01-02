import time
start=time.time()

####################################################################################
# ===============================EXECUTION TIME:0.4s=================================

def main(upto):
	for x in xrange(1,upto):
		l1=list(str(x))

		if set(l1)==set(list(str(2*x))):
			if set(l1)==set(list(str(3*x))):
				if set(l1)==set(list(str(4*x))):
					if set(l1)==set(list(str(5*x))):
						if set(l1)==set(list(str(6*x))):
							print x
							return


main(1000000)
print time.time()-start