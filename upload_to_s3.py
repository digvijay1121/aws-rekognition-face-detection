import boto3
import os

# Create S3 client
s3 = boto3.client(
    "s3",
    region_name=os.environ["AWS_REGION"]
)

bucket_name = os.environ["S3_BUCKET_NAME"]
file_name = "employee.jpg"

# Upload image
s3.upload_file(file_name, bucket_name, file_name)

print(f"{file_name} uploaded successfully to {bucket_name}")
