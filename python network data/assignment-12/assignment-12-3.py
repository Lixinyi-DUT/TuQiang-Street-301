import urllib
from BeautifulSoup import *

url='http://python-data.dr-chuck.net/known_by_Insiya.html '

count = 7
pos= 18
print 'count', count
print 'position', pos

for i in range(count+1):
    print 'Retrieving',url
    html=urllib.urlopen(url).read()
    soup=BeautifulSoup(html)
    tags = soup('a')
    url = tags[pos-1].get('href', None)
