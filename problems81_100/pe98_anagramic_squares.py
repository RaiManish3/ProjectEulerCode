import math
import time

##########################################################################
# ==================EXECUTION TIME: 50s===================================

"""
	METHOD: BRUTE FORCE
	BASICALLY IN ANAGRAMIC_MAIN FUNCTION I SEARCHED FOR THE PAIRS,
	AND IN ALPHA_TO_NUMERAL I CREATED A NUMBER CORRESPONDING TO THE
	STRING AND CHECKED IF IT WAS A SQUARE THEN IF OTHER PARTNER IS
	ALSO A SQUARE, WE HAVE OUR RESULT.

"""

begin=time.time()
m=0
words=[]

def alpha_to_numberal(strx,index,l1,num_lst,stry):
	global m

# PATTERN MAKES A SQUARE OR NOT
	if index==len(strx):
		num_str=int(''.join(map(str,num_lst)))
		n=math.sqrt(num_str)
		if n==int(n):
			str_num_int=0
			for i in xrange(len(stry)):
				ind3=strx.find(stry[i])
				str_num_int=str_num_int*10+num_lst[ind3]
				if i==0 and str_num_int==0:
					return
			n2=math.sqrt(str_num_int)
			if n2==int(n2):
				ml=max(num_str,str_num_int)
				if m<ml:
					m=ml
					words.append([strx,stry])
		return

# GENERATE THE NUMBER FOR THE STRING PATTERN
# THIS IS WHERE I BELIEVE THE INEFFICIENCY LIES
	for i in l1:
		if index==0 and i==0:
			return
		if strx[index] in strx[:index]:
			num_lst[index]=num_lst[strx.find(strx[index])]
			alpha_to_numberal(strx,index+1,l1,num_lst,stry)
			return
		else:
			num_lst[index]=i
			ind2=l1.index(i)
			l1.remove(i)
			alpha_to_numberal(strx,index+1,l1,num_lst,stry)
			l1.insert(ind2,i)



def anagramic_main():
	f=open('p098_words.txt','r')
	str1=f.read()
	lst=list(str1.split(','))
	# SORT BY LENGTH OF STRING
	lst.sort(key= len,reverse=True)
	l=len(lst)
	ll=[]
	ind=[]
	global m

	for x in xrange(l):
		# print x,m
		strx=''.join(sorted(lst[x]))
		if strx in ll:
			index=ind[ll.index(strx)]
			alpha_to_numberal(lst[index],0,[9,8,7,6,5,4,3,2,1,0],[0 for i in xrange(len(strx))],lst[x])
			if m>0:
				return m
		else :
			ll.append(strx)
			ind.append(x)

# print anagramic_main()
# print words
# print time.time()-begin