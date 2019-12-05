'''
author: Levi
synopsis: To download file from storage bucket 
'''

from google.cloud import storage

def get_credentials():
    bucket_name = '<your-bucket-name>'
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.get_blob('to/path/file')
    results = blob.download_as_string().decode()
    print(results)

get_credentials()