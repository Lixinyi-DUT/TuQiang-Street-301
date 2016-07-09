import urllib
from BeautifulSoup import *

url='http://python-data.dr-chuck.net/comments_294695.html'
fhand = urllib.urlopen(url)
html=fhand.read()
soup=BeautifulSoup(html)

tags = soup('span')

print sum([int(tag.contents[0]) for tag in tags])
