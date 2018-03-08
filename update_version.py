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
    upload = s3.upload_fileobj(consoleData, 'ns-cloud-artifacts', 'nsolid/nsolid-console-' + nsolidVersion.replace('.', '') + '.json')
with open(runtimeFile, 'rb') as runtimeData:
    upload = s3.upload_fileobj(runtimeData, 'ns-cloud-artifacts', 'nsolid/nsolid-runtime-' + nsolidVersion.replace('.', '') + '.json')

# Console Update
for newConsole in consoleContent['imageIds']:
    for oldConsole in previousConsole['imageIds']:
        if newConsole['region'] == oldConsole['region']:
            templates = os.listdir('./templates')
            for template in templates:
                if ".json" in template:
                    with open("./templates/" + template, "r") as inFile:
                        lines = inFile.readlines()
                    with open("./templates/" + template, "w") as outFile:
                        for line in lines:
                            if oldConsole['ami'] in line:
                                line.replace(oldConsole['ami'], newConsole['ami'])
                            outFile.write(line)

# Runtime Update
for newRuntime in runtimeContent['imageIds']:
    for oldRuntime in previousRuntime['imageIds']:
        if newRuntime['region'] == oldRuntime['region']:
            templates = os.listdir('./templates')
            for template in templates:
                if ".json" in template:
                    with open("./templates/" + template, "r") as inFile:
                        lines = inFile.readlines()
                    with open("./templates/" + template, "w") as outFile:
                        for line in lines:
                            if oldRuntime['ami'] in line:
                                line.replace(oldRuntime['ami'], newRuntime['ami'])
                            outFile.write(line)

print('Update Complete.')
