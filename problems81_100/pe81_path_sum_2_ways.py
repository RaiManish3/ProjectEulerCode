import time
begin=time.time()

#################################################################################
# ================================EXECUTION TIME:8ms============================

def path_sum():
	f=open('p081_matrix.txt','r')
	lst=[]

	for i in xrange(80):
		str1=f.readline()
		str1=str1[:-1]
		ll=list(str1.split(','))
		ll=list(map(int,ll[:]))
		lst.append(ll)

	for i in xrange(1,80):
		lst[i][0]+=lst[i-1][0]
		lst[0][i]+=lst[0][i-1]

	for i in xrange(1,80):
		for j in xrange(1,80):
			lst[i][j]+=min(lst[i][j-1],lst[i-1][j])

	return lst[79][79]

print path_sum()
print time.time()-begin