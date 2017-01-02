# Basically method used in elementary multiplication
lst=[]
lst.append(1)

def mutiplier(number):
	carry=0
	l=len(lst)
	for i in xrange(l):
		tmp=lst[i]*number
		lst[i]=(tmp+carry)%10
		carry=(tmp+carry)/10
		# print tmp,carry
	if carry!=0:
		if carry>=10:										#if carry>=10 store it in different boxes
			lst.append(carry%10)
			lst.append(carry/10)
		else:
			lst.append(carry)


def generate_factorial(upto):
	for i in xrange(1,upto+1):
		mutiplier(i)


generate_factorial(int(raw_input("Enter a number whose factorial you want :\n")))

lst.reverse()
str1=''.join(map(str,lst))
print str1
# print sum(lst)