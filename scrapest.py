#Objective in this program is to obtain the title of the html page.
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(),features='html.parser')
#All these return the same value
print(bsObj.h1)
print(bsObj.html.body.h1)
print(bsObj.body.h1)
print(bsObj.html.h1)
print(bsObj.title)
print(bsObj.div)
#HANDLING ERRORS
#With the urlopen() two errors might occur,ie. page might not be found on the server, or the server may not be found.
'''try:
   html = urlopen("http://www.pythonscraping.com/pages/page1.html")
except HTTPError as e:
    print(e)
#return null, break, or do some other "Plan B"
else:
program continues.'''

#If the server is not found at all, the urlopen returns a None object.
# We can check if this is the case as follows
''''if html is None:
    print("URL is not found")
else:'''

#the next exception to check is if the beautifulsoup_obj has an nonExistentTag.
 #This returns the AttributeError which can be handled as follows,
'''
try:
    badContent = bsObj.nonExistingTag.anotherTag
except AttributeError as e:
    print("Tag was not found")
else:
    if badContent == None:
print ("Tag was not found")
    else:
    print(badContent)
 '''

#Final program with the two major exception handled.
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
     html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)