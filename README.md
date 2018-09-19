# S3presignedURL-lambda

This service takes a filename and time in minutes as input and outputs a presigned S3 URL with expiry time equal to input time. 
This can be used to integrate with slack as a slash app

Deployment using serverless:
```
sls deploy --aws-profile {aws profile name}
```

Call the generated URL from slack /gets3URL file={filename},time=5
