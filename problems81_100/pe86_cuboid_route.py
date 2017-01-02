import time
import math
begin=time.time()

##########################################################################
# =======================EXECUTION TIME:2s================================

"""
	SOURCE : MATHBLOG.
	I AM ONLY GOING TO EXPLAIN LINE 32
	ASSUME h<=w<=l
	SEE IF 1<WH<=L THEN THERE ARE EXACTLY FLOOR(wh/2) SOLUTIONS.
	HERE FOR ANY 'h' THE VALUE OF 'w' COMES OUT TO BE <=l (AS ASSUMED)

	BUT THE CASE WHEN L<WH<=2L ; WE HAVE TO RESTRICT PAIRS WHERE 'w' TAKES
	VALUE > 'l' . SO IT HAS TO TAKE VALUE FROM CEIL(wh/2) TO L ; BOTH INCLUDED.
	IN THIS CASE THERE ARE 1+(LENGTH-(wh+1)/2) SOLUTIONS.

	VERIFY YOURSELF TAKING l=4.
"""

def shortest_route():
	target=10**6
	solutions=0
	length=0

	while solutions<target:
		length+=1
		for wh in xrange(3,2*length+1):
			min_path=math.sqrt(length**2+wh**2)
			if min_path==int(min_path):
				solutions+= wh/2 if wh<=length else 1+(length-(wh+1)/2)


	return length

# print shortest_route()
# print time.time()-begin