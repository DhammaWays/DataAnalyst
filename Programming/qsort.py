# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:50:18 2016

@author: lsharma
"""

"""Implement quick sort in Python.
Input a list.
Output a sorted list."""

def qsort(array, s, e): # helper function to allow in-place sort
    if( e <= s ): # just one element or empty, return as it is
        pass
    elif( e-s == 1 ): # two elements, just swap them if needed
        if( array[s] > array[e] ):
            temp = array[e]
            array[e] = array[s]
            array[s] = temp
    else:
        shift = True
        i = s
        p = e
        while( shift ):
            while( i < p and array[i] <= array[p] ): # find next element on left which is bigger then pivot 
                i += 1
            
            if( i >= p ): # pivot is in right place, need to sort left and right side
                shift = False
                qsort(array, s, p-1)
                qsort(array, p+1, e)
            else: # shift pivot to left
                temp = array[p]
                array[p] = array[i]
                array[i] = array[p-1]
                array[p-1] = temp
                p -= 1
                shift = True
                
    return array
    
def quicksort(array):
    return qsort(array, 0, len(array)-1)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)

#test = [1, 2, 3, 4, 5, 6]
#print quicksort(test)

#test = [21, 15, 10, 7, 5, 4, 3, 1, -1]
#print quicksort(test)
