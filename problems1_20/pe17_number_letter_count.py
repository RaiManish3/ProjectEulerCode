
def digit_data1(number):
	return {
		0:0,1: 3,2: 3,3: 5,4: 4,5: 4,6: 3,7: 5,8: 5,9: 4,20: 6, 30:6,40:5,50:5,60:5,70:7,80:6,90:6
	}[number]

def digit_data2(number):
	return {
		10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8
	}[number]

count=0

def count_tens(i):
	global count
	tmp=i
	tmp=tmp/10
	if tmp ==1:
		count+=digit_data2(i)
	else :
		count+=digit_data1(tmp*10)
		count+=digit_data1(i%10)


def sum_digit(start,number):
	global count
	count_p=0
	for i in xrange(start,number+1):
		count_p=count
		tmp=i
		if tmp>=100:
			count+=digit_data1(tmp/100)
			count+=7 					#for hundred=7
			tmp=tmp%100
			if tmp!=0:
				count+=3				#for and =3

		if tmp>=10:
			count_tens(tmp)

		if tmp<10:
			count+=digit_data1(tmp)

		# print "i=%d and this_count= %d"%(i,count-count_p)		


sum_digit(int(raw_input("enter start: ")),int(raw_input("enter a number: ")))

# print count
