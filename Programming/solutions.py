# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:52:38 2016

@author: lsharma
"""

"""
Technical Interview Questions
Udacity Data Analyst Nanodegree
Lekhraj Sharma
Dec 2016
"""

def question1(s, t):
    """
    Given two strings "s" and "t", checks whether some anagram of "t" is a substring of "s"
    ASSUMPTION: Matches are case specific. Empty "t" matches.
    ARGUMENTS: String "s" for which existense of an anagram of String "t" is checked
    MODIFIES: None
    RETURN: True if an anagram of "t" is present in "s", otherwise returns False
    """
    from itertools import permutations
    
    # Basic cases: Empty strings or anagram string being larger length
    if( len(t) == 0 ):
        return True
    elif( len(t) > len(s) ):
        return False
    
    foundAnagram = False
    for anaChars in permutations(t, len(t)):
        anaStr = ''.join(anaChars)
        if anaStr in s:
            foundAnagram = True
            break
        
    return foundAnagram
        
    
def question2_0(a):
    """
    Given a string "a", returns the longest palindromic substring contained in "a"
    ARGUMENTS: String "a" for which longest palindromic substring is to be extracted
    MODIFIES: None
    RETURN: Longest palindromic substring in string "a"
    """
    # trivial case
    if( len(a) <= 1 ):
        return(a)
        
    import re
        
    def rePalExp(n):
        reExp = "(.+)"*n + ".?"
        for i in range(n, 0, -1):
            reExp += "\\" + str(i)
        return reExp
    
    maxLen = len(a) // 2
    for i in range(maxLen, 0, -1):
        #print(rePalExp(i))
        m = re.search(rePalExp(i), a)
        if( m ):
            return m.group(0)
            
    # no match found just return first character as palindrome of 1 char        
    return a[0]      


# check how much of reverse of second string match with first string from its end
def matchReverse(a, i1, j1, i2, j2):
    match = True
    for i, j in zip(range(j1, i1-1, -1), range(i2, j2+1)):
        if( a[i] != a[j] ):
            match = False
            break

    return (match, i+1, j-1)  

# merge two palindrome strings
def merge_pal(a, i1, j1, i2, j2):
    len1 = j1-i1 + 1
    len2 = j2-i2 + 1
    if( a[j1] != a[i2] ): # can not be directly merged
        if( len1 >= len2): # first is bigger
            return (i1, j1)
        else:
            return (i2, j2)
    else:
        # Findout how much reverse of second string match with first string from end
        match, _, _ = matchReverse(a, i1, j1, i2, j2)
        if( not match ):
          if( len1 >= len2 ):
            return (i1, j1) # just return first string
          else:
            return (i2, j2)
        else: # reverse of whole string matched, so it can be completely combined
            return (i1, j2)

def question2_helper(a, i, j):
    # trivial case
    size = j-i + 1
    if( size <= 1 ):
      return (True, i, i)
    elif( size == 2 ):
      return (a[i] == a[j], i, j)
    elif( size == 3 ):
      if( a[i] == a[j] ):
        return (True, i, j)
      elif( a[i] == a[i+1] ):
        return (True, i, i+1)
      elif( a[i+1] == a[j] ):
        return (True, i+1, j)
      else:
        return (False, i, j)
 
    # Recursively subdivide
    if( size & 1 ): # odd length string
        i1, j1, i2, j2 = i, i+(size//2), i+(size//2), j
    else:
        i1, j1, i2, j2 = i, i+(size//2) - 1, i+(size//2), j
        
    match, _, _ = matchReverse(a, i1, j1, i2, j2)
    if( match ):
        return (True, i, j)
    else:
        isPal1, i1, j1 = question2_helper(a, i1, j1)
        isPal2, i2, j2 = question2_helper(a, i2, j2)
    
    len1 = j1-i1 + 1
    len2 = j2-i2 + 1
    if( isPal1 and isPal2 ):
        return (True, *merge_pal(a, i1, j1, i2, j2))
    elif( isPal1 ):
        match, i3, j3 = matchReverse(a, i1, j1, i2, j2)
        #print(match, i3, j3, i1, j1, i2, j2, len1, len2)
        if( not match ): # expected
          if( j3-i3+1 > len1 ):
            return (True, i3, j3)
          else:
            return (True, i1, j1)
        else:
          return (True, i1, j2)
    elif( isPal2 ):
        match, i3, j3 = matchReverse(a, i1, j1, i2, j2)
        if( not match ): # expected
          if( j3-i3+1 > len2 ):
            return (True, i3, j3)
          else:
            return (True, i2, j2)
        else:
          return (True, i1, j2)
    else:
        match, i3, j3 = matchReverse(a, i1, j1, i2, j2)
        if( match ):
          return (True, i1, j2)
        else:
          len3 = j3-i3+1
          if( len3 >= len1 ):
            return (True, i3, j3)
          else: # find pal string within remaining two first and second halfs
            isPal4, i4, j4 = question2_helper(a, i1, i3-1)
            isPal5, i5, j5 = question2_helper(a, j3+1, j2)
            if( isPal4 and isPal5 ):
              len4 = j4-i4+1
              len5 = j5-i5+1
              # return maximum of three
              if( len3 >= len4 ):
                if( len3 >= len5 ):
                  return (True, i3, j3)
                else:
                  return (True, i5, j5)
              elif( len4 >= len5 ):
                  return (True, i4, j4)
              else:
                  return (True, i5, j5)
            elif( isPal4 ):
              if( len3 >= j4-i4+1 ):
                return (True, i3, j3)
              else:
                return (True, i4, j4)
            elif( isPal5 ):
              if( len3 >= j5-i5+1 ):
                return (True, i3, j3)
              else:
                return (True, i5, j5)
            else: # return middle pal
                return (True, i3, j3)
              
    # Fallback, no real palindrome found!
    return (False, i, j)

def question2(a):
    """
    Given a string "a", returns the longest palindromic substring contained in "a"
    ARGUMENTS: String "a" for which longest palindromic substring is to be extracted
    MODIFIES: None
    RETURN: Longest palindromic substring in string "a"
    """

    isPal, i, j = question2_helper(a, 0, len(a)-1)
    if( isPal ):
      return a[i:j+1]
    else:
      return "OOPS! Something went Wrong!"
       
    
def primMST(G, s):
    '''
    Minimum Spanning Tree (Prim's: Select the edges with minimum weight)
    Returns predecessor node of minimum spanning tree path to a node and dist from prdecessor dictionary
    '''
    from heapq import heappush, heappop
    from collections import defaultdict

    # Trivial case: when start node is not connected, singleton!
    if( s not in G or len(G[s]) == 0 ): 
        return {s: None}, {s: 0}
    
    # populate MinQ
    Q = [(0, s)] # dist, node
    visited = set()
    inf = float('inf')

    distMap = defaultdict(lambda: inf)    
    distMap[s] = 0
    predMap = {s : None}

    # Iterate over picking minimum value node until queue is empty
    while( Q ):
        d, u = heappop(Q)
        if( u not in visited ):
            for edge in G[u]:
                v = edge[0]
                if( v not in visited ):
                    newDist = edge[1]
                    if( newDist < distMap[v] ):
                        heappush(Q, (newDist, v))
                        distMap[v] = newDist
                        predMap[v] = u
                        
            visited.add(u)

    return predMap, distMap    

def question3(G):
    """
    Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree
    connects all vertices in a graph with the smallest possible total weight of edges.
    ARGUMENTS: Graph "G" with adjacency dictionary where Vertices are represented as unique strings,
    for example {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
    MODIFIES: None
    RETURN: Minimum Spanning Tree adjacency dictionary
    """
    # Trivial case: Empty Graph
    if( len(G) == 0 ):
        return {}
    
    # Use prim's method to generate minimum spanning tree
    predMap, distMap = primMST(G, G.keys()[0])
    
    # Create MST graph adjacency list
    mstG = {}
    for t, s in predMap.items():
        if( s ):
            mstG[s] = mstG.get(s, []) + [(t, distMap[t])]
            mstG[t] = mstG.get(t, []) + [(s, distMap[t])]            
    
    return mstG

# Binary Tree node 
class tNode(object):
  def __init__(self, data):
    self.data = data 
    self.left = None
    self.right = None

# Build a binary search Tree
def buildBST(T, r):
  node = tNode(r)
  for i in range(len(T[r])):
    if( T[r][i] == 1 ):
      if( i < r ):
        node.left = buildBST(T, i)
      else:
        node.right = buildBST(T, i)
        break
        
  return node
        
  
def question4(T, r, n1, n2):
    """
    Find the least common ancestor between two nodes on a binary search tree.
    The least common ancestor is the farthest node from the root that is an
    ancestor of both nodes.
    ARGUMENTS: T is the tree represented as a matrix, where the index of the
    list is equal to the integer stored in that node and a 1 represents a
    child node, r is a non-negative integer representing the root, and n1 and n2
    are non-negative integers representing the two nodes in no particular order.
    MODIFIES: None
    RETURN: Least common ancestor node
    """
    # Trivial case
    if( r == n1 or r == n2 ):
      return None
    elif( n1 < r < n2 ):
      return r
      
    # Build the BST 
    root = buildBST(T, r)
    
    # Find the root node whose value is between given n1 and n2
    while(root is not None):
      if( (n1 < root.data < n2) or (n2 < root.data < n1) ):
        return root.data
      
      # Keep seraching to left or right of tree based on which side our value lies  
      if( n1 < root.data ):
        root = root.left
      else:
        root = root.right
        
    return None 

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m):
    """
    Find the element in a singly linked list that's m elements from the end.
    ARGUMENTS: ll is the first node of a linked list and m is the "mth number from the end".
    Node structure passed and returned is: 
        class Node(object):
          def __init__(self, data):
            self.data = data
            self.next = None
    MODIFIES: None
    RETURN: "m" element (Node) from end
    """
    # Trivial case
    if( not ll or m < 0 ):
      return None
      
    nxtNode = ll
    prevNode = ll
    count = 0
    while( nxtNode is not None ):
      if( count > m ):
        prevNode = prevNode.next
      
      count += 1  
      nxtNode = nxtNode.next
        
    if( count <= m ):
      return None
    else:
      return prevNode



# Test Code

# Only execute test code if called from main (i.e. not when it is imported as module)        
if __name__ == "__main__":

    print(question1("Udacity", "ad"))
    print(question1("Udacity", "ty"))
    print(question1("Udacity", "uy"))
    print(question1("", "Hello"))
    print(question1("Hello", ""))
    print(question1("", ""))
    
    print(question2("xabbay"))
    print(question2("xabcbay"))
    print(question2("xabbaabbay"))
    print(question2("xabbaabbcy"))
    print(question2("abbaabba"))
    print(question2("abbaxabbaxyz"))
    print(question2("xyabbahelloZZollehzzz"))
    print(question2("abcdefg"))
    print(question2("a"))
    
    G = {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
    print(question3(G))
    G = {'A': [('B', 2), ('C', 3)], 'B': [('A', 2), ('C', 2)], 'C': [('B', 2), ('A', 3)]}
    print(question3(G))    
    G = {'A': [('B', 2), ('C', 3), ('D', 2)], 'B': [('A', 2), ('D', 1)], 'C': [('A', 3), ('D', 2)],
         'D': [('C', 2), ('B', 1), ('E', 1)], 'E': [('D', 1)]}
    print(question3(G))
      
    ll = Node(1)
    node = ll
    for i in range(2, 12):
      node.next = Node(i)
      node = node.next
    
    print(question5(ll, 1).data)
    print(question5(ll, 5).data)
    print(question5(ll, 10).data)
    print(question5(ll, 0).data)
    print(question5(ll, 11))
    print(question5(None, 2))
    print(question5(ll, -2))
        
    T = [[0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0]]
    print(question4(T, 3, 1, 4))
    T = [[0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]
    print(question4(T, 3, 0, 4))
    print(question4(T, 3, 0, 2))
    print(question4(T, 3, 1, 2))
    

    




