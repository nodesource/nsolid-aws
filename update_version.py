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
print("\nRunning...\n")

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
            # Make AMIs public
            ec2 = boto3.client('ec2', region_name=console['region'])
            ec2.modify_image_attribute(
                Attribute='launchPermission',
                ImageId=console['ami'],
                OperationType='add',
                UserGroups=[
                    'all'
                ]
            )
            ec2.modify_image_attribute(
                Attribute='launchPermission',
                ImageId=runtime['ami'],
                OperationType='add',
                UserGroups=[
                    'all'
                ]
            )
            # Update File
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
consoleContents = s3.list_objects_v2(Bucket="ns-cloud-artifacts", Prefix="nsolid/nsolid-console")
runtimeContents = s3.list_objects_v2(Bucket="ns-cloud-artifacts", Prefix="nsolid/nsolid-runtime")
consoleKeys = []
runtimeKeys = []
for c in consoleContents['Contents']:
    consoleKeys.append({"date": c['LastModified'].strftime('%s'),"key": c['Key']})
for r in runtimeContents['Contents']:
    runtimeKeys.append({"date": r['LastModified'].strftime('%s'),"key": r['Key']})
consoleKeys = sorted(consoleKeys, key=lambda x: x['date'], reverse=True)
runtimeKeys = sorted(runtimeKeys, key=lambda x: x['date'], reverse=True)
consolePreviousKey = consoleKeys[0]['key']
runtimePreviousKey = runtimeKeys[0]['key']
if consolePreviousKey == 'nsolid/nsolid-console-' + nsolidVersion.replace('.', '') + '.json':
    print('deleting Console')
    s3.delete_object(
        Bucket='ns-cloud-artifacts',
        Key=consolePreviousKey
    )
    consoleContents = s3.list_objects_v2(Bucket="ns-cloud-artifacts", Prefix="nsolid/nsolid-console")
    consoleKeys = []
    for c in consoleContents['Contents']:
        consoleKeys.append({"date": c['LastModified'].strftime('%s'),"key": c['Key']})
    consoleKeys = sorted(consoleKeys, key=lambda x: x['date'], reverse=True)
    consolePreviousKey = consoleKeys[0]['key']
if runtimePreviousKey == 'nsolid/nsolid-runtime-' + nsolidVersion.replace('.', '') + '.json':
    print('deleting Runtime')
    s3.delete_object(
        Bucket='ns-cloud-artifacts',
        Key=runtimePreviousKey
    )
    runtimeContents = s3.list_objects_v2(Bucket="ns-cloud-artifacts", Prefix="nsolid/nsolid-runtime")
    runtimeKeys = []
    for r in runtimeContents['Contents']:
        runtimeKeys.append({"date": r['LastModified'].strftime('%s'),"key": r['Key']})
    runtimeKeys = sorted(runtimeKeys, key=lambda x: x['date'], reverse=True)
    runtimePreviousKey = runtimeKeys[0]['key']
consoleObj = s3.get_object(Bucket="ns-cloud-artifacts", Key=consolePreviousKey)
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
                                updatedLine = line.replace(oldConsole['ami'], newConsole['ami'])
                                outFile.write(updatedLine)
                            else:
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
                                updatedLine = line.replace(oldRuntime['ami'], newRuntime['ami'])
                                outFile.write(updatedLine)
                            else:
                                outFile.write(line)

print('Update Complete.')
