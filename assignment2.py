import os
import re
import sys
import time

graphRE=re.compile("(\\d+)\\s(\\d+)")
edgeRE=re.compile("(\\d+)\\s(\\d+)\\s(\\d+)")

def BellmanFordHelper(G, V, E):
	

# https://www-m9.ma.tum.de/material/en/spp-bellman-ford/
def BellmanFord(G, V, E):
    pathPairs=[[-1 for i in range(V)] for j in range(V)]
    
    # Fill in your Bellman-Ford algorithm here
    # The pathPairs will contain a matrix of path lengths:
    #    0   1   2 
    # 0 x00 x01 x02
    # 1 x10 x11 x12
    # 2 x20 x21 x22
    # Where xij is the length of the shortest path between i and j
    
    print 'vertices: ' + str(V)
    print 'edges: ' + str(E)
    
    # from slides, W is G
    # initialize pathPairs
    for i in range(0,V):
		pathPairs[i][0] = 0
		for j in range(1,V-1):
			# check entire graph for valid edges or not, if the edge is infinity then
			for k in (0,V):
				for l in (0,V):
					if G[1][j][k] < float('inf'):
						if pathPairs[k]
				
	
	
			
    
    return pathPairs

def FloydWarshall(G, V):
    pathPairs=[[-1 for i in range(V)] for j in range(V)]
    # Fill in your Floyd-Warshall algorithm here
    # The pathPairs will contain a matrix of path lengths:
    #    0   1   2 
    # 0 x00 x01 x02
    # 1 x10 x11 x12
    # 2 x20 x21 x22
    # Where xij is the length of the shortest path between i and j
    
    # initialize pathPairs
    for i in range(0,V):
		for j in range(0,V):
			if i == j:
				pathPairs[i][j] = 0
			elif G[1][i][j] == float("inf"):
				pathPairs[i][j] = float("inf")
			else: 
				pathPairs[i][j] = int(G[1][i][j])
	
	# the meat of the algorithm	
    for k in range(0, V):
		for i in range(0,V):
			for j in range (0, V):
				# this if-statement is here in case of overflow problems
				# if pathPairs[i][k] != float("inf") and pathPairs[k][j] != float("inf"):
				if pathPairs[i][k] + pathPairs[k][j] < pathPairs[i][j]:
					pathPairs[i][j] = pathPairs[i][k] + pathPairs[k][j]
    
    return pathPairs

def readFile(filename):
    # File format:
    # <# vertices> <# edges>
    # <s> <t> <weight>
    # ...
    inFile=open(filename,'r')
    line1=inFile.readline()
    graphMatch=graphRE.match(line1)
    if not graphMatch:
        print(line1+" not properly formatted")
        quit(1)
    vertices=list(range(int(graphMatch.group(1))))
    edges=[]
    
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            row.append(float("inf"))
        edges.append(row)
        
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch=edgeRE.match(line)
        if edgeMatch:
            source=edgeMatch.group(1)
            sink=edgeMatch.group(2)
            if int(source) >= len(vertices) or int(sink) >= len(vertices):
                print("Attempting to insert an edge between "+str(source)+" and "+str(sink)+" in a graph with "+str(len(vertices))+" vertices")
                quit(1)
            weight=edgeMatch.group(3)
            edges[int(source)][int(sink)]=weight
                
    return (vertices,edges)

def writeFile(lengthMatrix,filename):
    filename=os.path.splitext(os.path.split(filename)[1])[0]
    outFile=open('output/'+filename+'_output.txt','w')
    for vertex in lengthMatrix:
        for length in vertex:
            outFile.write(str(length)+',')
        outFile.write('\n')

def numVE(filename):
	f = open(filename, 'r')
	V, E = f.readline().split()
	f.close()
	return int(V), int(E)
	
def main(filename,algorithm):
    algorithm=algorithm[1:]
    G=readFile(filename)
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)
    
    V, E = numVE(filename) # Added
    
    pathLengths=[]
    if algorithm == 'b' or algorithm == 'B':
        pathLengths=BellmanFord(G, V, E)
    if algorithm == 'f' or algorithm == 'F':
        pathLengths=FloydWarshall(G, V)
    if algorithm == "both":
        start=time.clock()
        BellmanFord(G, V, E)
        end=time.clock()
        BFTime=end-start
        FloydWarshall(G, V)
        start=time.clock()
        end=time.clock()
        FWTime=end-start
        print("Bellman-Ford timing: "+str(BFTime))
        print("Floyd-Warshall timing: "+str(FWTime))
    writeFile(pathLengths,filename)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python bellman_ford.py -<f|b> <input_file>")
        quit(1)
    main(sys.argv[2],sys.argv[1])
