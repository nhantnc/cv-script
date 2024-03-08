import boto3

def create_role_session_name(id):
  timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
  return f"{id}-{timestamp}"

def renew_assumed_role(role_arn, session_name, external_id):
    """
    Function to renew an assumed role using AWS STS.

    :param role_arn: The ARN of the role to assume :param session_name: An identifier for the assumed role session
    :param session_name: An identifier for the assumed role session
    :param external_id: A unique identifier that is used by third parties when assuming roles in their customers'
    accounts
    :return: Temporary security credentials (access key, secret access key, session token)
    """
    sts_client = boto3.client('sts', region_name='us-east-1')

    # Call the assume_role method of the STSConnection object and pass the role
    # ARN and a role session name.
    assumed_role_object = sts_client.assume_role(
        RoleArn=role_arn,
        RoleSessionName=session_name,
        ExternalId=external_id
    )

    # From the response that contains the assumed role, get the temporary
    # credentials that you can use to make subsequent API calls
    credentials = assumed_role_object['Credentials']

    return {
        'access_key': credentials['AccessKeyId'],
        'secret_key': credentials['SecretAccessKey'],
        'session_token': credentials['SessionToken']
    }
