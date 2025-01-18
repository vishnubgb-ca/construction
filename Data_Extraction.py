import os
import boto3

def extract_data():
# Get AWS credentials from environment variables
  aws_access_key_id = os.environ.get("aws_access_key_id")
  aws_secret_access_key = os.environ.get("aws_secret_access_key")
  bucket_name = os.environ.get("bucket")  # Corrected variable name
  region = os.environ.get("region")

# Check if all the credentials are available
  if not all([aws_access_key_id, aws_secret_access_key, bucket_name, region]):
    print("Please set all the environment variables: aws_access_key_id, aws_secret_access_key, bucket, region")
    exit(1)

# Create a session using your credentials
  session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=region
  )

# Create an S3 client using the session
  s3 = session.client("s3")  # Use the session to create the client

# Generate a presigned URL for the S3 object
  try:
    url = s3.generate_presigned_url(
        ClientMethod="get_object",
        Params={"Bucket": bucket_name, "Key": "construction dataset.zip"},
        ExpiresIn=7500  # URL expiration time in seconds (adjust as needed)
    )
    print("Generated presigned URL:", url)
  except Exception as e:
    print("Error generating presigned URL:", str(e))
  return url

extract_data()

