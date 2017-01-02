import time
begin=time.time()

######################################################################################
# =====================================EXECUTION TIME: 2s=============================

def gen_phi_func(upto):
	phi_list=list(xrange(upto+1))
	for i in xrange(2,upto+1):
		if phi_list[i]==i:
			for j in xrange(i,upto+1,i):
				phi_list[j]=phi_list[j]/i*(i-1)

	return sum(phi_list[2:])

print gen_phi_func(1000000)
print time.time()-begin
