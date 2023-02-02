from bottledaemon import daemon_run
from bottle import route, run, template, static_file, TEMPLATE_PATH
from datetime import datetime
from pathlib import Path
from decouple import config
import Adafruit_DHT
import time

TEMPLATE_PATH.insert(0, str(Path(__file__).parent))
datafilelocation = "{}/{}".format(str(Path(__file__).parent),"data.txt")

# Read data from the file
def read_data_file():
    datafile = open(datafilelocation, 'r')
    data = datafile.readlines()
    temperature = data[0].rstrip()
    humidity = data[1].rstrip()
    timestamp = data[2].split()
    date, time = timestamp
    return temperature, humidity, date, time

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root="{}/{}".format(str(Path(__file__).parent),"static"))

@route('/')
def index():
    temperature, humidity, date, time = read_data_file()
    data = {'title': config('ROOM_NAME'),
            'temperature': temperature,
            'humidity': humidity,
            'date': date,
            'time': time
            }

    return template('template.tpl', data)

if __name__ == '__main__':
    daemon_run(host='0.0.0.0', port=8080)
