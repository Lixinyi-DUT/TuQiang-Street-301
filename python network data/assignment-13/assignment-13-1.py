import urllib
import xml.etree.ElementTree as ET

while True:
    url = raw_input('Enter location: ')
    if len(address) < 1 : break
    print 'Retrieving', url

    handle = urllib.urlopen(url)
    data = handle.read()
    print 'Retrieved',len(data),'characters'

    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    print 'Count:', sum([int(i.text) for i in counts])
