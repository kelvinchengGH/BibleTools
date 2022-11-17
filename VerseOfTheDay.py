#!/usr/bin/python

"""
Fetches the Verse of the Day from Bible Gateway
and prints it to the terminal.
"""


#############
# IMPORTS
#############
import os, subprocess, textwrap
from bs4 import BeautifulSoup


#############
# CONSTANTS
#############
LINE_LEN = 60
URL = 'https://www.biblegateway.com'


#############
# FUNCTIONS
#############
def getVerseOfTheDay():
    """ Fetch the verse of the day and its citation. """
    # Get the HTML for the site.
    cmd = [ 'curl', '-s', URL ]
    output = subprocess.check_output( cmd )

    # Parse it to get the verse of the day and the citation.
    soup = BeautifulSoup( output, 'html.parser' )
    
    citation = soup.find( 'span', { 'class' : 'citation' } )
    citationStr = citation.text
    
    verse = soup.find( 'div', { 'id' : 'verse-text' } )
    verseStr = verse.text.strip()

    return ( verseStr, citationStr )


def printVerse( verse, citation ):
    """ Print the verse in a pretty format. """
    print '~' * LINE_LEN
    print '\n'.join( textwrap.wrap( verse, LINE_LEN,
                                    break_long_words=False ) )
    print
    print citation
    print '~' * LINE_LEN


#############
# main()
#############
def main():
    os.system( 'clear' )
    verse, citation = getVerseOfTheDay()
    printVerse( verse, citation )

    
if __name__ == "__main__":
    main()

