a=[1,2,0]
i=1
sumup=2

while a[i]<4000000:
	i+=1

	a.insert(i,a[i-1]+a[i-2])

	if a[i]%2==0:
		sumup+=a[i];
	print a[i], sumup
	# print