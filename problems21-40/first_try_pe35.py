import max_prime_under as mp

t_count=0

def check_prime_in_digit_range(index,digits,lst):
	global t_count

	for i in xrange(index+1):
		l1=[]
		number=lst[i]
		while number!=0:
			l1.append(number%10)
			number/=10

		if 0 in l1 or 2 in l1 or 5 in l1:
			lst[i]=0
			t_count-=1
			continue

		for x in xrange(digits-1):
			number=0
			d=digits-1
			j=0
			while d>=0:
				number+=l1[(digits-2-x-j)%digits]*(10**d)
				d-=1
				j+=1
			if number not in lst:
				lst[i]=0
				t_count-=1
				break


	t_count+=len(lst)


def circular_prime(no_digits):
	limit=10**no_digits
	prev_digits=1
	lst=[]
	lst.append(2)

	for i in xrange(3,limit+2,2):
		number=i
		new_digits=1

		if number%2==0:
			continue

		while number>=10:
			number/=10
			new_digits+=1


		if new_digits>prev_digits:
			check_prime_in_digit_range(len(lst)-1,prev_digits,lst)
			lst=[]

		
		if mp.isPrime(i):
			lst.append(i)

		prev_digits=new_digits



circular_prime(6)
print t_count
