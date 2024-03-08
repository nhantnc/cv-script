import json
from utils import aws_utils

def renew_assumed_role():
    with open('input/assumed_role.json', 'r') as f:
        data = json.load(f)
        response = aws_utils.renew_assumed_role(data['roleArn'], data['RoleSessionName'], data['handshakeId'])
        print("Assumed Role Renewed Successfully ==>")
        print(response)