#Below is a nested dictionary
event = {
    'invocationSource': 'FulfillmentCodeHook',
    'sessionState': {
        'sessionAttributes': {},
        'intent': {
            'name': 'StartDesktop',
            'state': 'ReadyForFulfillment',
            'slots': {
                'VDIName': {
                    'value': {
                        'interpretedValue': 'poc-vdi-01'
                    }
                }
            }
        }
    }
}

session_state = event['sessionState']
intent = session_state['intent']

print(f"intent: {intent['name']}")

