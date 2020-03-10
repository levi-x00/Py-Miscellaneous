'''
Author: Levi
Purpose: for update lambda function runtime
ToRun:
    $ python update-function-runtime.py <profile-name>
    $ # example
    $ python update-function-runtime.py dev-account
'''

import boto3
from boto3.session import Session 
from pprint import pprint as pp
from sys import argv

class Lambda:

    __api = None 
    __region = 'ap-southeast-1'

    def __init__(self, session=None):
        self.__api = boto3.client('lambda', region_name=self.__region) if session is None else session.client('lambda', region_name=self.__region)
        

    def list_functions(self):
        kwargs = {}
        while True:
            response = self.__api.list_functions(
                FunctionVersion='ALL',
                MaxItems=50,
                **kwargs
            )

            yield response['Functions']

            if 'NextMarker' in response:
                kwargs['Marker'] = response['NextMarker']
            else:
                break

    def update_function_config(self, function_name):
        response = self.__api.update_function_configuration(
            FunctionName=function_name,
            Runtime='nodejs12.x',
            TracingConfig={
                'Mode': 'PassThrough'
            }
        )
        print(response)

if __name__ == '__main__':
    # profile = argv[1]
    # session = Session(profile_name=profile)
    # lbd = Lambda(session)
    lbd = Lambda()
    lists_functions = list(lbd.list_functions())

    for list_fns in lists_functions:
        for fn in list_fns:
            if 'nodejs' in fn['Runtime'] and 'LATEST' in fn['Version']:
                lbd.update_function_config(fn['FunctionName'])
