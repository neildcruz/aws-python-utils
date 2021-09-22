###
#    Utility to determine which Lambda functions are consuming account level reserved capacity
###

import boto3

# Boto3 Client
client = boto3.client('lambda')


def main():

    # Get all lambda functions
    func_response = client.list_functions()
    functions = func_response['Functions']

    # Create list of function names
    function_names = []
    for function in functions:
        function_names.append(function['FunctionName'])

    # Iterate over function names and list functions with reserved executions
    for func in function_names:
        concurrency_response = client.get_function_concurrency(
            FunctionName=func)
        reserved_concurrency = 0
        if 'ReservedConcurrentExecutions' in concurrency_response:
            reserved_concurrency = concurrency_response['ReservedConcurrentExecutions']
        if reserved_concurrency > 0:
            print(func + '      ' +
                  str(reserved_concurrency))


main()
