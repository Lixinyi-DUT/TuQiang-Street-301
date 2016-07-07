from datetime import datetime

def get_his_life():
    hisbirth = datetime(1926,8,17)
    now = datetime.now()
    diff = now-hisbirth
    hislife = diff.days * 24 * 3600 + diff.seconds
    return hislife

def prolong(hislife,donater):
    if donater>0:
        hislife = hislife + 1
        print('excited')
    else:
        print('I\'m angry')
    return hislife

hislife=get_his_life()
hath=range(2,-1,-1)
for life in hath:
    hislife=prolong(hislife,life)
print('Now he has '+str(hislife)+'s')
