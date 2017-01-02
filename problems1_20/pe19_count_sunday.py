# ---------------------------LEAP YEAR FUNCTION--------------------------
def leap(year):

	if year%4==0:
		if year%100==0 and year%400!=0:
			return 28
		else: return 29

	return 28

# --------------------------DICTIONARY FOR CORRESPONDING DAYS OF MONTH-----------

def data_days(x,year):
	if x!=2:
		return {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:30}[x]
	return leap(year)


# ----------------------------COUNTING MONTH FOR WHICH SUNDAY IS THE FIRST DAY-------

def count_sundays(residue_index,s_year,e_year):
	count,month=0,1
	y=s_year   #y------>year
	# countp=0

	for i in xrange((e_year-s_year+1)*12):
		# residue_index holds the index of first day of upcoming month

		if residue_index==0:            #implies start of month to be sunday
			count+=1

		# UNCOMMENT BELOW TO SEE MONTH WISE SUNDAY COUNT
		# print "residue_index=%d and count_this=%d" %(residue_index,count-countp)
		# countp=count

		residue_index=(residue_index+data_days(month,y))%7 

		month=(month+1)%12

		if month==0: 
			month=12
		if month==1:
			y+=1

	return count


# print count_sundays(2,1901,2000)
