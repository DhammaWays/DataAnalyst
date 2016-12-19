# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:40:01 2016

@author: lsharma
"""

def maxDiff_0(A):
    if( A[1] > A[0] ):
        cur_max, max_sofar = A[1], A[1]
        cur_min, min_sofar = A[0], A[0]
    else:
        cur_max, max_sofar, cur_min, min_sofar = A[1], A[1], A[1], A[1]
        
    negdiff = A[1] - A[0]
    iMax = 1    
    for i in range(2, len(A)):
        if( A[i] < cur_max):  
            if( cur_max - min_sofar > max_sofar - min_sofar ):
                max_sofar = cur_max           
            if( cur_max - cur_min > max_sofar - min_sofar):
                max_sofar = cur_max
                min_sofar = cur_min

            cur_max = A[i]
            if(A[i] < cur_min):
                cur_min = A[i]
            iMax = i
       
        if( A[i]-A[i-1] > negdiff ):
            negdiff = A[i] - A[i-1]

        if( cur_max < A[i] ):
            cur_max = A[i]
            iMax = i
        elif( cur_min > A[i] and i < iMax ):
            cur_min = A[i]
          
    # last batch
    #print((min_sofar, max_sofar), (cur_min, cur_max), negdiff)
    if( cur_max-min_sofar > max_sofar-min_sofar ):
        max_sofar = cur_max           
    if( cur_max-cur_min > max_sofar - min_sofar):
        max_sofar = cur_max
        min_sofar = cur_min

    # If whole series is decreasing, our differences will be negative       
    if( negdiff <= 0 ): 
        return negdiff
    else:
        return max_sofar - min_sofar
    
# Returns the maximum difference (A[j] - A[i], where j > i) in given numeric list
def maxDiff(A):
    # Trivial case: Treat empty list and single element list as no difference
    if( len(A) <= 1 ):
        return 0
    
    # Since maximum element must follow minimum (j > i), we can just track min and diff
    # Idea is to ietrate over the list maintaining min and maxdiff we have so far    
    min_sofar = min(A[0], A[1])
    maxdiff_sofar = A[1] - A[0]
    for i in range(2, len(A)):
        if( A[i] - min_sofar > maxdiff_sofar ):
            maxdiff_sofar = A[i] - min_sofar
            
        if( A[i] < min_sofar ):
            min_sofar = A[i]
            
    return maxdiff_sofar
        
# Test

print(maxDiff([5, 10]))
print(maxDiff([3, 15, 1, 3, 7, 14]))
print(maxDiff([0, 14, 1, 9, 7, 15]))
print(maxDiff([1, 10, 2, 15, 1, -1, 10, 0, -2 , 3, 15]))
print(maxDiff([0, 5, 10, 10, 12, 15]))
print(maxDiff([15, 10, 8, 7, 4]))
print(maxDiff([-5, -2, -1, -1]))
