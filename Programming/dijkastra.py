# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 13:56:55 2016

@author: lsharma
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False
        
    def __lt__(self, other):
        return self.value < other.value


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        "Insert a new node with value new_node_val"
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node
        
    def find_insert_node(self, node_val):
        "Insert a new node with value node_val if it already does not exist"
        if( node_val not in self._node_map):
            return self.insert_node(node_val)
        else:
            return self._node_map[node_val]        

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
        node_from = self.find_insert_node(node_from_val)
        node_to = self.find_insert_node(node_to_val)
        new_edge = Edge(new_edge_val, node_from, node_to)
        node_from.edges.append(new_edge)
        node_to.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node, To Node)"""
        return [(e.value, e.node_from.value, e.node_to.value)
                for e in self.edges]

    def get_edge_list_names(self):
        """Return a list of triples that looks like this:
        (Edge Value, From Node Name, To Node Name)"""
        return [(edge.value,
                 self.node_names[edge.node_from.value],
                 self.node_names[edge.node_to.value])
                for edge in self.edges]

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

    def get_adjacency_list_names(self):
        """Each section in the list will store a list
        of tuples that looks like this:
        (To Node Name, Edge Value).
        Node names should come from the names set
        with set_node_names."""
        adjacency_list = self.get_adjacency_list()
        def convert_to_names(pair, graph=self):
            node_number, value = pair
            return (graph.node_names[node_number], value)
        def map_conversion(adjacency_list_for_node):
            if adjacency_list_for_node is None:
                return None
            return map(convert_to_names, adjacency_list_for_node)
        return [map_conversion(adjacency_list_for_node)
                for adjacency_list_for_node in adjacency_list]

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_index = self.find_max_index()
        adjacency_matrix = [[0] * (max_index) for _ in range(max_index)]
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
                ret_list.extend(self.dfs_helper(edge.node_to))
        
        return ret_list

    def dfs(self, start_node_num):
        """Outputs a list of numbers corresponding to the traversed nodes
        in a Depth First Search.
        ARGUMENTS: start_node_num is the starting node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        self._clear_visited()
        start_node = self.find_node(start_node_num)
        return self.dfs_helper(start_node)

    def dfs_names(self, start_node_num):
        """Return the results of dfs with numbers converted to names."""
        return [self.node_names[num] for num in self.dfs(start_node_num)]

    def bfs(self, start_node_num):
        """TODO: Create an iterative implementation of Breadth First Search
        iterating through a node's edges. The output should be a list of
        numbers corresponding to the traversed nodes.
        ARGUMENTS: start_node_num is the node number (integer)
        MODIFIES: the value of the visited property of nodes in self.nodes
        RETURN: a list of the node values (integers)."""
        node = self.find_node(start_node_num)
        self._clear_visited()
        ret_list = [node.value]
        node.visited = True
        # Your code here
        from collections import deque
        vqueue = deque([node])
        while( len(vqueue) > 0 ):
            node = vqueue.popleft()
            for edge in node.edges:
                if( not edge.node_to.visited ):
                    ret_list.append( edge.node_to.value )
                    edge.node_to.visited = True
                    vqueue.append( edge.node_to )
                
        return ret_list

    def bfs_names(self, start_node_num):
        """Return the results of bfs with numbers converted to names."""
        return [self.node_names[num] for num in self.bfs(start_node_num)]
        
    # Dijkastra Algorithm - To dind shortest path from "source" to "target" node
    #
    
    def dijkastra_1(self, s, t):
      '''
      Returns prdecessor-path and distance dictionary
      '''
      from heapq import heappush, heappop, heapify
      from collections import defaultdict
      
      # Only proceed if the start_node is connected (i.e. not a singelton)!
      if( s not in self._node_map):
          return {s: [None]}, {s: 0}
      
      # populate MinQ
      Q = []
      visited = set()
      inf = float('inf')
      for node in self.nodes:
         if( node.value != s ):
             heappush(Q, (inf, node))
         else:
             heappush(Q, (0, node))
             
      distMap, pathMap = defaultdict(lambda: inf), {s: None}
      distMap[s] = 0
      
      # iterate over picking minimum value node until queue is empty
      while( Q ):
          d, node = heappop(Q)
          u = node.value
          visited.add(u)
          #print("U =>", u)
          if( u == t ): # found path to target
            return pathMap, distMap
            
          for edge in node.edges:
              v = edge.node_to.value
              if( v not in visited ):
                  #print("v:", v)
                  newDist = edge.value + distMap[u]
                  if( newDist < distMap[v] ):
                      Q[Q.index((distMap[v], edge.node_to))] =  (newDist, edge.node_to)
                      heapify(Q)
                      distMap[v] = newDist
                      pathMap[v] = u
                      
      return pathMap, distMap
                      
    def predecessor_to_path(self, p, s, t):
        '''
        Returns full path from "s" to "t" using given predcessor map 
        '''
        path = []
        prev = t
        while prev != s:
          path.insert(0, prev)
          prev = p[prev]
          
        path.insert(0, s)
        return path
                      
    def dijkastra( self, s, t):
      '''
      Returns path and distance dictionary
      Here we do not have to update existing entries in min heap, so no need to
      heapify. This should run faster plus we build path as well iteratively
      instead of just keeping prdecssors around.
      '''
      from heapq import heappush, heappop, heapify
      from collections import defaultdict
      
      # Only proceed if the start_node is connected (i.e. not a singelton)!
      if( s not in self._node_map):
          return {s: [s]}, {s: 0}
      
      # populate MinQ
      visited = set()
      inf = float('inf')
      Q = [(inf, self.find_node(s), [s])] # dist, node, path
      visited = set()
      inf = float('inf')
             
      distMap, pathMap = defaultdict(lambda: inf), {s: [s]}    
      distMap[s] = 0
      
      # iterate over picking minimum value node until queue is empty
      while( Q ):
          d, node, path = heappop(Q)
          u = node.value
          #print("U=>", u, path)
          #if( u != path[-1] ):
          if( u not in visited ):
              #path.append(u)
              if( u == t ): # found path to target
                return pathMap, distMap
                
              for edge in node.edges:
                  v = edge.node_to.value
                  node = edge.node_to
                  if( v == u ): # to handle undirected edges
                      v = edge.node_from.value
                      node = edge.node_from
                  if( v not in visited ):
                      newDist = edge.value + distMap[u]
                      if( newDist < distMap[v] ):
                          npath = path + [v]
                          #print("v:", v, npath)
                          heappush(Q, (newDist, node, npath))
                          distMap[v] = newDist
                          pathMap[v] = npath                 
              visited.add(u)
                                        
      return pathMap, distMap
  
    def kruskalMST(self, s):
        '''
        Minimum Spanning Tree (Kruskal: In case of equal edge weight choose with minimum sum of two node numbers connecting this edge)
        Returns predecessor node of minimum spanning tree path to a node and dist from prdecessor dictionary
        '''
        from heapq import heappush, heappop, heapify
        from collections import defaultdict

        if( s not in self._node_map ): # when start node is not connected, singleton!
            return {s: [None]}, {s: 0}
        
        # populate MinQ
        Q = [(0, s, None)] # span, node_num, connecting edge node_num
        visited = set()
        inf = float('inf')

        distMap = defaultdict(lambda: inf)    
        distMap[s] = 0
        pathMap = {s : None}

        # iterate over picking minimum value node until queue is empty
        while( Q ):
            d, u, up = heappop(Q)
            #print("U=>", u, d)
            if( u not in visited ):
                for edge in self.find_node(u).edges:
                    v = edge.node_to.value
                    if( u == v ): # non-directed
                        v = edge.node_from.value

                    if( v not in visited ):
                        newDist = edge.value
                        if( newDist <= distMap[v] ):
                            #print("v:", v, newDist)
                            heappush(Q, (newDist, v, u))
                            distMap[v] = newDist
                            pathMap[v] = u
                            
                visited.add(u)

        return pathMap, distMap


    def primMST(self, s):
        '''
        Minimum Spanning Tree (Prim's: Selec the edges with minimum weight)
        Returns predecessor node of minimum spanning tree path to a node and dist from prdecessor dictionary
        '''
        from heapq import heappush, heappop, heapify
        from collections import defaultdict

        if( s not in self._node_map ): # when start node is not connected, singleton!
            return {s: 0}
        
        # populate MinQ
        Q = [(0, s)] # span, node_num
        visited = set()
        inf = float('inf')

        distMap = defaultdict(lambda: inf)    
        distMap[s] = 0
        pathMap = {s : None}

        # iterate over picking minimum value node until queue is empty
        while( Q ):
            d, u = heappop(Q)
            #print("U=>", u, d)
            if( u not in visited ):
                for edge in self.find_node(u).edges:
                    v = edge.node_to.value
                    if( u == v ): # non-directed
                        v = edge.node_from.value

                    if( v not in visited ):
                        newDist = edge.value
                        if( newDist < distMap[v] ):
                            #print("v:", v, newDist)
                            heappush(Q, (newDist, v))
                            distMap[v] = newDist
                            pathMap[v] = u
                            
                visited.add(u)

        return pathMap, distMap

