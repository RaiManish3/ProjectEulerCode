import time
import math
begin=time.time()

####################################################################
# ========================EXEVUTION TIME:6s=========================

"""
	INITIALLY I WORKED ON A SORT OF BRUTE FORCE METHOD USING
	LISTS ADDITION AND ALL, BUT IT WAS NOT EFFECTIVE AT ALL.
	SO FOR THIS CODE, SOURCE: MATHBLOG!

	SEE HERE WE ARE DOING THE CALCULATION FOR THE LAST AND FIRST
	9-DIGITS SEPERATELY.

	THE LAST 9-DIGITS ARE SIMPLE, WE JUST TAKE THE REQUIRED MODULO
	BUT THE FIRST 9-DIGITS REQUIRE SOME INSIGHTS.
		F{n}=phi^{n}/root{5} ;  for large n , where phi= golden ratio= (root(5)+1)/2
		Take log both sides
		log F = n*log(phi)-log(root(5))
			  = t
		NOW TO GET THE FIRST 9 DIGITS OF F{n} WE OBSERVE THAT
		10^1 gives 2 digit number	===> 10^8 should give 9 digit number
		NOW THE THING THAT SPECIFIES THE VALUE OF 10^x IS ACTUALLY THE
		FRACTIONAL PART OF 'x'. VERIFY YOURSELF!

	SO FOR FIRST 9 DIGITS WE HAVE 10^{fractional_part(t)+8}
"""

refer="123456789"
k_val=2
f1,f2=1,1
last_9=10**9

while 1:
	f1,f2=f2,(f1+f2)%last_9
	k_val+=1
	print k_val
	strx=str(f2)
	strx_sorted=''.join(sorted(strx))
	if strx_sorted==refer:
		t=k_val*0.20898764024997873 - 0.3494850021680094
		stry=str(long(10**(t-long(t)+8)))
		stry_sorted=''.join(sorted(stry))
		if stry_sorted==refer:
			print k_val
			break

print time.time()-begin