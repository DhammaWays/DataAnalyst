# Returns first unique character in given string (case-sensitive)

# This initial implementation returns first character that is not repeating
# without checking if same character may have been seen earlier or will be
# seen later

def uniqueFirstChar_0(S):
  i = 0
  while( i < len(S) ):
    # Get ready to scan next group
    count = 1
    
    # Keep skipping over next group of repeated characters
    while( i+1 < len(S) and S[i] == S[i+1] ):
      i += 1
      count += 1
      
    # We are done if found our first non-repeating character
    if( count == 1 ):
      break
  
    # Keep advancing
    i += 1
  
  # We have found our first unique character if we have not gone past string end
  if( i < len(S) and count == 1 ):
    return S[i]
  else:
    return None

# Returns first unique charcter (non-repeating) across whole string
# Here we make one pass to create counts and second to find first one with count of 1
def uniqueFirstChar_1(S):
  from collections import Counter, OrderedDict

  # We make our counter "ordered" by having it use "OrderedDict" instead of
  # normmal dict (OredredDict methods will take percendence over dict methods)
  # Therefore our oredred counter object will store keys in decreasing order
  # of their count followed by order they were inserted
  class OrderedCounter(Counter, OrderedDict):
    pass

  # Create ordered counter object and iterate to find first character with count of 1
  ordCnt = OrderedCounter(S)
  for k, v in ordCnt.items():
    if(v == 1):
      return k
  
  # All are repeating characters    
  return None
  
# Returns first unique character (non-repeating) across whole string
# We just make one pass and return the first element of our unique character set
def uniqueFirstChar(S):
  from collections import OrderedDict
  
  dupSet = set()
  uniqueSet = OrderedDict()
  
  ## Scan the given string in one pass, keeping track of duplicate
  # and unique characters set. Chose “ordered” set for unique
  # characters so that we can just return its first element.

  for c in S:
    if c not in dupSet:
      if c in uniqueSet:
        del uniqueSet[c]
        dupSet.add(c)
      else:
        uniqueSet[c] = None
  
  # Return first unique character or None if no unique character is found      
  return next(iter(uniqueSet), None) 
  
  
# Test
print(uniqueFirstChar("aabbcdd1223"))
print(uniqueFirstChar("aabb"))
print(uniqueFirstChar("aabbx"))
print(uniqueFirstChar("z"))
print(uniqueFirstChar("ABCDEFGH"))
print(uniqueFirstChar("aabbacd"))
print(uniqueFirstChar("abbaacd"))
print(uniqueFirstChar("abbacd"))


