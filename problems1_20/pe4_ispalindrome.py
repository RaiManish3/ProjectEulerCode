n1=999
n2=998

def isPal(n):
	n_str=str(n)
	l=len(n_str)
	i,j=0,l-1
	while i<j:
		if n_str[i]!=n_str[j]:
			break
		i+=1
		j-=1
	if i<j:
		return 0
	else :
		return 1

# print isPal(raw_input("Enter a number:  "))

def gen(n1,n2):
	if n1<=0 or n2<=0:
		return 0
	temp=n2
	pr=n1*temp
	# ck=n2*n2
	while pr>=900000:
		# print pr
		if isPal(pr):
			return pr
		else :
			temp-=1
			pr=n1*temp

	if pr<900000:
		gen(n2,n1-1)

# print gen(999,999)


# -----Need improvement---------------------------------------------------------------- 