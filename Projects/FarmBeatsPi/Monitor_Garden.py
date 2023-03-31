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
grovepi.pinMode(light_sensor,"INPUT")

# Connect the Grove Moisture Sensor to analog port A2
# SIG,NC,VCC,GND
moisture_sensor = 2

while True:
    try:
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(dht_sensor,dht_white)  
        if math.isnan(temp) == False and math.isnan(humidity) == False:
            print("temp = %.02f C humidity =%.02f%%" %(temp, humidity))

        # Get sensor value
        light_sensor_value = grovepi.analogRead(light_sensor)

        # Calculate resistance of sensor in K
        light_resistance = (float)(1023 - light_sensor_value) * 10 / light_sensor_value
        print("light_sensor_value = %d resistance = %.2f" %(light_sensor_value,  light_resistance))

        print(grovepi.analogRead(moisture_sensor))

        time.sleep(.9)

    except IOError:
        print ("Error")
