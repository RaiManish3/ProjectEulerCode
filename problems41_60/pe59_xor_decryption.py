# XOR -->	a ^ b
import sys
import time
start=time.time()

######################################################################################
# ================================EXECUTION TIME: 0.1s================================

"""
	I MUST CONFESS THAT I DON'T KNOW MUCH ABOUT ECRYPTION/DECRYPTION;
	SO I RELIED ON BRUTE FORCING THOUGH LATER I CAME TO KNOW ABOUT AN
	EFFICIENT METHOD (FREQUENCY ANALYSIS) WHICH MAKES THE CODE SIMPLER AS WELL AS
	MORE LOGICAL.

	THE CHARACTER SET I MADE IS OF [LOWERCASE LETTER, UPPERCASE LETTER, NUMERALS
	SPACE,PUNTUATIONS-HYHENS,COMMAS,SINGLE AND DOUBLE QUOTE,EXCLAMATION MARK,PARENTHESIS,FORWARD SLASH,COLON
	SEMI-COLON,QUESTION-MARK]

	THESE ALL ARE COMMONLY USED IN ENGLISH LAGUAGUE SO I WENT THAT WAY. 

	NOTE: REFER TO ASCII CHAR SET

	-------------------------------UPDATE----------------------------------------

	READ ABOUT FREQUENCY ANALYSIS:
	IMPLEMENTED THAT IN CODE BELOW IN FUNCTION XOR_DECRYPT_FREQUENCY()

	NOTE: HERE 'SPACE' IS THE MOST OCCURING CHARACTER RATHER THAN 'E'
"""

def read_file(file_name):
	f=open(file_name,'r')
	str1=f.read()
	f.close()
	l1=list(str1.split(','))
	return list(map(int,l1[:]))

# def xor_decrypt():
# 	lst=read_file('p059_cipher.txt')
# 	l=len(lst)
# 	char_set=[i for i in xrange(95,123)]

# 	for i in xrange(65,91):
# 		char_set.append(i)

# 	l1=[32,33,34,39,40,41,44,45,46,47,58,59,63]
# 	for i in l1:
# 		char_set.append(i)

# 	for i in xrange(48,58):
# 		char_set.append(i) 

# 	f2=open('pe059_message.txt','a')
# 	for i in xrange(97,123):
# 		for j in xrange(97,123):
# 			for k in xrange(97,123):
# 				key="%c%c%c\n"%(i,j,k)
# 				str2="key=%s\n"%(key)
# 				sum_ascii=0
# 				for x in xrange(l):
# 					if x%3==0:
# 						w=lst[x]^i
# 					if x%3==1:
# 						w=lst[x]^j
# 					if x%3==2:
# 						w=lst[x]^k

# 					if w not in char_set:
# 						str2=""
# 						break
# 					sum_ascii+=w
# 					word="%c"%(w)
# 					str2+=word
# 				if str2!="":
# 					f2.write(str2)
# 					f2.write("\nascii_sum=%d\n"%(sum_ascii))

# 	f2.close()


# xor_decrypt()
# print time.time()-start
# --------------------------------------testing------------------------------------
# a="%c "%(87^39)
# print a



####################################################################################
# ============================EXECUTION TIME: 1ms===================================

def xor_decrypt_frequency():
	lst=read_file('p059_cipher.txt')
	l=len(lst)
	key=[0,0,0]
	space_ascii=32

# -------------------for key-----------------------------------
	for j in xrange(0,3):

		ll=[0 for i in xrange(100)]
		for x in xrange(j,l,3):
			ll[lst[x]]+=1

		m=max(ll)
		index=ll.index(m)

		for i in xrange(97,123):
			if i^index==space_ascii:
				key[j]=i
				break
# -------------------------------------------------------------

	# print "%c%c%c\n"%(key[0],key[1],key[2])
	sum_ascii=0

	for x in xrange(0,l):
		sum_ascii+=lst[x]^key[x%3]

	return sum_ascii


# print xor_decrypt_frequency()
# print time.time()-start

# ===================================================================================