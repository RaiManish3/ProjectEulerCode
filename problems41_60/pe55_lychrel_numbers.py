import pe36_double_base_palindrome as db
import time 
start=time.time()

#####################################################################################
# =================================EXECUTION TIME: 0.6s==============================

"""
	GONE FOR BRUTE FORCE WITH SLIGTH MODIFICATIONS
	CREATED A LIST 'LST' CONTAINING ALL NUMBERS UPTO 10000; THE IDEA IS THAT WHEN I FIND
	PALINDROME THEN ALL THE NUMBERS THAT WERE ADD AND REVERSE TO REACH THERE ARE CROSSED
	OUT FROM 'LST' SO THAT ONE DOES NOT HAVE TO GO THROUGH THAT COMPUTATION AGAIN.

"""

def add(list1,list2):
	carry=0
	temp_list=[]
	l=len(list1)

	for i in xrange(l):
		x=list1[i]+list2[i]
		temp_list.append((x+carry)%10)
		if x+carry>9:
			carry=1
		else: carry=0
	
	if carry==1:
		temp_list.append(carry)

	return temp_list

def from_list_to_int(lst):
	lst=list(map(str,lst[:]))
	str1=''.join(lst)
	return int(str1)

def lychrel(upto):
	lst=[i for i in xrange(1,upto)]
	lychrel_list=[]
	for i in lst:
		if i ==-1:
			continue
		num1=i
		l1=list(str(num1))
		l1=list(map(int,l1[:]))

		ll=[]             
		flag=0

		for x in xrange(50):
			ll.append(from_list_to_int(l1))
			l2=l1[:]
			l2.reverse()
			result=add(l1,l2)
			l1=result
			str_result=''.join(list(map(str,result)))
			ll.append(from_list_to_int(l2))

			if db.isPal(str_result):
				for m in ll:
					if m<upto:
						lst[m-1]=-1
				break

			if x==49:
				flag=1

		if flag:
			lychrel_list.append(i)

	return len(lychrel_list)



# print lychrel(10000)
# print time.time()-start