# from operator import add         #this adds list elements componentwise
# l1,l2=[1,2,3],[1,2,3]
# print map(add,l1,l2)


lst=[]

def take_int():
	str1=raw_input()
	return list(map(int,str1.split()))

# --------------------------------------Take Multiline Input-------------------------------
def input_data(lines):
	global lst
	for i in xrange(1,lines+1) :
		tmp=[]
		tmp=take_int()
		lst.append(tmp)


# ---------------------------------------BOTTOM UP ARROACH---------------------------

def bottom_ups(lines):
	input_data(lines)
	
	i=lines-1
	while i>0:
		j=0
		while j<i:
			k=j+1
			if lst[i][j]>lst[i][k]:
				lst[i-1][j]+=lst[i][j]
			else:
				lst[i-1][j]+=lst[i][k]
			j+=1
		i-=1


# bottom_ups(100)
# print lst[0][0]
