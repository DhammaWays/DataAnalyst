# -*- coding: utf-8 -*-

"""
Technical Interview Questions
Udacity Data Analyst Nanodegree
Lekhraj Sharma
Dec 2016
"""

def question1_0(s, t):
    """
    Given two strings "s" and "t", checks whether some anagram of "t" is a substring of "s"
    ASSUMPTIONS: Matches are case specific. Empty "t" matches.
    ARGUMENTS: String "s" for which existense of an anagram of string "t" is checked
    MODIFIES: None
    RETURN: True if an anagram of "t" is present in "s", otherwise returns False
    """
    from itertools import permutations
    
    # Trivial cases: Empty strings or anagram string being larger length
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
        
def question1(s, t):
    """
    Given two strings "s" and "t", checks whether some anagram of "t" is a substring of "s"
    ASSUMPTIONS: Matches are case specific. Empty "t" matches.
    ARGUMENTS: String "s" for which existense of an anagram of string "t" is checked
    MODIFIES: None
    RETURN: True if an anagram of "t" is present in "s", otherwise returns False
    """
    
    # Trivial cases: Empty strings or anagram string being larger length
    lenT = len(t)
    lenS = len(s)
    if( lenT == 0 ):
        return True
    elif( lenT > lenS ):
        return False

    # Counter is handy for comparing count of characters in a string
    from collections import Counter   
    cntT = Counter(t)
    cntS = Counter(s[0:lenT])
    foundAnagram = False
    
    # Keep comparing sliding window of length of "t" by advancing it 1 char at a time
    for i in range(lenT, lenS):
        # We have found our anagram (at index of i-lenT) if curremt window has
        # same set of characters with same count (frequency) as our pattern "t". 
        if( cntT == cntS ):
            foundAnagram = True
            break
        
        # Keep advancing our window by 1 character
        # Add current character and remove first character from last window
        cntS += Counter(s[i])
        cntS -= Counter(s[i-lenT])
    
    # If we have not found an anagram already, need to check for last remaining window
    if( foundAnagram ):    
        return True
    else:
        return cntT == cntS 
    
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
    
    # Build regular expression to find palindrome of n*2 length
    # For example for string length of 6(even) or 7(odd) it Looks like:
    #  (.+)(.+)(.+).?\3\2\1
    def rePalExp(n):
        reExp = "(.+)"*n + ".?"
        for i in range(n, 0, -1):
            reExp += "\\" + str(i)
        return reExp
    
    # Keep checking for palindrome from largest possible to samllest possible
    # We exit as soon as we find the first palindrome 
    maxLen = len(a) // 2
    for i in range(maxLen, 0, -1):
        m = re.search(rePalExp(i), a)
        if( m ):
            return m.group(0)
            
    # No match found just return first character as palindrome of 1 char        
    return a[0]      

# Helper methods for question 2
# Find longest palindrome match in a string with given centers
def matchCenter(s, n, i1, i2):
    matchWhole = True
    for i, j in zip(range(i1, -1, -1), range(i2, n)):
        if( s[i] != s[j] ):
            matchWhole = False
            break
          
    if( matchWhole ):
      return (i, j)
    else:
      return (i+1, j-1)

# Return length of string given its start and end index tuple
def lenStr( curIdx ):
    return (curIdx[1]-curIdx[0]+1)
  
def question2(a):
    """
    Given a string "a", returns the longest palindromic substring contained in "a"
    ASSUMPTIONS: Single character string is also a palindrome
    ARGUMENTS: String "a" for which longest palindromic substring is to be extracted
    MODIFIES: None
    RETURN: Longest palindromic substring in string "a". In case of multiple longest
            palindromes, first one from start of string is returned.
    """
    
    # Trivial case
    size = len(a)
    if( size == 0 ):
        return ""
    
    # Iterate over whole string, keeping track of current maximum palindrome 
    maxStr = (0, 0)
    for i in range(0, size-1):
        # Find all odd matches which have same center in a palindrome
        curStr = matchCenter(a, size, i, i)
        if( lenStr(curStr) > lenStr(maxStr) ):
            maxStr = curStr
      
        # Find all even matches which have two centers in a palindrome
        curStr = matchCenter(a, size, i, i+1)
        if( lenStr(curStr) > lenStr(maxStr) ):
            maxStr = curStr
      
    return a[maxStr[0]:maxStr[1]+1]

