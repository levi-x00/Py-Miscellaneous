'''
AUTHOR  : Levi
email   : rezhapzz@gmail.com
synopsis: Delete a logGroup in Google Stackdriver Logging
'''

from google.cloud import logging
from google.api_core.exceptions import ClientError

client = logging.Client()
logger = client.logger('levi-test-logging')

try: 
    logger.delete()
except ClientError as e:
    print(f'Error: {e.args[0]}')

