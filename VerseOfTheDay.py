"""
Fetches the Verse of the Day from Bible Gateway
and prints it to the terminal.
"""

import os, subprocess, textwrap
from bs4 import BeautifulSoup


os.system( 'clear' )


# Get the HTML for the site.
url = 'https://www.biblegateway.com'
cmd = [ 'curl', '-s', url ]
output = subprocess.check_output( cmd )


# Parse it to get the verse of the day and the citation.
soup = BeautifulSoup( output, 'html.parser' )

citation = soup.find( 'span', { 'class' : 'citation' } )
citationStr = citation.text

verse = soup.find( 'div', { 'id' : 'verse-text' } )
verseStr = verse.text.strip()


# Print the verse in a pretty format.
lineLen = 60
print '~' * lineLen
print '\n'.join( textwrap.wrap( verseStr, lineLen,
                                break_long_words=False ) )
print
print citationStr
print '~' * lineLen
