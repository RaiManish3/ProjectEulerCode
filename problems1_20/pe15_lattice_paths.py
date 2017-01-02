# my way to approach
# -----------------------------INEFFICIENT-------------------------------------
# count=0
# lst=[]
# lst.append(2)
# lst.append(6)

# def path(i,j):
# 	global count
# 	# print 'i=%d and j =%d and count=%d' %(i,j,count)
# 	if i>=size or j>=size:
# 		return
# 	if i==j and i!=0 and i!=size-1:
# 		count+=lst[size-2-i]
# 		return
# 	if i==size-1 and j==size-1:
# 		count+=1
# 	# print 'i=%d and j =%d and count=%d' %(i,j,count)
# 	path(i+1,j)
# 	path(i,j+1)

# for size in xrange(4,22):
# 	count=0
# 	path(0,0)
# 	lst.append(count)

# print lst

# -------------------------------EFFICIENT WAY-----------------------------------
# using DP
def eff_path(size):
	count_all=[[ (1 if (i==0) else 0) for i in range(size)] for y in range(size)]
	count_all[0]=[1 for i in range(size)]

	for i in xrange(1,size):
		for j in xrange(1,size):
			count_all[i][j]=count_all[i-1][j]+count_all[i][j-1]

	return count_all[size-1][size-1]

print eff_path(21)


# -------------------------------KNOWLEDGE------------------------------------
# ternary oprator in python:
# a if condition else b
# Also nnotice the way the 2-D list has been constructed.