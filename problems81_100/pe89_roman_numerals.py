import time
begin=time.time()

#####################################################################
# =======================EXECUTION TIME: 17ms========================

"""
	BASICALLY I FIRST BUILT UP THE DECIMAL AND THEN CALCULATED THE 
	REQUIRED DIFFERENCE.
"""

roman_char_map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def diff_minimal_and_given(num,l):
	result=0
	n_str=str(num)
	ll=len(n_str)
	ind=0								
	for i in n_str:
		if i=='4' or i=='9':
			if ind==0 and ll==4:
				result+=int(i)
			else: result+=2
		elif i in ['5','6','7','8']:
			result+=int(i)-4
		elif i in ['1','2','3']:
			result+=int(i)
		ind+=1

	return l-result


def main():
	f=open('p089_roman.txt','r')
	t_count=0

	for lines in f.readlines():
		lines=lines[:-1]
		num,flag=0,0

		# EXTRACT THE SUM

		for a in lines:

			if flag==1:
				flag=0
				continue

			ind1=lines.index(a)+1

			if a=='I':
				if ind1<len(lines):
					if lines[ind1]=='X':
						num+=roman_char_map['X']-roman_char_map[a]
						flag=1
						continue
					elif lines[ind1]=='V':
						num+=roman_char_map['V']-roman_char_map[a]
						flag=1
						continue

			if a=='X':
				if ind1<len(lines):
					if lines[ind1]=='L':
						num+=roman_char_map['L']-roman_char_map[a]
						flag=1
						continue
					elif lines[ind1]=='C':
						num+=roman_char_map['C']-roman_char_map[a]
						flag=1
						continue

			if a=='C':
				if ind1<len(lines):
					if lines[ind1]=='D':
						num+=roman_char_map['D']-roman_char_map[a]
						flag=1
						continue
					elif lines[ind1]=='M':
						num+=roman_char_map['M']-roman_char_map[a]
						flag=1
						continue

			num+=roman_char_map[a]

		# COUNT THE DIFFERENCE
		t_count+=diff_minimal_and_given(num,len(lines))

	return t_count

# print main()
# print time.time()-begin