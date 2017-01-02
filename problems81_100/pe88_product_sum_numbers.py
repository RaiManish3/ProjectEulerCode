##############################################################

"""
	SOURCE : DREAMSHIRE.
	WHAT I UNDERSTOOD:
	THE REASON WHY k=p-s+c is that we can make for the 
	required 'k' by taking a smaller number of factors
	such that their product is 'p' and sum is 's' , suppose
	p>=s then we can add "p-s" 1's or equivalently "k-c" 1's.
	thus the formula.

	next we need the minimal product-sum thats why n[k]=p
	is p< previous n[k]'s (or say previous p's).

	then we recursive check for all factors, by multiplying to existing
	product and sum and increasing the factor count by 1.

	also the next factor to be analysed starts from 'i'.
	
"""

def prodsum(p, s, c, start):
    k = p - s + c     # product - sum + number of factors
    if k < kmax:
        if p < n[k]: n[k] = p
        for i in xrange(start, kmax//p*2 + 1):
           	prodsum(p*i, s+i, c+1, i)


kmax=int(raw_input("ENTER THE k_max: "))
kmax+=1
n=[2*kmax]*(kmax)
prodsum(1,1,1,2)

print sum(set(n[2:]))