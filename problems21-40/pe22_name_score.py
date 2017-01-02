# for the names file I removed all punctuations using sed replacement

f=open('names.txt','r')
str1=f.readline()

lst=list(str1.split())
lst.sort()

# print lst

l=len(lst)
t_count=0

for i in xrange(l):
	l1=len(lst[i])
	i_count=0
	for j in xrange(l1):
		tmp=lst[i][j]
		if tmp>='a' and tmp<='z':
			i_count+=ord(tmp)-ord('a')+1
		elif tmp>='A' and tmp<='Z':
			i_count+=ord(tmp)-ord('A')+1
	t_count+=(i_count)*(i+1)


print t_count
# print lst[937]
