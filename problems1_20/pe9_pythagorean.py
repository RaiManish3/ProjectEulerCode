import math

def pythagorean_triplet(sum_upto):
	a=1
	while a<=250:
		b=499
		while b>=250:
			c=sum_upto-a-b
			temp= math.sqrt(a**2+b**2)

			print a,b,temp
			if temp==c:
				print a ,b, c
				return a*b*c
			b-=1
		a+=1

print pythagorean_triplet(1000)
