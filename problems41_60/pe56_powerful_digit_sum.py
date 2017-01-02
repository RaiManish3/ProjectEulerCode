import time
start=time.time()

####################################################################################
# =================================EXECUTION TIME: 8s===============================

def get_power(a,b):
	num=a

	if a%10==0:
		return

	l1=[]
	while num!=0:
		l1.append(num%10)
		num/=10

	tmp,carry=0,0

	for x in xrange(b-1):
		l=len(l1)
		for j in xrange(l):
			tmp=l1[j]*a
			l1[j]=(tmp+carry)%10
			carry=(tmp+carry)/10
		while carry!=0:
			l1.append(carry%10)
			carry/=10

	return sum(l1)


def max_digit_sum(a_upto,b_upto):
	num_dic={'a':1,'b':1,'digit_sum':1}
	for a in xrange(1,a_upto):
		for b in xrange(1,b_upto):
			count=get_power(a,b)
			if count>num_dic['digit_sum']:
				num_dic['digit_sum']=count
				num_dic['a']=a
				num_dic['b']=b

	return num_dic

print max_digit_sum(100,100)
print time.time()-start