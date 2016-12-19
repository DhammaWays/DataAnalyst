# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:40:01 2016

@author: lsharma
"""

def maxDiff(A):
    if( A[1] > A[0] ):
        cur_max, max_sofar = A[1], A[1]
        cur_min, min_sofar = A[0], A[0]
    else:
        cur_max, max_sofar, cur_min, min_sofar = A[1], A[1], A[1], A[1]
        
    nextScan = False
    for i in range(2, len(A)):
        print("Enter=>",(min_sofar, max_sofar), (cur_min, cur_max), nextScan, A[i])
        if( not nextScan and A[i] < cur_max ):
            nextScan = True
            cur_max, cur_min = A[i], A[i]
        
        if(nextScan):
            if( cur_max > max_sofar ):
                max_sofar = cur_max           
                nextScan = False
            elif( cur_min < min_sofar):
                min_sofar = cur_min
                nextScan = False
           
        if( cur_max < A[i] ):
            cur_max = A[i]
        elif( cur_min > A[i] ):
            cur_min = A[i]
        print("Exit=>",(min_sofar, max_sofar), (cur_min, cur_max), nextScan, A[i])

        
    # last batch
    print((min_sofar, max_sofar), (cur_min, cur_max), nextScan)
    if( cur_max > max_sofar ):
        max_sofar = cur_max           
    elif( cur_min < min_sofar):
        min_sofar = cur_min

    return max_sofar - min_sofar
    
    
#A = [3, 15, 1, 3, 7, 14]
#A = [3, 14, 1, 3, 7, 15]
A = [1, 2, 1, 10, 0, 5]   
print(maxDiff(A))
