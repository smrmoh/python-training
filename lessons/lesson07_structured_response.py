def validate_request(event):
    vdi_name = event.get('VDIName')
    action = event.get('Action')

    if not vdi_name:
        return {
            'is_valid': False,
            'message': 'Missing VDIName'
        }

    if not action:
        return {
            'is_valid': False,
            'message': 'Missing Action'
        }

    if action != 'Start':
        return {
            'is_valid': False,
            'message': 'Unsupported Action'
        }

    return {
        'is_valid': True,
        'message': 'Request is valid'
    }

event = {
    'VDIName': 'poc-vdi-01',
    'Action': 'Delete'
}

result = validate_request(event)

if result['is_valid']:
    print('Validation passed. Ready to prepare backend request.')
else:
    print(f"Request rejected: {result['message']}")


#print(result['is_valid'])
#print(result['message'])

#print(result)