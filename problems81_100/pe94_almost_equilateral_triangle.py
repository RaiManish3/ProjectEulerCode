import time
begin=time.time()
###########################################################################
# ======================EXECUTION TIME:0.1ms===============================

"""
	# my first approach was through heron's formula check for area but there is
	# limitation to the precision of floating point plus to evaluate till 10**9
	# takes too much time.

	# better approach is through pell's equation.

	SOURCE : http://www.mathblog.dk/project-euler-94-almost-equilateral-triangles/
"""


def almost_eq_tr():
	limit=10**9
	# pells first solution to x^2-3*y^2=1
	x0=x=2
	y0=y=1

	# store result
	p_sum=0

	while 1:

		# for solution to the b=a+1
		aTimes3=2*x-1
		areaTimes3=y*(x-2)

		if aTimes3>limit: break

		if areaTimes3>0 and aTimes3%3==0 and areaTimes3%3==0:
			p_sum+=(aTimes3+1)

		# for solution to the b=a-1
		aTimes3=2*x+1
		areaTimes3=y*(x+2)
		if aTimes3%3==0 and areaTimes3%3==0:
			p_sum+=(aTimes3-1)


		x,y=x*x0+3*y*y0,x0*y+y0*x

	return p_sum

# print almost_eq_tr()
# print time.time()-begin