import json

message_body = {
    'VDIName': 'poc-vdi-01',
    'Action': 'Start'
}

message_json = json.dumps(message_body)

print(message_body)
print(type(message_body))

print(message_json)
print(type(message_json))

received_message = json.loads(message_json)

print(received_message)
print(type(received_message))
print(f"Desktop: {received_message['VDIName']}")
print(f"Action: {received_message['Action']}")