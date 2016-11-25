# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 16:41:05 2016

@author: lsharma
"""

'''
Count islands of 1 in 2D matrix
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False

class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

# You only need to change code with docs strings that have TODO.
# Specifically: Graph.dfs_helper and Graph.bfs
# New methods have been added to associate node numbers with names
# Specifically: Graph.set_node_names
# and the methods ending in "_names" which will print names instead
# of node numbers

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = []
        self._node_map = {}


    def insert_node(self, new_node_val):
        "Insert a new node with value new_node_val"
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
        nodes = {node_from_val: None, node_to_val: None}
        for node in self.nodes:
            if node.value in nodes:
                nodes[node.value] = node
                if all(nodes.values()):
                    break
        for node_val in nodes:
            nodes[node_val] = nodes[node_val] or self.insert_node(node_val)
        node_from = nodes[node_from_val]
        node_to = nodes[node_to_val]
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node, To Node)"""
        return [(e.value, e.node_from.value, e.node_to.value)
                for e in self.edges]

    def get_adjacency_list(self):
        """Return a list of lists.
        The indecies of the outer list represent "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_index = self.find_max_index()
        adjacency_list = [[] for _ in range(max_index)]
        for edg in self.edges:
            from_value, to_value = edg.node_from.value, edg.node_to.value
            adjacency_list[from_value].append((to_value, edg.value))
        return [a or None for a in adjacency_list] # replace []'s with None

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_index = self.find_max_index()
        adjacency_matrix = [[0] * (max_index+1) for _ in range(max_index)]
        for edg in self.edges:
            from_index, to_index = edg.node_from.value, edg.node_to.value
            adjacency_matrix[from_index][to_index] = edg.value
        return adjacency_matrix

    def find_max_index(self):
        """Return the highest found node number
        Or the length of the node names if set with set_node_names()."""
        if len(self.node_names) > 0:
            return len(self.node_names)
        max_index = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index

    def find_node(self, node_number):
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)
    
    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def dfs_helper(self, start_node):
        """TODO: Write the helper function for a recursive implementation
        of Depth First Search iterating through a node's edges. The
        output should be a list of numbers corresponding to the
        values of the traversed nodes.
        ARGUMENTS: start_node is the starting Node
        MODIFIES: the value of the visited property of nodes in self.nodes 
        RETURN: a list of the traversed node values (integers).
        """
        ret_list = []
        # Your code here
        if(not start_node.visited ):
            start_node.visited = True
            ret_list = [start_node.value]
            for edge in start_node.edges:
                if( edge.node_to.value != start_node.value ):
                  ret_list.extend(self.dfs_helper(edge.node_to))
                else:
                  ret_list.extend(self.dfs_helper(edge.node_from))
        
        return ret_list

    def dfs(self, start_node_num):
        """Outputs a list of numbers corresponding to the traversed nodes
        in a Depth First Search.
        ARGUMENTS: start_node_num is the starting node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        #self._clear_visited()
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)


# Has 5 islands
Mat2D = [ [1, 1, 0, 0, 0],
          [0, 1, 0, 0, 1],
          [1, 0, 1, 1, 1],
          [1, 0, 0, 0, 1],
          [1, 0, 1, 0, 1],
          [0, 0, 1, 0, 0] ]                          

graph = Graph()

N = len(Mat2D[0])
M = len(Mat2D)

# populate graph
for i in range(M):
    for j in range(N):
        if( Mat2D[i][j] == 1 ):
          graph.insert_node(i*N+j)
          if( j > 0 and Mat2D[i][j-1] == 1): # horizontal edge
            graph.insert_edge(Mat2D[i][j], i*N+j-1, i*N+j)
            
          if( i > 0 and Mat2D[i-1][j] == 1): # top edge
            graph.insert_edge(Mat2D[i][j], (i-1)*N+j, i*N+j)
            
          if( i > 0 and j > 0 and Mat2D[i-1][j-1] == 1 ): # left diganonal edge
            graph.insert_edge(Mat2D[i][j], (i-1)*N+j-1, i*N+j)
            
          if( i > 0 and j < N-1 and Mat2D[i-1][j+1] == 1 ): # right diagnonal edge
            graph.insert_edge(Mat2D[i][j], (i-1)*N+j+1, i*N+j)
            

# traverse graph to find connected nodes
cLst = []
graph._clear_visited()
for i in range(M):
  for j in range(N):
    if( Mat2D[i][j] == 1 ):
      tLst = graph.dfs( i*N + j )
      if( tLst ):
        cLst.append(tLst)
        
print("Number of islands:", len(cLst))
print( cLst )
      
import pprint
pp = pprint.PrettyPrinter(indent=2)
#pp.pprint(graph.get_edge_list())
#pp.pprint(graph.get_adjacency_matrix())
