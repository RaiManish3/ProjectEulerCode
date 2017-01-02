import time
start=time.time()

##########################################################################################
# ===============================EXECUTION TIME: 0.2s=======================================

"""
	THE CODE IS RATHER LENGTHY. I JUST WORKED UPON A BASIC IDEA OF FUNCTIONAL PROGRAMMING
	MADE A CODE FOR EACH HAND. AND A SUPPLEMENTARY FUNCTION 'MAKE AND BREAK STRINGS' WHICH
	GENERATES A HANDSOME LIST FOR COMPARISON.
	THEN MAIN FUNCTION GETS CONNECTED TO THESE THROUGH FUNCTION 'WHAT_HAND_IS_IT'

	THE 'MAIN' FUNCTION:
	THERE ARE FOUR SUITS, SO I DECIDED TO STORE EACH PLAYERS DATA IN THE ORDER OF THE CARD
	SUIT; 0 BEING 'C',1 ->'D', 2->'H', 3->'S'
	ALSO ASSIGNED VALUES TO SPECIAL CARDS, T->10, J->11, Q->12, K->13, A->14

"""

def make_and_break_string(player_list):
	str2=''
	for i in xrange(4):
		l=len(player_list[i])
		for j in xrange(l):
			str2+=str(player_list[i][j])+','
	str2=str2[:-1]
	l1=list(str2.split(','))
	return list(map(int,l1[:]))

def high_hand(player_list):
	l_tmp=make_and_break_string(player_list)
	l_tmp.sort()
	return [10,l_tmp[-1],l_tmp[-2]]

def one_pair(player_list):
	l_tmp=make_and_break_string(player_list)
	l_tmp.sort()
	for i in xrange(4):
		if l_tmp[i]==l_tmp[i+1]:
			return [9,l_tmp[i],l_tmp[-1]]
	return [0]			
		
def two_pair(player_list):
	l_tmp=make_and_break_string(player_list)
	l_tmp.sort()
	l1=[]
	for i in xrange(4):
		if l_tmp[i]==l_tmp[i+1]:
			l1.append(l_tmp[i])
	if len(l1)==2:
		return [8,max(l1[0],l1[1]),min(l1[0],l1[1])]
	return [0]
	

def three_of_a_kind(player_list):
	l_tmp=make_and_break_string(player_list)
	l_tmp.sort()
	for i in xrange(3):
		if l_tmp[i]==l_tmp[i+2]:
			return [7,l_tmp[i],l_tmp[-1]]
	return [0]


def straight(player_list):
	l_tmp=make_and_break_string(player_list)
	l_tmp.sort()
	for i in xrange(4):
		if l_tmp[i+1]!=l_tmp[i]+1:
			return [0]

	return [6,l_tmp[-1],l_tmp[-2]]



def flush(player_list):
	for i in xrange(4):
		if len(player_list[i])==5:
			player_list[i].sort()
			return [5,player_list[i][-1],player_list[i][-2]]
	return [0]

def full_house(player_list):
	l_tmp=make_and_break_string(player_list)
	l_tmp.sort()

	if l_tmp[0]==l_tmp[2] and l_tmp[3]==l_tmp[4]:
		return [4,l_tmp[0],l_tmp[3]]
	if l_tmp[0]==l_tmp[1] and l_tmp[2]==l_tmp[4]:
		return [4,l_tmp[2],l_tmp[0]]
	return [0]

def four_of_a_kind(player_list):
	l_tmp=make_and_break_string(player_list)
	l_tmp.sort()
	for i in xrange(2):
		if l_tmp[i]==l_tmp[i+3]:
			return [3,l_tmp[i],l_tmp[-1]]
	return [0]


def straight_flush(player_list):
	for i in xrange(4):
		if len(player_list[i])==5:
			l_tmp=make_and_break_string(player_list)
			l_tmp.sort()
			if l_tmp[1]==l_tmp[0]+1:
				if l_tmp[2]==l_tmp[0]+2:
					if l_tmp[3]==l_tmp[0]+3:
						if l_tmp[4]==l_tmp[0]+4:
							return [2,l_tmp[-1],l_tmp[-2]]

	return [0]

def royal_flush(player_list):
	l_tmp=straight_flush(player_list)
	if l_tmp[0]:
		if l_tmp[1]==14:
			return [1,14,13]
	return [0]


def what_hand_is_it(player_list):
	l_tmp=royal_flush(player_list)
	if l_tmp[0]:
		return l_tmp
	l_tmp=straight_flush(player_list)
	if l_tmp[0]:
		return l_tmp
	l_tmp=four_of_a_kind(player_list)
	if l_tmp[0]:
		return l_tmp
	l_tmp=full_house(player_list)
	if l_tmp[0]:
		return l_tmp
	l_tmp=flush(player_list)
	if l_tmp[0]:
		return l_tmp
	l_tmp=straight(player_list)
	if l_tmp[0]:
		return l_tmp
	l_tmp=three_of_a_kind(player_list)
	if l_tmp[0]:
		return l_tmp
	l_tmp=two_pair(player_list)
	if l_tmp[0]:
		return l_tmp
	l_tmp=one_pair(player_list)
	if l_tmp[0]:
		return l_tmp
	return high_hand(player_list)
	
	

def main(upto):
	f=open('poker.txt','r')
	player1_count=0
	player2_count=0
	# s_count=[0 for x in xrange(10)]
	# s_count2=[0 for x in xrange(10)]

	for i in xrange(upto):
		str1=f.readline()
		str1=str1[:-1]
		lst=list(str1.split())
		player1_list=[[] for  x in xrange(4)]
		player2_list=[[] for  x in xrange(4)]

		for x in xrange(10):
			if lst[x][0]=='T':
				lst[x]='10'+lst[x][1:]

			elif lst[x][0]=='J':
				lst[x]='11'+lst[x][1:]

			elif lst[x][0]=='Q':
				lst[x]='12'+lst[x][1:]

			elif lst[x][0]=='K':
				lst[x]='13'+lst[x][1:]

			elif lst[x][0]=='A':
				lst[x]='14'+lst[x][1:]

			if lst[x][-1]=='C':
				if x<5:
					player1_list[0].append(int(lst[x][:-1]))
				else: player2_list[0].append(int(lst[x][:-1]))

			if lst[x][-1]=='D':
				if x<5:
					player1_list[1].append(int(lst[x][:-1]))
				else: player2_list[1].append(int(lst[x][:-1]))
			

			if lst[x][-1]=='H':
				if x<5:
					player1_list[2].append(int(lst[x][:-1]))
				else: player2_list[2].append(int(lst[x][:-1]))


			if lst[x][-1]=='S':
				if x<5:
					player1_list[3].append(int(lst[x][:-1]))
				else: player2_list[3].append(int(lst[x][:-1]))



		p1=what_hand_is_it(player1_list)
		p2=what_hand_is_it(player2_list)

		# s_count[p1[0]-1]+=1
		# s_count2[p2[0]-1]+=1


		if p1[0]<p2[0]:
			player1_count+=1
		elif p2[0]<p1[0]:
			player2_count+=1
		else:
			if p1[1]>p2[1]:
				player1_count+=1
			elif p1[1]<p2[1]:
				player2_count+=1
			else: 
				if p1[2]>p2[2]:
					player1_count+=1
				else: player2_count+=1

	# print s_count
	# print s_count2
	return player1_count,player2_count


print main(1000)
print time.time()-start

# =========================================================================================
# l1=['1','2','12']
# l2=list(map(int,l1[:]))
# print l2

# print make_and_break_string([[5], [3], [6, 2, 8, 13, 4], []])
