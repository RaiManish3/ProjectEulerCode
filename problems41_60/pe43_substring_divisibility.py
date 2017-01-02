import time
start=time.time()

######################################################################################
# ==========================execution time:0.2s========================================


lst=[]

def gen_pandigital_for_digit(digits,str_num,count):
	global lst

	# checks for required condition breaks unwanted cases
# ----------------------------------------------------------------------------
	if count==4:
		if int(str_num[1:4])%2!=0:
			return

	if count==5:
		if int(str_num[2:5])%3!=0:
			return

	if count==6:
		if int(str_num[3:6])%5!=0:
			return

	if count==7:
		if int(str_num[4:7])%7!=0:
			return

	if count==8:
		if int(str_num[5:8])%11!=0:
			return

	if count==9:
		if int(str_num[6:9])%13!=0:
			return

	if count==digits:
		if int(str_num[7:10])%17!=0:
			return
		lst.append(int(str_num))
		return
# -----------------------------------------------------------------------------------

	for x in xrange(9,-1,-1):
		if str(x) in str_num:
			continue

		str_num+=str(x)
		count+=1

		gen_pandigital_for_digit(digits,str_num,count)
		str_num=str_num[:-1]
		count-=1

def main():
	gen_pandigital_for_digit(10,'',0)
	return sum(lst)

print main()
print time.time()-start
									
