# -------------------------------CAN BE MADE MORE EFFICIENT-----------------------
# =================================EXECUTION TIME 7s==============================
import time

begin=time.time()

def div(x):
	count=1
	i=2
	stop=int(math.sqrt(x))
	while i<=stop: 						#make it loop till the sqrt(x) and add 2 to the counter.
		if x%i==0:
			count+=2
			# print i," count= ",count
		i+=1
	if stop*stop==x:
		count-=1
	return count

def num_gen(num_divisor):
	n=100
	while 1:
		term=(n*(n+1))/2
		# print term
		if div(term)>num_divisor:
			return term
		n+=1

print num_gen(500)
print time.time()-begin
# print div(76576500)