# Test Code

# Only execute test code if called from main (i.e. not when it is imported as module)        
if __name__ == "__main__":
    
    graph = Graph()
    
    # You do not need to change anything below this line.
    # You only need to implement Graph.dfs_helper and Graph.bfs
    
    graph.set_node_names(('Mountain View',   # 0
                          'San Francisco',   # 1
                          'London',          # 2
                          'Shanghai',        # 3
                          'Berlin',          # 4
                          'Sao Paolo',       # 5
                          'Bangalore'))      # 6 
    
    graph.insert_edge(51, 0, 1)     # MV <-> SF
    graph.insert_edge(51, 1, 0)     # SF <-> MV
    graph.insert_edge(9950, 0, 3)   # MV <-> Shanghai
    graph.insert_edge(9950, 3, 0)   # Shanghai <-> MV
    graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
    graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
    graph.insert_edge(9900, 1, 3)   # SF <-> Shanghai
    graph.insert_edge(9900, 3, 1)   # Shanghai <-> SF
    graph.insert_edge(9130, 1, 4)   # SF <-> Berlin
    graph.insert_edge(9130, 4, 1)   # Berlin <-> SF
    graph.insert_edge(9217, 2, 3)   # London <-> Shanghai
    graph.insert_edge(9217, 3, 2)   # Shanghai <-> London
    graph.insert_edge(932, 2, 4)    # London <-> Berlin
    graph.insert_edge(932, 4, 2)    # Berlin <-> London
    graph.insert_edge(9471, 2, 5)   # London <-> Sao Paolo
    graph.insert_edge(9471, 5, 2)   # Sao Paolo <-> London
    # (6) 'Bangalore' is intentionally disconnected (no edges)
    # for this problem and should produce None in the
    # Adjacency List, etc.
    
    '''
    import pprint
    pp = pprint.PrettyPrinter(indent=2)
    
    print "Edge List"
    pp.pprint(graph.get_edge_list_names())
    
    print "\nAdjacency List"
    pp.pprint(graph.get_adjacency_list_names())
    
    print "\nAdjacency Matrix"
    pp.pprint(graph.get_adjacency_matrix())
    
    print "\nDepth First Search"
    pp.pprint(graph.dfs_names(2))
    
    # Should print:
    # Depth First Search
    # ['London', 'Shanghai', 'Mountain View', 'San Francisco', 'Berlin', 'Sao Paolo']
    
    print "\nBreadth First Search"
    pp.pprint(graph.bfs_names(2))
    # test error reporting
    # pp.pprint(['Sao Paolo', 'Mountain View', 'San Francisco', 'London', 'Shanghai', 'Berlin'])
    
    # Should print:
    # Breadth First Search
    # ['London', 'Shanghai', 'Berlin', 'Sao Paolo', 'Mountain View', 'San Francisco']
    '''
    
    
    # Test
                       
    s, t =  0, 2
    p, d = graph.dijkastra_1(s, t)
    path = graph.predecessor_to_path(p, s, t)
    print("Shortest distance from", graph.node_names[s], "to", graph.node_names[t], "is", d[t])
    print("Path:", ' - '.join([graph.node_names[i] for i in path]))
           
    s, t =  0, 2
    p, d = graph.dijkastra(s, t)
    path = p[t]
    print("Shortest distance from", graph.node_names[s], "to", graph.node_names[t], "is", d[t])
    print("Path:", ' - '.join([graph.node_names[i] for i in path]))
     
    p, d = graph.kruskalMST(s)
    path = graph.predecessor_to_path(p, s, t)
    print("Kruskal MST Path:", ' - '.join([graph.node_names[i] for i in path]))
    
    p, d = graph.primMST(s)
    path = graph.predecessor_to_path(p, s, t)
    print("Prim MST Path:", ' - '.join([graph.node_names[i] for i in path]))
    
    
    # Answer:
    # Shortest distance from Mountain View to London is 10113
    # Path: Mountain View - San Francisco - Berlin - London
       