# Helper method to find minimum spanning tree using prim's method   
def primMST(G, s):
    """
    Minimum Spanning Tree (Prim's: Select the edges with minimum weight)
    Returns predecessor node of minimum spanning tree path to a node and dist from prdecessor dictionary
    """
    from heapq import heappush, heappop
    from collections import defaultdict

    # Trivial case: when start node is not connected, singleton!
    if( s not in G or len(G[s]) == 0 ): 
        return {s: None}, {s: 0}
    
    # populate minimum heap (queue)
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
    connects all vertices in a graph with the smallest possible total weight of edges   
    ASSUMPTIONS: Graph "G" is fully connected. In case of disconnected portions, make multiple
                 calls with each connected piece.
    ARGUMENTS: Graph "G" with adjacency dictionary where Vertices are represented as unique strings,
    for example {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
    MODIFIES: None
    RETURN: Minimum Spanning Tree adjacency dictionary
    """
    # Trivial case: Empty Graph
    if( len(G) == 0 ):
        return {}
    
    # Use prim's method to generate minimum spanning tree
    predMap, distMap = primMST(G, list(G.keys())[0])
    
    # Create MST graph adjacency list
    mstG = {}
    for t, s in predMap.items():
        if( s ):
            mstG[s] = mstG.get(s, []) + [(t, distMap[t])]
            mstG[t] = mstG.get(t, []) + [(s, distMap[t])]
        else:
            mstG[t] = mstG.get(t, [])
    
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
          
def question4_0(T, r, n1, n2):
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
    # Order the n1, n2 in increaseing order
    if( n1 <= n2 ):
        lower, upper = n1, n2
    else:
        lower, upper = n2, n1
    
    # Trivial case
    if( r == lower or r == upper ):
      return r
    elif( lower < r < upper ):
      return r
      
    # Build the BST 
    root = buildBST(T, r)
    
    # Traverse BST from root to find the parent node whose value is between
    # given n1 and n2
    while(root is not None):
      if( (lower < root.data < upper) or (root.data == lower) or (root.data == upper)):
        return root.data
      
      # Keep searching to left or right of the tree based on which side our
      # value lies  
      if( upper < root.data ):
        root = root.left
      else:
        root = root.right
    
    # Did not find common ancestor    
    return None 

# Helper methods to find left and right child in Tree matrix
def leftChild(T, r):
    left = None
    for i in range(r):
        if( T[r][i] == 1 ):
            left = i
            break
    return left

def rightChild(T, r):
    right = None
    for i in range(r+1, len(T[r])):
        if( T[r][i] == 1 ):
            right = i
            break
    return right
    
    
def question4(T, r, n1, n2):
    """
    Find the least common ancestor between two nodes on a binary search tree.
    The least common ancestor is the farthest node from the root that is an
    ancestor of both nodes.
    ASSUMPTIONS: Tree is true binary serach tree. Right root is given. Both n1 and n2 exist in given tree.
    ARGUMENTS: T is the tree represented as a matrix, where the index of the
    list is equal to the integer stored in that node and a 1 represents a
    child node, r is a non-negative integer representing the root, and n1 and n2
    are non-negative integers representing the two nodes in no particular order.
    MODIFIES: None
    RETURN: Least common ancestor node. In case of n1 or n2 being parent of each other, the parent is returned.
    """
    # Bad input checks
    if( not T or r > len(T)-1 or len(T) != len(T[r]) ):
        return None
    
    # Order the n1, n2 in increaseing order
    if( n1 <= n2 ):
        lower, upper = n1, n2
    else:
        lower, upper = n2, n1
    
    # Traverse BST from root to find the parent node whose value is between
    # given n1 and n2
    root = r
    while(root is not None):
      if( (lower < root < upper) or (root == lower) or (root == upper)):
        return root
      
      # Keep searching to left or right of the tree based on which side our
      # value lies  
      if( upper < root ):
        root = leftChild(T, root)
      else:
        root = rightChild(T, root)
    
    # Did not find common ancestor    
    return None 

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m):
    """
    Find the element in a singly linked list that's m elements from the end.
    ASSUMPTIONS: question5(ll, 0) is the last node and question5(ll, length(ll)-1) is the first node.
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
    
    # We do not know the length (L) of singly linked list to directly jump
    # to "L-m" element like in indexable iterator. 
    
    # Instead of making two passes (first to find the length and second to
    # advance to "L-m" element, traverse the list with two pointers in a single
    # pass, where one tracks the end of list and another stays behind from it
    # with "m" elements gap
    nxtNode = ll
    prevNode = ll
    count = 0
    
    # Keeping advancing two pointers (nxt, prev) with the gap of given
    # "m" elements until we reach end of list
    while( nxtNode is not None ):
      # Advance prev pointer only after we have created a gap of "m" elements
      if( count > m ):
        # After "m" elemnts we advance "prev" in lockstep with "nxt"
        prevNode = prevNode.next
      
      count += 1  
      nxtNode = nxtNode.next
    
    # Either the list is shorter than "m" elements or "prev" points to our
    # "m" elements from end    
    if( count <= m ):
      return None
    else:
      return prevNode


# Test Code

# Only execute test code if called from main (i.e. not when it is imported as module)        
#if __name__ == "__main__":
if True:

    print("Test cases for question1: checking for any anagram in a string")
    print(question1("Udacity", "ad"))
    # True
    print(question1("Udacity", "ty"))
    # True
    print(question1("Udacity", "uy"))
    # False
    print(question1("Udacity Nanodegree is fun for learners", "edon"))
    # True
    print(question1("", "Hello"))
    # False
    print(question1("Hello", ""))
    # True
    print(question1("", ""))
    # True
 
    print("\nTest cases for question2: finding longest palindrome in a string")   
    print(question2("xabbay"))
    # abba
    print(question2("xabcbay"))
    # abcba
    print(question2("xabbaabbay"))
    # abbaabba
    print(question2("xabbaabbcy"))
    # bbaabb
    print(question2("abbaabba"))
    # abbaabba
    print(question2("pqrstuvwxyzabbaxabbapqrstuvwxyz"))
    # abbaxabba
    print(question2("xyabbahelloZZollehzzz"))
    # helloZZolleh
    print(question2("abcdefg"))
    # a
    print(question2("a"))
    # a
    
    print("\nTest cases for question3: finding minimum spanning tree of a graph")
    G = {'A': [('B', 2)], 'B': [('A', 2), ('C', 5)], 'C': [('B', 5)]}
    print(question3(G))
    # {'C': [('B', 5)], 'B': [('C', 5), ('A', 2)], 'A': [('B', 2)]}
    G = {'A': [('B', 2), ('C', 3)], 'B': [('A', 2), ('C', 2)], 'C': [('B', 2), ('A', 3)]}
    print(question3(G))
    # {'C': [('B', 2)], 'B': [('C', 2), ('A', 2)], 'A': [('B', 2)]}
    G = {'A': [('B', 2), ('C', 3), ('D', 2)], 'B': [('A', 2), ('D', 1)], 'C': [('A', 3), ('D', 2)],
         'D': [('C', 2), ('B', 1), ('E', 1)], 'E': [('D', 1)]}
    print(question3(G))
    # {'E': [('D', 1)], 'C': [('D', 2)], 'D': [('E', 1), ('B', 1), ('C', 2)], 'B': [('A', 2), ('D', 1)], 'A': [('B', 2)]}
    G = {'A': [('B', 10)], 'B': [('A', 10), ('C', 5), ('D', 3), ('E', 5)],
         'C': [('B', 5), ('E', 3)], 'D': [('B', 3), ('E', 3)],
         'E': [('F', 5), ('C', 3), ('D', 3)], 'F': [('E', 5)]}
    print(question3(G))
    # {'D': [('E', 3), ('B', 3)], 'E': [('D', 3), ('F', 5), ('C', 3)], 'F': [('E', 5)], 'C': [('E', 3)], 'B': [('D', 3), ('A', 10)], 'A': [('B', 10)]}
    print(question3({}))
    # {}
    print(question3({'A':[]}))
    # {'A':[]}
    
    print("\nTest cases for question4: finding least common ancestor in a binary search tree")   
    # Tree: 3->(0->1, 4)
    T = [[0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [0, 0, 0, 0, 0]]
    print(question4(T, 3, 1, 4))
    # 3
    print(question4(T, 5, 1, 4))
    # None
    print(question4([], 0, 1, 4))
    # None
    print(question4(T, 4, 0, 1))
    # None
    # Tree: 3->(1->(0,2), 4)
    T = [[0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]
    print(question4(T, 3, 0, 4))
    # 3
    print(question4(T, 3, 0, 2))
    # 1
    print(question4(T, 3, 1, 2))
    # 1
    print(question4(T, 3, 4, 3))
    # 3
    # Tree: 4->(1->(0, 2)), (6->(5, 8->7))
    T = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 0, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 0]]
    print(question4(T, 4, 0, 5))
    # 4
    print(question4(T, 4, 0, 2))
    # 1
    print(question4(T, 4, 2, 3))
    # 2
    print(question4(T, 4, 5, 7))
    # 6
    print(question4(T, 4, 5, 8))
    # 6
    print(question4(T, 4, 6, 7))
    # 6
        
    print("\nTest cases for question5: finding m th element from end in singly linked list")
    ll = Node(1)
    node = ll
    for i in range(2, 12):
      node.next = Node(i)
      node = node.next
    
    print(question5(ll, 1).data)
    # 10
    print(question5(ll, 5).data)
    # 6
    print(question5(ll, 10).data)
    # 1
    print(question5(ll, 0).data)
    # 11
    print(question5(ll, 11))
    # None
    print(question5(None, 2))
    # None
    print(question5(ll, -2))
    # None
   
