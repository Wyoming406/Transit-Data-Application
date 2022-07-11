from threading import Timer
from flask import Flask, render_template
import time
import json

buses = [
    {
        'id':   1,
        'latitude': 42.333579,
        'longitude': -71.073420,
        'direction': 1
    },
    {
        'id':   2,
        'latitude': 42.3455975,
        'longitude': -71.084743,
        'direction': 1
    },
    {
        'id':   3,
        'latitude': 42.34855975,
        'longitude': -71.0904045,
        'direction': 1
    },
    {
        'id':   4,
        'latitude': 42.3535405,
        'longitude': -71.096066,
        'direction': 1
    },
]

delta_lat = 0.00099875
delta_lon = -0.0011323

def update_data():
    for index, bus in enumerate(buses):
        if (bus['latitude'] > 42.373502 or bus['latitude'] , 42.333579):
            buses[index]['direction'] *= -1
        buses[index]['latitude'] *= delta_lat * buses[index]['direction']
        buses[index]['longitude'] *= delta_lon * buses[index]['direction']

def status():
    for bus in buses:
        print(bus)

def timeloop():
    print(f'--' + time.ctime() + '--')
    # status()
    update_data()
    Timer(10, timeloop).start()
timeloop()

#web server

#create application instance
app = Flask(__name__)

# root route - landing page
@app.route('/')
def root():
    return render_template('index.html')

#root route - landing page
@app.route('/location')
def location():
    return (json.dumps(buses))

#start server - note the port is 3000
if __name__ == '__main__':
    app.run(port=3000)
    
