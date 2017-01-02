import time
begin=time.time()

######################################################################################
# ===============================EXECUTION TIME: 43s======================================

"""
	BASICALLY IMPLEMENTED BRUTE FORCE.
	MADE FUNCTION FOR CHECKING ALL VALID MOVES.

	MADE A RECURSIVE FUNCTION 'FIND_SOL' WHICH FILLS UP THE BLANKS WITH (1..9) VALUES
	AND SENDS THIS CONFIGURATION TO 'CHECKS' FUNCTION OTHERWISE REVERTS THAT BLANK TO
	0 VALUE ONLY.

"""

grid=[]
grid2=[]

def check_3x3(i,j):
	start_i,start_j=(i/3)*3,(j/3)*3
	stop_i,stop_j=start_i+3,start_j+3
	for x in xrange(start_i,stop_i):
		for y in xrange(start_j,stop_j):
			if grid[x][y]==grid[i][j] and x!=i and y!=j:
				return 0
	return 1
	

def check_row(i,j):
	for x in xrange(9):
		if grid[i][x]==grid[i][j] and x!=j:
			return 0
	return 1

def check_column(i,j):
	for x in xrange(9):
		if grid[x][j]==grid[i][j] and x!=i:
			return 0
	return 1

def checks(i,j):
	if check_row(i,j) and check_column(i,j) and check_3x3(i,j):
		return 1
	return 0

flag_exit=0
t_count=0

def find_sol(row,col):
	global flag_exit,t_count
	if row>8:
		# for m in xrange(9):
		# 	print grid[m]
		t_count+=100*grid[0][0]+10*grid[0][1]+grid[0][2]
		flag_exit=1
		return

	if grid2[row][col]:
		find_sol((row+(col+1)/9),(col+1)%9)
	else:
		for i in xrange(1,10):
			grid[row][col]=i
			if checks(row,col):
				find_sol((row+(col+1)/9),(col+1)%9)
				if flag_exit:
					return
			grid[row][col]=0                                         #THIS LINE MADE IT ALL SOLVABLE



def take_input():
	global grid2
	global flag_exit
	f=open('p096_sudoku.txt','r')

	for i in xrange(50):
		flag_exit=0
		print i
		for j in xrange(10):
			if j==0:
				f.readline()
			if j!=0:
				str1=f.readline()
				str1=str1[:-1]
				l1=list(str1)
				l1=list(map(int,l1[:]))
				grid.append(l1)

				l2=l1[:]
				grid2.append(l2)

		find_sol(0,0)

		del grid[:]
		del grid2[:]

take_input()
print t_count
print time.time()-begin