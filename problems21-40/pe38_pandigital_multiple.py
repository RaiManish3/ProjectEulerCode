import time
start_time=time.time()

######################################################################################

# ================================execution time: 4ms =====================================

digits_upto=4
lst=[]
# count=1

"""
	The gen_number generates all strings of len<=5 and starting with 9.
	the argument of this recursive function takes 'digit' which ensures that
	numbers of length greater than digits_upto aren't generated.The main operation
	on 'digit' is of increment to generate bigger numbers.
	'str_num' contains the string so far formed; so when you return you end up in previous string
	
	# in first version of this code, i had a third argument
	and count is the last argument which acts as switch between higher numbers.
	it is noe commented.
"""
													
												#PREVIOUS VERSION 
												# def gen_number(digit,str_num,count):
def gen_number(digit,str_num):

	for i in xrange(1,10):

		if str(i) in str_num:                   			 #remove duplicate digit entry
			continue

		str_num+=str(i)
		if digit>=digits_upto:
				return
		if not str_num in lst:
			lst.append(str_num)

												# count+=1
												# if count>digit:
												# gen_number(digit+1,str_num,count)
		gen_number(digit+1,str_num)							#calling for higher numbers
		str_num=str_num[:-1]								#removing the last element added
												# continue

															# gen_number(1,'9',1)
															# print lst




def main():
												# gen_number(1,'9',1)
	gen_number(1,'9')
	max_num=9

	for i in lst:
		size=0
		j=int(i)
		# l1=[]
		l1=list(i)

		for k in xrange(2,5):
			tmp=j*k
			s_tmp=str(tmp)

			if '0' in list(s_tmp):							#zeroes aren't allowed
				break

															# s_tmp should have distinct elements
															# within itself and with l1
															# & of set is intersection
			if (set(list(s_tmp)) & set(l1)) or len(set(list(s_tmp)))!=len(list(s_tmp)):
				break

			# print tmp,set(list(s_tmp)),set(l1)

			l1+=list(s_tmp)

			if len(l1)==9:
				str2=''.join(l1)
				if int(str2)>max_num:
					max_num=int(str2)
					# print i
					break

			if len(l1)>9:
				break

	return max_num

print main()
print time.time()-start_time

###########################################################################################

# INTERSECTION OF TWO SETS
# l1=[1,2,3]
# l2=[2,3,4]
# print list(set(l1) & set(l2))	