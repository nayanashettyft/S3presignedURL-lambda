#!/usr/bin/env python
# requires the boto module
import boto3
from boto.s3.connection import S3Connection
import time
import datetime

def lambda_handler(event, context):
    print("Received event")
    resp = "Hello"
    result,filepath,expTime = getdata(event['queryStringParameters']['text'])
    if result:
        resp = getsignedURL(filepath, expTime)
    else:
        resp = "Invalid input"
    return {"statusCode":200, "body": resp}


def getdata(string):
    try:
        data = dict(x.split('=') for x in string.split(','))
        filepath = data['file']
        expTime = data['time']
        return 1,filepath, expTime
    except:
        return 0,0,0


def getsignedURL(filepath, expTime):
    bucket_name = "s3signed-example"
    s3path = "test/"
    keypath = s3path + filepath
    expTime_sec = int(expTime) * 60

    if validateS3object(keypath):
        params = {
            'Bucket': bucket_name,
            'Key': keypath
        }
        s3 = boto3.client('s3')
        uurl = s3.generate_presigned_url('get_object', Params=params, ExpiresIn=expTime_sec)
        return "Your URL: " + uurl
    else:
        return "Invalid filename"


def validateS3object(keypath):
    bucket_name = "s3signed-example"
    s3 = boto3.client('s3')
    try:
        response = s3.head_object( Bucket=bucket_name, Key=keypath)
        return 1
    except:
        return 0
    