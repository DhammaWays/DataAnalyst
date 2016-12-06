# -*- coding: utf-8 -*-
"""
Created on Tue Dec 06 14:23:44 2016

@author: lsharma
"""

# Snake and Ladders: Find minimum moves to reach final target

import dijkastra


# Our Snake and Ladder board is 10x10

# Load ladders (each tuple indicates start and end of a ladder)
N = 3
ladL = [(32, 62), (42, 68), (12, 98)]
Ladders = {}
for j in range(N):
    start, end = ladL[j]
    Ladders[start] = end

# Load snakes (each tuple indicates start and end of a snake)  
M = 7
snakeL = [(95, 13), (97, 25), (93, 37), (79, 27), (75, 19), (49, 47), (67, 17)]
Snakes = {}
for j in range(M):
    start, end = snakeL[j]
    Snakes[start] = end

# Populate graph
# Directed graph for 10x10 board (Node 1 to 100)
# Each Node is connected to next 6 nodes unless there is a ladder or snakes mouth
# In case of ladder or snake mouth we directly jump to their end from this node

# Very important to create graph with dijkastra module prefix otherwise it will
# not find noudle instance later on when methods are called internally

graph = dijkastra.Graph()

for j in range(1, 100):
    if( j in Ladders or j in Snakes ): # No nodes at start of ladders or snakes as we directly jump to their end
        continue
        
    for k in range(j+6, j, -1): # add next 6 nodes in reverse order so that direct BFS can work
        if( k > 100):
            continue
            
        to_node = k  
        if( k in Ladders ):
            to_node = Ladders[k]
        elif( k in Snakes ):
            to_node = Snakes[k]
        
        graph.insert_edge(1, j, to_node)
                
# Find shortest path from 1 to 100

pathMap, distMap = graph.dijkastra(1, 100)

# print path taken to final node and number of dice rolls
# Answer: [1, 6, 98, 100] and 3 dice rolls
# 1 -> dice roll of 5 -> 6 - > dice roll of 6 -> 12 -> ladder -> 98 -> dice roll of 2 -> 100

print(pathMap[100])
if( 100 not in pathMap ):
    print(-1)
else:
    print(distMap[100])