import time
begin=time.time()

################################################################################
# ============================EXECUTION TIME: 9ms===============================

"""
	SOURCE: http://blog.dreamshire.com/project-euler-82-solution/
	ACTUALLY I TRIED A FEW ATTEMPTS BEFORE LOOKING INTO SOMEBODY'S WORK,
	BUT ALL IN VAIN.

	THE IDEA HERE IS SIMPLE YET INTERESTING.
	WE DECLARE A 1-D LIST ACCOUNTING FOR THE BEST PATH UPTIL NOW.
	HERE WE START WITH LAST COLUMN AND MAKE OUR WAY TO THE FIRST ONE.

	DOWN APPROACH:
	THE CLEVER MOVE: WE ASSIGN COST[0]+=LST[0][J] AND MAKE COMPARISON OF PATH
	COST[I]-->FROM RIGHT COLUMN
	COST[I-1]--->FROM ABOVE THE CURRENT CELL
	WHICHEVER IS LOWEST, MAKE IT ADD TO THE CURRENT VALUE OF CELL

	THEN WE BEGIN TO GO UP:
	ANY CELL HAS A COST OF IT AS A CONSEQUENCE OF ABOVE,
	SO MAKE A COMPARISON FOR
	COST[I]--->  PREVIOUSLY UPDATED
	COST[I+1]+ VALUE ORIGINALLY IN CURRENT CELL---> THE UPWARD MOVE

	THEREFORE WE MADE ALL THE COMPARISONS: RIGHT, UP , DOWN
"""

size=80
def read_input():

	f=open('p082_matrix.txt','r')
	# f=open('a0.txt','r')

	lst=[map(int,row.split(',')) for row in f.readlines()]

	cost=[lst[i][-1] for i in xrange(size)]

	for j in xrange(size-2,-1,-1):
		cost[0]+=lst[0][j]
		for i in xrange(1,size):
			cost[i]= min(cost[i-1],cost[i])+lst[i][j]
		for i in xrange(size-2,-1,-1):
			cost[i]=min(cost[i],cost[i+1]+lst[i][j])
		# print (cost.index(min(cost)),j),"-->",

	return min(cost)

print read_input()
# print time.time()-begin