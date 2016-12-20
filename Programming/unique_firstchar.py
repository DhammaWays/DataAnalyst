# Returns first unique character in given string (case-sensitive)
def uniqueFirstChar(S):
  i = 0;
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
    
# Test
print(uniqueFirstChar("aabbcdd1223"))
print(uniqueFirstChar("aabb"))
print(uniqueFirstChar("aabbx"))
print(uniqueFirstChar("z"))
print(uniqueFirstChar("ABCDEFGH"))