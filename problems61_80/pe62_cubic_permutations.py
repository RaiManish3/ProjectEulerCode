import time
start_time=time.time()
########################################################################################
# ===============================EXECUTION TIME:1.7s=========================================

"""
	I MUST CONFESS THAT INITIALLY I CAME UP WITH WORST SORT OF BRUTE FORCE TECHNIQUE.
	BUT THANKS TO MATHBLOG, THAT I WAS ABLE TO COMPREHEND A MUCH BETTER SOLUTION.

	SO HERE IT GOES:
	MANTAIN A DICTIONARY OF HIGHEST PERMUTATION OF A CUBE YOU COME ACROSS,
	INCREMENT THE COUNTER AS AND WHEN YOU HAVE CUBE MAPPING TO SAME HIGHEST
	PERMUTATION.
	WHEN COUNTER FOR ANY BELLS FIVE, WE ARE DONE.
"""

permutated_dic={}

def make_highest_permutation(cube):
	k=list(str(cube))
	k.sort()
	k.reverse()
	str1=''.join(k)
	return int(str1)

def main2(start):
	while 1:
		cube=start**3
		high_perm=make_highest_permutation(cube)
		if high_perm in permutated_dic.keys():
			permutated_dic[high_perm][0]+=1
			if permutated_dic[high_perm][0]==5:
				return permutated_dic[high_perm][1]
		else:
			lst=[1,cube]
			permutated_dic[high_perm]=lst
		start+=1


# print main2(346)
# print time.time()-start_time