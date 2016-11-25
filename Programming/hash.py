# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:50:42 2016

@author: lsharma
"""

"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in 
        the table."""
        hvalue = self.calculate_hash_value(string)
        if( self.table[hvalue] ):
            self.table[hvalue].append(string)
        else:
            self.table[hvalue] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hvalue = self.calculate_hash_value(string)
        return hvalue if self.table[hvalue] and string in self.table[hvalue] else -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        return ord(string[0])*100 + ord(string[1]) # our hash is simply first char * 100 + second char
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')

