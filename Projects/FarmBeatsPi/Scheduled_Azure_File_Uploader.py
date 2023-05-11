#!/usr/bin/env python
#
# Azure Blob Storage file uploaded
#	*	Uploads a file to Azure Blob Storage.
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

import os
import uuid
import logging
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

logger = logging.getLogger('azureuploadlogger')
logger.setLevel(logging.ERROR)
handler = logging.FileHandler('azureUploader.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

def upload_blob_file(self, blob_service_client: BlobServiceClient, container_name, file_path, file_name):
    container_client = blob_service_client.get_container_client(container=container_name)
    with open(file=file_path, mode="rb") as data:
        blob_client = container_client.upload_blob(name=file_name, data=data, overwrite=True)

# Retrieve the connection string for use with the application. The storage
# connection string is stored in an environment variable on the machine
# running the application called AZURE_STORAGE_CONNECTION_STRING. If the environment variable is
# created after the application is launched in a console or with Visual Studio,
# the shell or application needs to be closed and reloaded to take the
# environment variable into account.
connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# Create a local directory to hold blob data
local_path = "/home/pi/GrovePi/Projects/FarmBeatsPi/"

# Create a file in the local data directory to upload and download
local_file_name = "farmbeatspi_log.csv"

upload_file_path = os.path.join(local_path, local_file_name)


# Create a blob client using the local file name as the name for the blob
# blob_client = blob_service_client.get_blob_client(container=farmbeatspicsv, blob=local_file_name)
try:
    upload_blob_file("fbpicsv" , blob_service_client, "farmbeatspicsv", upload_file_path, local_file_name)
    logger.info("Uploaded file: " + local_file_name)
except Exception as e:
    logger.error(e)
