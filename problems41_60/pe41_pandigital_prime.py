import max_prime_under as mp
import time
start=time.time()

######################################################################################
# ===================================time of execution: 0.04s================================

"""
		What i am doing here is creating a list for storing pandigital numbers of a particular digit
		then i'll make an iteration over only those set of numbers.

		The optimisation problem:
		when i make an start from digit 9 in main function the runtime is 4s.
		so i found a much better solution online.(source: mathblog)

		the divisibity by 3 is of great use here.
		a number is divisible by 3 if its digits sum is divisible by 3.
		for 9 digit numbers: 1+2+3+4+5+6+7+8+9=45 , =>there is no pandigital prime in it.
		for 8 digit numbers: 1+2+3+4+5+6+7+8=36, =>same inference
		for 7 digit numbers: 1+2+3+4+5+6+7=28 =>possibly yes.

"""

lst=[]

def gen_pandigital_for_digit(digits,str_num,count):
	global lst

	if count==digits:
		if str_num[-1] in ['2','4','6','8']:
			return
		lst.append(int(str_num))
		return

	for x in xrange(digits,0,-1):
		if str(x) in str_num:
			continue

		str_num+=str(x)
		count+=1

		gen_pandigital_for_digit(digits,str_num,count)
		str_num=str_num[:-1]
		count-=1


def main():
	global lst
	for digits in xrange(7,6,-1):                              #originally i kept the start to be 9                         
		lst=[]												   #which gave me result in 4s
		gen_pandigital_for_digit(digits,'',0)

		for i in lst:
			if mp.isPrime(i):
				return i


# print main()
# print time.time()-start