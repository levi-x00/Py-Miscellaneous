'''
author: Levi
purpose: for update lambda function runtime
'''

import boto3
from pprint import pprint as pp 

lbd = boto3.client('lambda', region_name='ap-southeast-1')

def list_functions():
    kwargs = {}
    while True:
        response = lbd.list_functions(
            FunctionVersion='ALL',
            MaxItems=50,
            **kwargs
        )

        yield response['Functions']

        if 'NextMarker' in response:
            kwargs['Marker'] = response['NextMarker']
        else:
            break

def update_function_config(function_name):
    response = lbd.update_function_configuration(
        FunctionName=function_name,
        Runtime='nodejs12.x'
    )
    print(response)

if __name__ == '__main__':

    lists_functions = list(list_functions())

    for list_fns in lists_functions:
        for fn in list_fns:
            if 'nodejs' in fn['Runtime'] and 'LATEST' in fn['Version']:
                update_function_config(fn['FunctionName'])
