#!/usr/bin/env python
#
# GrovePi Project for FarmBeats monitoring.
#	*	Reads the data from moisture, light, and temperature and humidity sensor. Logs the data to csv file.
#	
#	*	Sensor Connections on the GrovePi:
#			-> Grove Moisture sensor	- Port A2
#			-> Grove light sensor		- Port A0
#			-> Grove DHT sensors		- Port D2
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
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
import logging
import math
import time
import csv

# Connect the Grove DHT Pro Sensor to digital port D2
# SIG,NC,VCC,GND
dhtSensor = 2
# DHT Pro Sensor Type
dhtType = 1   # The White colored sensor.
#dhtType = 0    # The Blue colored sensor.

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
lightSensor = 0

# Connect the Grove Moisture Sensor to analog port A2
# SIG,NC,VCC,GND
moistureSensor = 2

logFile = open("/home/pi/GrovePi/Projects/FarmBeatsPi/farmbeatspi_log.csv", 'a', newline='')

logger = logging.getLogger('farmbeatsDataLogger')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler('farmbeatsDataLogger.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#Read the data from the sensors
def readSensor():
	try:
		moisture = grovepi.analogRead(moistureSensor)
		light = grovepi.analogRead(lightSensor)
		[temp,humidity] = grovepi.dht(dhtSensor,dhtType)
		#Return -1 in case of bad temp/humidity sensor reading
		if math.isnan(temp) or math.isnan(humidity):		#temp/humidity sensor sometimes gives nan
			return [-1,-1,-1,-1]
		return [moisture,light,temp,humidity]
	
	#Return -1 in case of sensor error
	except IOError as TypeError:
			return [-1,-1,-1,-1]

# Write data to CSV file
def writeCsvData(csvSensorData):
    dataWriter = csv.writer(logFile)
    dataWriter.writerow(csvSensorData)
    return 1 

try:
    currTime = time.strftime("%Y-%m-%d:%H-%M-%S")

    [moisture,light,temp,humidity] = readSensor()

    # Print the collected sensor readings to terminal
    # print(("Time: %s\nMoisture: %d\nLight: %d\nTemp: %.2f\nHumidity:%.2f %%\n" %(currTime,moisture,light,temp,humidity)))

    # Write the collected sensor readings to csv file
    writeCsvData([currTime,moisture,light,temp,humidity])

    # Close the file
    logFile.close()

    logger.info("Data collected and written to CSV")

except KeyboardInterrupt:
    logFile.close()
except IOError as e:
    logger.error(e)
