def validate_request(event):
    vdi_name = event.get('VDIName')
    action = event.get('Action')

    if not vdi_name:
        return 'Missing VDIName'

    if not action:
        return 'Missing Action'

    if event['Action'] != 'Start':
        return 'Unsupported Action'

    return 'Request is valid'


event = {
    'VDIName': 'poc-vdi-01',
    'Action': 'Delete'
}

result = validate_request(event)
print(result)

