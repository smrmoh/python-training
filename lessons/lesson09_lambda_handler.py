import json


def lambda_handler(event, context):
    vdi_name = event.get('VDIName')
    action = event.get('Action')

    if not vdi_name or not action:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'VDIName and Action are required'
            })
        }

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Request validated',
            'VDIName': vdi_name,
            'Action': action
        })
    }


# Simulate an incoming request locally
test_event = {
    #'VDIName': 'poc-vdi-01',
    'Action': 'Start'
}

response = lambda_handler(test_event, None)

print(f"Status code: {response['statusCode']}")

response_body = json.loads(response['body'])
print(f"Message: {response_body['message']}")