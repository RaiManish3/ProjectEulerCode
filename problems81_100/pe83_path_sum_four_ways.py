
# source http://problematicsets.com/project-euler-83-minimal-path-sums-using-dijkstras-algorithm/
import time
begin=time.time()

f=open('p083_matrix.txt','r')
grid={}
row_now=1

for line in f:
	tmp=line.replace('\n','')
	tmp=tmp.split(',')
	for a in xrange(len(tmp)):
		grid[(row_now,a+1)]=int(tmp[a])
	row_now+=1

rows,cols=80,80

def findNeighbours(vertex):
	i,j=vertex[0],vertex[1]
	output=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
	remove=[]

	for x in output:
		if x[0]<1 or x[0]>rows or x[1]<1 or x[1]>cols:
			remove.append(x)

	final=[x for x in output if not x in remove]
	return final

def dka(graph,source):
	dist={}
	for v in graph:
		dist[v]=float("inf")
	dist[source]=graph[source]
	Q=dist.copy()
	length=len(Q)
	while length>0:
		u=min(Q,key=Q.get)
		if dist[u]==float("inf"):
			break
		if u==(rows,cols):
			break
		del Q[u]
		length-=1
		n=findNeighbours(u)
		neighbours=[x for x in n if x in Q]
		for v in neighbours:
			alt=dist[u]+grid[v]
			if alt<dist[v]:
				dist[v]=alt
				Q[v]=alt
	return dist

answerGrid=dka(grid,(1,1))

print answerGrid[(rows,cols)]
print time.time()-begin