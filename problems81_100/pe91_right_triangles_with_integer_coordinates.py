import time
begin=time.time()

###################################################################
# ====================EXECUTION TIME:6s============================

"""
	BRUTE FORCE.
	THERE'S A VERY EFFICIENT AT 'MATHBLOG'. 
"""

def pythagorus_right(x1,y1,x2,y2):
	a=x1**2+y1**2
	b=x2**2+y2**2
	c=(x2-x1)**2+(y2-y1)**2

	if c==a+b or a==b+c or b==a+c: 
		return 1
	return 0


def main():
	upto=51
	lst1=set()
	lst2=set()

	for y1 in xrange(upto):
		for x1 in xrange(1,upto):
			for x2 in xrange(upto):
				for y2 in xrange(1,upto):
					if x1!=x2 or y1!=y2:
						if pythagorus_right(x1,y1,x2,y2):
							lst1.add((x1,y1,x2,y2))
							if y1!=0 and x2!=0:
								lst2.add((x2,y2,x1,y1))

	# calculations to remove duplicates!
	t=len(lst1)
	n=len(lst1-lst2)
	return n+(t-n)/2

# print main()
# print time.time()-begin