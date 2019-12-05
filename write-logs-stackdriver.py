'''
AUTHOR  : Levi
email   : rezhapzz@gmail.com
synopsis: sample writing logs to Google Stackdriver Logging
'''

from google.cloud import logging
from google.api_core.exceptions import ClientError

client = logging.Client()

logger = client.logger('levi-test-logging')

try:
    for i in range(5):
        logger.log_struct({ 'message': 'hello'})
except ClientError as e:
    print(e)