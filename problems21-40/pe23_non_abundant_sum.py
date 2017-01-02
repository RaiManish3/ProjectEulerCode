import pe21_amicable_number as fd
import time
start_time=time.time()

####################### need to optimise the solution
####################### currently it takes about 4.7 s to calculate

lst=[]
lst.append(12)

def data_list(upto):
	for i in xrange(18,upto):
		if fd.divisor_sum(i)>i:
			lst.append(i)

sum_lst=[]

def sum_abundant(upto):
	data_list(upto)
	l=len(lst)

	for i in xrange(l):
		for j in xrange(i,l):
			tmp=lst[i]+lst[j]
			if tmp>upto:
				break
			sum_lst.append(tmp)

	t_sum=(upto*(upto+1))/2
	return t_sum-sum(set(sum_lst))




print sum_abundant(28123)
print "time taken: ", time.time()-start_time

# ----------------------------------testing-----------------------------------------
# sum_abundant(28123)
# print lst
# print sum(set(sum_lst))


#=====================================Picked from the Forum===========================
# ------------------------------------time: 0.7s--------------------------------------

# def PE023(limit = 28123):
#   somDiv = [1] * (limit+1) # jusk 28123 inclus
#   for i in range(2, int(limit**.5)+1):
#     somDiv[i*i] += i
#     for k in range(i+1, limit//i+1):
#         somDiv[k*i] += k+i

#   abondant, res = set(), 0
#   ajout = abondant.add
#   for n in range(1, limit+1):
#     if somDiv[n]>n: ajout(n)
#     if not any( (n-a in abondant) for a in abondant ): 
#       res+=n
#       print n,res
#   return res

# print PE023(int(raw_input("Enter a number: ")))


# ====================================================================================