#!/usr/bin/env python
#
#
#
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import grovepi
import math
import time

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
dht_sensor = 2  # The Sensor goes on digital port D4.
# temp_humidity_sensor_type
dht_white = 1   # The White colored sensor.

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0
#grovepi.pinMode(light_sensor,"INPUT")

# Connect the Grove Moisture Sensor to analog port A2
# SIG,NC,VCC,GND
moisture_sensor = 2

log_file="plant_monitor_log.csv"

while True:
    try:
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(dht_sensor,dht_white)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("Temperature: %.02f C Humidity: %.02f%%" %(temp, humidity))

        # Get Light sensor value
        light_sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of light sensor in K
        #if light_sensor_value > 0:
        #    light_resistance = (float)(1023 - light_sensor_value) * 10 / light_sensor_value
        #    print("Light Sensor Level: %d K: %.2f" %(light_sensor_value,  light_resistance))

        # Get Moisture sensor value
        moisture_sensor_value = grovepi.analogRead(moisture_sensor)

        curr_time = time.strftime("%Y-%m-%d:%H-%M-%S")

        # Print the collected sensor readings to terminal
        print(("Time:%s\nMoisture: %d\nLight: %d\nTemp: %.2f\nHumidity:%.2f %%\n" %(curr_time,moisture_sensor_value,light_sensor_value,temp,humidity)))

		# Save the sensor readings to the CSV file
        f=open(log_file,'a')
        f.write("%s,%d,%d,%.2f,%.2f;\n" %(curr_time,moisture_sensor_value,light_sensor_value,temp,humidity))
        f.close()

        time.sleep(5)

    except IOError:
        print ("Error")
