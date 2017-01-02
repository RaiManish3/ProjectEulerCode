import max_prime_under as mp
import time
start=time.time()
######################################################################################
# ===============================EXECUTION TIME:0.4s==================================

prime_list=[]

def gen_prime_list():
	for i in xrange(1001,9999,2):
		if mp.isPrime(i):
			prime_list.append(i)

def main():
	gen_prime_list()
	count=0
	l=len(prime_list)

	for i in xrange(l/3):
		num1=prime_list[i]
		for j in xrange(l/3,2*l/3):
			num2=prime_list[j]
			l1=list(str(num1))
			l2=list(str(num2))
			l1.sort()
			l2.sort()

			if l1==l2:
				c=num2-num1
				num3=c+num2
				if num3 in prime_list:
					l3=list(str(num3))
					l3.sort()
					if l3==l1:
						print "%d%d%d"%(num1,num2,num3) 
						count+=1
						if count==2:
							return

	
main()
print time.time()-start