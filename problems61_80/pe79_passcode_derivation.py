
def crack_passcode():
	f=open('p079_keylog.txt','r')
	lst=[]

	for i in xrange(50):
		str1=f.readline()
		l=list(str1)

		if l[0] in lst and l[1] in lst:
			if lst.index(l[0])>lst.index(l[1]):
				ind=lst.index(l[1])
				ind2=lst.index(l[0])
				lst.remove(l[0])
				lst.remove(l[1])
				lst.insert(ind,l[0])
				lst.insert(ind2,l[1])

		if l[1] in lst and l[2] in lst:
			if lst.index(l[1])>lst.index(l[2]):
				ind=lst.index(l[2])
				ind2=lst.index(l[1])
				lst.remove(l[1])
				lst.remove(l[2])
				lst.insert(ind,l[1])
				lst.insert(ind2,l[2])
			

		if l[0] not in lst:
			if l[1] not in lst:
				if l[2] not in lst:
					lst.append(l[0])
					lst.append(l[1])
					lst.append(l[2])
				else : 
					ind=lst.index(l[2])
					lst.insert(ind,l[1])
			else:
				ind=lst.index(l[1])
				lst.insert(ind,l[0])


		elif l[2] not in lst:
			if l[0] not in lst:
				ind=lst.index(l[1])
				lst.insert(ind,l[0])
			ind=lst.index(l[1])
			lst.insert(ind+1,l[2])

		elif l[1] not in lst:
			if l[2] not in lst:
				ind=lst.index(l[0])
				lst.insert(ind+1,l[0])
			ind=lst.index(l[2])
			lst.insert(ind,l[1])

	str2=''.join(lst)
	return str2

print crack_passcode()
