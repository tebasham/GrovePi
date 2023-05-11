#!/usr/bin/env python
#
# Create fresh CSV for receiving FarmBeatsPi Data
#	*	Backup existing CSV file
#   *   Overwrite existing CSV file with fresh header row
#	
'''
## License

The MIT License (MIT)

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

import csv
import os
import shutil
import time

logFilePath = "/home/pi/GrovePi/Projects/FarmBeatsPi/"
logFileName = "farmbeatspi_log.csv"
logFile = open("/home/pi/GrovePi/Projects/FarmBeatsPi/farmbeatspi_log.csv", 'w', newline='')

# Copy provided file
def backupLogFile(srcFile,dstFile):
    shutil.copyfile(srcFile, dstFile)
    return 1

# Write data to the CSV file
def writeCsvData(headerRow):
    dataWriter = csv.writer(logFile)
    dataWriter.writerow(headerRow)
    return 1 

try:
    currTime = time.strftime("%Y-%m-%d:%H-%M-%S")

    backupLogFileName = currTime + logFileName

    backupLogFile(logFilePath + logFileName,logFilePath + backupLogFileName)

    # Write the header row to the csv file
    writeCsvData("DateTime,SoilMoisture,Temperature,Humidity")

    # Close the file
    logFile.close()

except KeyboardInterrupt:
    logFile.close()
except IOError:
    print("Error")