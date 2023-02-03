from datetime import datetime
from pathlib import Path
import Adafruit_DHT
import time

datafilelocation = "{}/{}".format(str(Path(__file__).parent),"data.txt")

# Write data to file
def write_data_file(temperature,humidity):
    with open(datafilelocation, mode="w") as datafile:
        now = datetime.now()
        timestamp = now.strftime("%m/%d/%Y %H:%M:%S")
        datafile.writelines([str(temperature), '\n', str(humidity), '\n', timestamp])
    datafile.close()

def read_temp_sensor():
    sensor = 11
    pin = 4
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temperature = temperature * 9/5.0 + 32
    if humidity is not None and temperature is not None:
        write_data_file(temperature, humidity)
    else:    
        time.sleep(5)
        read_temp_sensor()

if __name__ == '__main__':
    read_temp_sensor()
