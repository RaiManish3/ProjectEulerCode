# ------------------------------SELF-MADE----------------------
# ------------------------EFFICIENCY GOOD----------------------
lst=[]
lst.append(1)

def pow_sum():
	l=len(lst)
	tmp=0
	carry=0

	for i in xrange(l):
		tmp=lst[i]*2;
		lst[i]=tmp%10+carry
		carry=tmp/10
			
	if carry==1:		
		lst.append(1)
	

def call_pow(power):
	for i in xrange(1,power):
		pow_sum()

# call_pow(1001)

# print sum(lst)