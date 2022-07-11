from threading import Timer
import urllib.request
import time
import json

def locations():
    url = "http://localhost:3000/location"
    response = urllib.request.urlopen(url).read()
    data = json.loads(response)
    for bus in data:
        print(bus)


def timeloop():
    print(f'--' + time.ctime() + '--')
    locations()
    Timer(10, timeloop).start()
timeloop()
