__author__ = 'Ning'
import time as t
import shelve

s = shelve.open('my_students', writeback=True)
while True:
    entry = input('Begin scanning or enter q to quit: ')

    if entry in ['q', 'Q']:
        s.close()
        break
    elif 9<int(t.strftime("%H")) and 5<int(t.strftime("%M")):
        l = input("Late Bell rang, would you like to mark students late? (l):")
        if l == "l":
            tardy = input("Who are late?")
            s[entry]['lates'].append("%s at %s" %(tardy,t.time()))
            s[entry]['attendance'].append(t.time())
        elif l == "no" or l == "No":
            print(s[entry]['name'] + ' scanned in at ' + t.strftime('%H:%M\n', t.localtime()))
            s[entry]['attendance'].append(t.time())
    elif entry not in s.keys():
        print('ID not found; scan again.')

    else:
        print(s[entry]['name'] + ' scanned in at ' + t.strftime('%H:%M\n', t.localtime()))
        s[entry]['attendance'].append(t.time())





