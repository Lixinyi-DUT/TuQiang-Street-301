import urllib
import json

while True:
    '''url = raw_input('Enter location: ')
    if len(address) < 1 : break'''
    url='http://python-data.dr-chuck.net/comments_294696.json'
    print 'Retrieving', url

    handle = urllib.urlopen(url)
    data = handle.read()
    print 'Retrieved',len(data),'characters'

    js=json.loads(str(data))
    comments=js['comments']
    counts=[int(i['count']) for i in comments]
    print 'Count:', len(counts)
    #counts=[int(i.values) for i in js]
    print 'Sum:', sum(counts)
    break
