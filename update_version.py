#!/usr/bin/env python
import json
import shutil
import os
import boto3
s3 = boto3.client('s3')

nsolidVersion = raw_input("N|Solid Version:\n")
consoleFile = raw_input("N|Solid Console File (full path):\n")
runtimeFile = raw_input("N|Solid Runtime File (full path):\n")
consoleContent = json.loads(open(consoleFile).read())
runtimeContent = json.loads(open(runtimeFile).read())
'''
s3 = boto3.client('s3')
consoleContents = s3.list_objects_v2(Bucket="ns-cloud-artifacts", MaxKeys=1, Prefix="nsolid/nsolid-console")
runtimeContents = s3.list_objects_v2(Bucket="ns-cloud-artifacts", MaxKeys=1, Prefix="nsolid/nsolid-runtime")
consolePreviousKey = consoleContents['Content'][0]['Key']
consolePreviousKey = runtimeContents['Content'][0]['Key']
cosnoleObj = s3.get_object(Bucket="ns-cloud-artifacts", Key=consolePreviousKey)
runtimeObj = s3.get_object(Bucket="ns-cloud-artifacts", Key=runtimePreviousKey)
consoleBody = consoleObj['Body'].read()
runtimeBody = runtimeObj['Body'].read()
previousConsole = json.loads(consoleBody.decode('utf-8'))
previousRuntime = json.loads(runtimeBody.decode('utf-8'))
with open(consoleFile, 'rb') as consoleData:
    upload = s3.upload_fileobj(consoleData, 'ns-cloud-artifacts', 'nsolid/nsolid-console-' + nsolidVersion + '.json')
with open(runtimeFile, 'rb') as runtimeData:
    upload = s3.upload_fileobj(runtimeData, 'ns-cloud-artifacts', 'nsolid/nsolid-runtime-' + nsolidVersion + '.json')
'''

'''
Create a folder in S3 that has past json file for earlier image versions.
When this is run, upload the current file as well.

AMI-LIST can probably still work the same way (minus the double headers).
AMI Mappings will probably need to have a find and replace done on them,
referencing the old AMI ID it got from S3, and replacing with the new ID.
'''

# AMI-LIST.md update
if "**" + nsolidVersion + "**" in open('AMI-LIST.md').read():
    with open('AMI-LIST.md') as oldfile, open('.AMI-LIST.updated.md', 'w') as newfile:
        for line in oldfile:
            if "**" + nsolidVersion + "**" not in line:
                newfile.write(line)
else:
    shutil.copyfile('./AMI-LIST.md', './.AMI-LIST.updated.md')

for console in consoleContent['imageIds']:
    for runtime in runtimeContent['imageIds']:
        if console['region'] == runtime['region']:
            with open("./.AMI-LIST.updated.md", "r") as inFile:
                lines = inFile.readlines()
            with open("./.AMI-LIST.updated.md", "w") as outFile:
                correctRegion = False
                for line in lines:
                    if line.startswith("## " + console['region']):
                        correctRegion = True
                    if line.startswith("|----------------|") and correctRegion:
                        line = (line + "|   **" + nsolidVersion + "**    "
                                "| `" + console['ami'] + "` "
                                "| `" + runtime['ami'] + "` |\n")
                        correctRegion = False
                    outFile.write(line)

amiFile = open("./.AMI-LIST.updated.md").read()
with open('AMI-LIST.md', 'w') as originalFile:
    originalFile.write(amiFile)
os.remove("./.AMI-LIST.updated.md")

# AMI Maps update
