from bottledaemon import daemon_run
from bottle import route, run, template, static_file, TEMPLATE_PATH, response
from datetime import datetime
from pathlib import Path
from decouple import config
import Adafruit_DHT
import time
import json

TEMPLATE_PATH.insert(0, str(Path(__file__).parent))
DATA_FILE_LOCATION = "{}/{}".format(str(Path(__file__).parent),"data.txt")

# Read data from the file
def read_data_file():
    with open(DATA_FILE_LOCATION, mode="r") as datafile:
        data = datafile.readlines()
        temperature = data[0].rstrip()
        humidity = data[1].rstrip()
        timestamp = data[2].split()
        date, time = timestamp
        return temperature, humidity, date, time
    datafile.close()

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

@route('/raw')
def rawdata():
    temperature, humidity, date, time = read_data_file()
    response.headers['Content-Type'] = 'application/json'
    return json.dumps({'room': config('ROOM_NAME'),
                       'timestamp': f'{date}T{time}',
                       'temperature': temperature,
                       'humidity': humidity})

if __name__ == '__main__':
    daemon_run(host='0.0.0.0', port=config('WEBSERVER_PORT'))
