import math
import time
start=time.time()

########################################################################################
# =============================EXECUTION TIME:0.05s==================================

"""
	BRUTE FORCING BASICALLY;
	IDEA IS SIMPLE MAKE LISTS FOR ALL POOLYGONAL TYPE NUMBERS(4-DIGIT),

	I HAVE CHOSEN A NUMBER FROM OCTAGONAL DOMAIN ('MAIN' FUNCTION DOES THIS)
	AND THEN SEARCHED FOR THE REQUIRED CONDITIONS THROUGH OTHER DOMAINS;

	ORDER_FIGURATE_SET IS A RECURSIVE FUNCTION WHICH SORT OF WORKS ON SAME 
	CONDTIONS AND FINDS A CYCLE.

"""

# ------------------------CHECKS FOR POLYGONALITY-----------------------------------
def isTriangle(t):
	n=(-1+math.sqrt(1+8*t))/2
	if n==int(n):
		return 1
	return 0

def isSquare(t):
	n=math.sqrt(t)
	if n==int(n):
		return 1
	return 0

def isPentagonal(t):
	n=(1+math.sqrt(1+24*t))/6
	if n==int(n):
		return 1
	return 0

def isHexagonal(t):
	n=(1+math.sqrt(1+8*t))/4
	if n==int(n):
		return 1
	return 0

def isHeptagonal(t):
	n=(3+math.sqrt(9+40*t))/10
	if n==int(n):
		return 1
	return 0

def isOctagonal(t):
	n=(2+math.sqrt(4+12*t))/6
	if n==int(n):
		return 1
	return 0

# -------------------------------------------------------------------------------

# ----------------------MAKE POLYGONAL LISTS-------------------------------------

l_triangle,l_square,l_pentagonal,l_hexagonal,l_heptagonal,l_octagonal=[],[],[],[],[],[]

def make_figurate_lists(digit):
	start=10**(digit-1)
	stop=10**(digit)
	for i in xrange(start,stop):
		if isTriangle(i):
			l_triangle.append(str(i))
		if isSquare(i):
			l_square.append(str(i))
		if isPentagonal(i):
			l_pentagonal.append(str(i))
		if isHexagonal(i):
			l_hexagonal.append(str(i))
		if isHeptagonal(i):
			l_heptagonal.append(str(i))
		if isOctagonal(i):
			l_octagonal.append(str(i))


# ----------------------------------------------------------------------------

# ---------------------------RECURSIVELY FIND THE CYCLE---------------------------------------

make_figurate_lists(4)
lst=[0,0,0,0,0,0]
found=0

def order_figurate_set(start_phrase,original_phrase,flag):
	global found

	if flag[0] and found==0:
		for i in l_heptagonal:
			if i[:2]==start_phrase:
				flag[0]=0
				lst[1]=i
				order_figurate_set(i[2:],original_phrase,flag)
				if found==1:
					return
		flag[0]=1

	if flag[1] and found==0:
		for i in l_hexagonal:
			if i[:2]==start_phrase:
				flag[1]=0
				lst[2]=i
				order_figurate_set(i[2:],original_phrase,flag)
				if found==1:
					return
		flag[1]=1

	if flag[2] and found==0:
		for i in l_pentagonal:
			if i[:2]==start_phrase:
				flag[2]=0
				lst[3]=i
				order_figurate_set(i[2:],original_phrase,flag)
				if found==1:
					return
		flag[2]=1


	if flag[3] and found==0:
		for i in l_square:
			if i[:2]==start_phrase:
				flag[3]=0
				lst[4]=i
				order_figurate_set(i[2:],original_phrase,flag)
				if found==1:
					return
		flag[3]=1

	if flag[4] and found==0:
		for i in l_triangle:
			if i[:2]==start_phrase:
				flag[4]=0
				lst[5]=i
				order_figurate_set(i[2:],original_phrase,flag)
				if found==1:
					return
		flag[4]=1

	if 1 not in flag:
		if start_phrase==original_phrase:
			found=1
			return

# ------------------------------------------------------------------------------------ 

def main():
	global found
	for x in l_octagonal:
		order_figurate_set(x[2:],x[:2],[1,1,1,1,1])
		if found==1:
			lst[0]=x
			print lst
			return


main()
lst=list(map(int,lst[:]))
print sum(lst)
print time.time()-start
# ===================================================================================