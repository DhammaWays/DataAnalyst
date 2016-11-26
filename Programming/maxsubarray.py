# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26, 2016

@author: lsharma
"""

'''
Find largeest sum max_subarray
'''

# Using Kadane algorithm

def max_subarray(A):
    start = end = newstart = 0
    max_ending_here = max_so_far = A[0]
    for i in range(1, len(A)):
        x = A[i]
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        if( max_ending_here == x ):
          newstart = i
        if( max_so_far == max_ending_here ):
          end = i
          if( newstart > start ):
            start = newstart
            
    if( start > end ):
      start = end
      
    return max_so_far, A[start:end+1]

# Test 

#A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#SubArray: [4, -1, 2, 1] Sum: 6

#A = [-2, -3]
#SubArray: [-2] Sum: -2

#A = [5, -2, 3]

A = [10, -7, -4, 9, -2, -1, 5, -10, 7, 2]

maxsum, subA = max_subarray(A)
print( "SubArray:",subA, "Sum:", maxsum )
