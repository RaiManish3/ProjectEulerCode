import time
begin=time.time()

###############################################################################
# ============================EXECUTION TIME:10ms==============================

"""
	USED A BIT OF GEOMETRY:
	WE NEED THE POINT TO BE ON THE SAME SIDE OF THE THREE SIDES OF TRIANGLES, TREATING
	EACH SIDE AS VECTOR(ACCOMPLISHED BY TAKING CIRCULAR PERMUTATION OF VERTICES FOR CHECK)

	EQN OF LINE : (y-y1)/(x-x1)=(y2-y1)/(x2-x1)
				=> (x2-x1)*(y-y1)-(y2-y1)*(x-x1)=0
	PUT THE POINT TO BE CHECKED ON THE LEFT HAND SIDE EXPRESSION AND EVALUTE THE SIGN
	FOR IT.

	AS I SAID IF ALL SIGNS MATCH, WE HAVE REQUIRED TRIANGLE ELSE WE DON'T.
"""

def check(x1,y1,x2,y2):
	tmp=-y1*(x2-x1)+x1*(y2-y1)
	if tmp>0:
		return 1
	elif tmp<0:
		return -1
	return 0

def main():
	count=0
	f=open('p102_triangles.txt','r')
	for i in xrange(1000):
		str1=f.readline()
		str1=str1[:-1]
		lst=list(map(int,str1.split(',')))
		sign=[0,0,0]
		for i in xrange(3):
			sign[i]=check(lst[2*i],lst[2*i+1],lst[2*(i+1)%6],lst[2*(i+1)%6+1])
		if 0 in sign:
			continue
		if sign[0]==sign[1] and sign[1]==sign[2]:
			count+=1
	return count

print main()
print time.time()-begin