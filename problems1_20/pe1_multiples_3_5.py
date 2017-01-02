# -----------------------------my approach------------------------------
# n1=3
# n2=5
# t=1000.0

# s1,s2,s3=0,0,0

# for i in range(int(t)):
# 	if i<(t/n1):
# 		s1+=n1*i
# 	else :
# 		break

# 	if i<(t/n2):
# 		s2+=n2*i

# 	if i<(t/(n1*n2)):
# 		s3+=(n1*n2)*i

# 	print "i=", i , "s1=", s1 , "s2=", s2, "s3=", s3 

# print s1+s2-s3;


# ----------------------------one-liner---------------------------------
print sum( x for x in range(1000) if 0 in [x%3, x%5])