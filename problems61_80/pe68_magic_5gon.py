import time
begin=time.time()

# ############################################################################
# =======================EXECUTION TIME:0.2s==================================

"""
	brute force over required sum and check for the minimal starting point but
	yet the maximal string.
"""

lst=[[0,0,0] for i in xrange(5)]
all_num=[9,8,7,6,5,4,3,2,1,10]
avail=all_num[:]
used=[]
r_sum=14

def magic(i,j):

	if lst[i][j]==0:
		l=len(avail)
		x=0
		while x<l:
			# the sum criterion----------------------
			psum=sum(lst[i])+avail[x]
			if psum>r_sum:
				x+=1
				continue
			if j==2 and psum!=r_sum:
				x+=1
				continue

			# make change----------------------------
			lst[i][j]=avail[x]
			if j==2 and i!=4:
				lst[i+1][1]=avail[x]
			if j==1 and i==0:
				lst[4][2]=avail[x]

			used.append(avail[x])
			avail.remove(avail[x])

			if j==2:
				i+=1
			# -------------------------------------------

			magic(i,(j+1)%3)

			# revert back changes----------------------
			if j==2:
				i-=1

			lst[i][j]=0
			if j==2 and i!=4:
				lst[i+1][1]=0
			if j==1 and i==0:
				lst[4][2]=0

			avail.insert(x,used[-1])
			del used[-1]
			# ------------------------------------------
			x+=1

	else:
		# no element in avail two case 1. found a solution 2. didn't made the last row sum check
		if not avail:
			if sum(lst[4])!=r_sum:
				return	
			print lst
			return
		# skip over middle term; go to 3rd column.
		magic(i,2)

magic(0,0)
print time.time()-begin