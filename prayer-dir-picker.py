#!/usr/bin/env python

# Imports
import os
from random import randint

# Constants
firstPage = 4
lastPage = 34
rowsPerPage = 5
colsPerPage = 2


# Choose a random page, row, and column.
page = randint( firstPage, lastPage )
row = randint( 1, rowsPerPage )
col = randint( 1, colsPerPage )


# Prompt the user to pray for that person in the church directory.
os.system( 'clear' )
print( "Take out your church directory.\n" )
print( "Go to page %d and pray for the person in row %d column %d.\n" % ( page, row, col ) )
