import boto3
import pandas as pd
import io
import s3fs
import requests


# 1. Initialize the S3 client
s3_client = boto3.client('s3')

# 2. Get the object from S3
bucket_name = 'sim2023'
file_key = '/mlfornlp/archelec_metadata.csv'

response = s3_client.get_object(Bucket=bucket_name, Key=file_key)

# 3. Read the body of the response (the CSV content)
file_content = response['Body'].read()

# 4. Load into Pandas using io.BytesIO
df = pd.read_csv(io.BytesIO(file_content))

print(df["ocr_url"].iloc[0])


url = df["ocr_url"].iloc[0]
# Fetch the content
response = requests.get(url)
if response.status_code == 200:
    # Use .text to get the content as a string
    content = response.text
    print(content[:500])  # Print the first 500 characters
else:
    print(f"Failed to retrieve file. Status code: {response.status_code}")
