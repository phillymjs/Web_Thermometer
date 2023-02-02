# Web_Thermometer

My first Python project, now cleaned up a bit and improved with things I learned while doing my second Python project. This is a pair of Python3 scripts that read a DHT11 or DHT22 temperature/humidity module connected to a Raspberry Pi, and display it in a simple web page using the bottle framework. I use two separate scripts because one script that read the sensor on-demand caused delays in the page load.

The *thermo_read.py* script should be run via cron job at a repeating interval with the command "/path/to/venv/python3 thermo_read.py". When run, the script reads the sensor and writes the temperature, humidity, and date and time the reading was taken. It records that to *data.txt* in the same directory.

The *web_thermo.py* script should be started at boot via cron job, with the command "/path/to/venv/python3 web_thermo.py start". The script runs bottle as a daemon. The webserver will be located at http://ipaddress:8080. A browser pointed at that address will show the temperature, humidity, and the date and time the reading was taken.

The name of the room where the Pi with the sensor attached is set in .env, refer to *sample_env* if you wish to use the script yourself.