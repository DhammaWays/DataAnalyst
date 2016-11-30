# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:02:28 2016

@author: lsharma
"""

# Finding connection between islands

# Choosing 2 items out of n: nC2
def comb2(n):
    return (n*(n-1))//2
    
N = 10
L = [(0, 1), (2, 4), (3, 5), (8, 6), (8, 9), (1, 6), (9, 4)]
# Islands: [[0, 1, 2, 4, 6, 8, 9]), [3, 5]] + singleton([7])
# Answer: 23      

# Iteratvely expand islands out of intersecting sets until no more islands
# can be expanded     
Islands = [set(x) for x in L]      
merge = True
while( merge ):
    merge = False
    n = len(Islands)
    i = 0
    #print(Islands)
    while( i < n ):
        j = i + 1
        while( j < n ):
            if( not Islands[i].isdisjoint(Islands[j]) ):
                Islands[i] = Islands[i].union(Islands[j])
                del Islands[j]
                n -= 1
                merge = True
            j += 1
        i += 1                                
        
# Number of connections between islands = Total possible - connections for each island
#print(Islands)        
nConnections = comb2(N)
for x in Islands:
    nConnections -= comb2(len(x))

print(nConnections)        
            

        
