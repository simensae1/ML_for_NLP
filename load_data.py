import boto3
import pandas as pd
import io
import s3fs

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

print(df.head())
