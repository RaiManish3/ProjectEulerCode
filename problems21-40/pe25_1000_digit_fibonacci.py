
###################################################################################################

# ------------------------------------execution time: 1ms-------------------------------------


import time
start_time=time.time()


fib=[]
fib.append([1])
fib.append([1])

# uncomment line below
size=int(raw_input("Enter number of digits: "))
# size=1000

index=2

# --------------------- elementary addition of list of lists---------------------------
def add_fib():
	l=len(fib)
	carry=0
	temp_list=[]
	list1,list2=fib[l-1],fib[l-2]
	ls=len(list2)

	for i in xrange(ls):
		x=list1[i]+list2[i]
		temp_list.append((x+carry)%10)
		if x+carry>9:
			carry=1
		else: carry=0

	ll=len(list1)

	if ll>ls:
		for i in xrange(ls,ll):
			x=list1[i]
			temp_list.append((x+carry)%10)
			if x+carry>9:
				carry=1
			else:
				carry=0

	if carry==1:
		temp_list.append(carry)

	return temp_list
# -------------------------------------------------------------------------------------


# uncomment these for this very program
while len(fib[len(fib)-1])<size:
	fib.append(add_fib())
	fib.pop(0)
	index+=1

# print fib

# uncomment these for the execution
print index
print time.time()-start_time



#################################################################################################