##############################################################
# ==================EXECUTION TIME:7ms========================
import time

n_string=""
for i in xrange(100):
	n_string+=raw_input()
	if i!=99:
		n_string+=','

begin=time.time()

n_list_comp=list(n_string.split(','))
l=len(n_list_comp)

n1_list=list(map(int,n_list_comp[0]))
n1_list.reverse()

def add(list1,list2):
	temp_list=[]
	carry=0
	for i in xrange(50):
		x=list1[i]+list2[i]
		temp_list.append((x+carry)%10)
		if x+carry>9:
			carry=1
		else: carry=0

	ll=len(list1)
	if ll>50:
		for i in xrange(50,ll):
			x=list1[i]
			temp_list.append((x+carry)%10)
			if x+carry>9:
				carry=1
			else:
				carry=0

	if carry==1:
		temp_list.append(carry)

	return temp_list


i=1
while  i<l:
	n2_list=list(map(int,n_list_comp[i]))
	n2_list.reverse()
	i+=1
	temp_list=add(n1_list,n2_list)
	n1_list=temp_list
	del n2_list


n1_list.reverse()
str1=""
for x in xrange(10):
	str1+=str(n1_list[x])

print str1
print time.time()-begin

#the numbers:
#can be found under numbers_pe13.txt