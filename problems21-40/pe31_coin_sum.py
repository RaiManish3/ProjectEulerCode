
def main():
	ways=0
	money=20
	for i in xrange(money,-1,-200):
		for j in xrange(i,-1,-100):
			for k in xrange(j,-1,-50):
				for l in xrange(k,-1,-20):
					for m in xrange(l,-1,-10):
						for n in xrange(m,-1,-5):
							for o in xrange(n,-1,-2):
								ways+=1
								print i,j,k,l,m,n,o



	return ways


print main()
