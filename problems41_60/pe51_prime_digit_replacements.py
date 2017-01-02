import max_prime_under as mp
import time
start=time.time()

#######################################################################################
# ====================================EXECUTION TIME:0.2s=============================

"""
	YOU CAN FIND A MORE EFFICIENT CODE AT 'MATHBLOG' BUT THIS IS HOW I IMPLEMENTED THE CODE.
	BASICALLY MY WORK INCLUDES SOME ASSUMPTIONS AS WELL AS SOME SHORTCUTS.
	$ASSUMPTION : I ASSUME THAT I WILL BE ABLE TO FIND FIND THE NUMBER WITHIN 6 DIGIT LIMIT
				  FURTHER BELOW 56003 THERE IS NO SUCH NUMBER.

	$TRICK (RATHER SOME OBSERVATIONS I SHOULD CALL) : SEE WE WANT 8 FAMILY MEMBERS WHOSE ANY
	NUMBER OF ELEMENTS CAN REPEAT TO GENERATE ANOTHER PRIME ONLY. 
	I WENT FOR THE LOWEST REPEATING DIGITS ATLEAST ONE OF WHICH WILL BE REQUIRED TO COMPLETE THE FAMILY.
	THEY ARE 0,1,2.

	NOW HERE'S THE THING,
	A NUMBER WHOSE SUM OF DIGITS IF DIVISIBLE BY 3 IS NEVER PRIME.
	SUPPOSE THERE IS ONLY ONE REPEATED DIGIT, THEN AFTER YOU INCREMENT THAT DIGIT BY 
	CERTAIN AMOUNT YOU'LL FIND THAT ALTEAST THREE MEMBERS OF THE FAMILY ARE DIVISIBLE BY 3

	SAME IS THE CASE OF 2,4,5 DIGIT REPEAT.

	SO WITHOUT LOSS OF GENERALITY, WE CAN NARROW OUR SEARCH DOMAIN TO 3 REPEAPTED DIGITS ONLY.

	FUNCTIONS: CHECK_COM():
			   WHEN FOUND A PRIME NUMBER WITH 3 REPEATED DIGIT, THE FUNCTION CHECKS FOR ALL COMBINATION
			   BY INCREAMENTING THE REPEATED DIGITS AND MAINTAINS A COUNT OF PRIMES.

				MAIN():
				GENERATES ODD NUMBER, CHECKS IF 3 DIGIT REPEATED AND ALSO IF IT IS PRIME
				THEN PASSES TO CHECK_COM AND FINALLY BREAKS OUT WHEN REQUIRED CONDITION IS
				MET

"""

num_dic={'number':56003,'family-size':7}

def check_com(x,l1,i,j,k):
	l2=l1[:]

	count=1
	for m in xrange(1,10):
		l2[i]=str((int(l1[i])+m)%10)
		l2[j]=l2[i]
		l2[k]=l2[i]
		
		str2=''.join(l2)

		if mp.isPrime(int(str2)):
			if l2[0]=='0':
				count-=1
			count+=1


	if count>num_dic['family-size']:
		num_dic['family-size']=count
		num_dic['number']=x




def main():

	for x in xrange(56003,1000000,2):
		str1=str(x)
		l1=list(str1)
		digits=len(str1)
		ll1=len(l1)
		
		if len(set(l1))!=ll1:
			if mp.isPrime(x):
				for i in xrange(ll1-1):
					num=l1[i]
					if num in ['0','1','2']:
						if num in l1[i+1:ll1-1]:
							j=l1[i+1:].index(num)+(i+1)
							if num in l1[j+1:ll1-1]:
								k=l1[j+1:].index(num)+(j+1)
								check_com(x,l1,i,j,k)


		if num_dic['family-size']==8:
			break


main()
print num_dic
print time.time()-start




######################################################################################
# -------------------------------testing----------------------------------------
# l1=['1','2','3']
# print list(map(int,l1[:]))
# print int('1')+1

# n=[1,2,4,2,4,6,3,3]
# num=4
# if num in n:
# 	print n[3:].index(num)