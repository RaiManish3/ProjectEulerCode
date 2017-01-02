import time
begin=time.time()

##############################################################
# ===================EXECUTION TIME: 0.1ms====================

"""
	BASICALLY I EMPLOYED PELL'S EQUATION HERE.
	IF YOU ARE WONDERING, HERE'S THE OBSERVATION I MADE:
		WE WANT  {b}C{2}/{b+r}C{2}=1/2
		SOLVING FOR b GIVES: b= (1+2r+sqrt(1+8r^2))/2
		this b is an integer when 1+8r^2 is odd square
				=>1+8r^2=n^2
				or n^2-8r^2=1  which is Pell's equation

		the first solution for the above eqn is n=3,r=1
		now next solutions are given by the equation as in line 23
"""

r,n=1,3

while 1:
	n,r=n*3+8*r,3*r+n
	if n%2==1:
		b=(1+2*r+n)/2
		if b+r>10**12:
			print b
			break

print time.time()-begin