def add_to_have_10_limit_list(list1,list2):
	carry=0
	temp_list=[]

	for i in xrange(10):
		x=list1[i]+list2[i]
		temp_list.append((x+carry)%10)
		if x+carry>9:
			carry=1
		else: carry=0
	
	return temp_list

def subtract_to_have_10_limit_list(list1,list2):
	carry=0
	temp_list=[]

	for i in xrange(10):
		if list2[i]>=list1[i]:
			x=list2[i]-list1[i]
			carry=0
		else:
			x=10+list2[i]-list1[i]
			carry=-1

		temp_list.append(x)
		if carry==-1:
			list2[i+1]+=-1
	
	return temp_list