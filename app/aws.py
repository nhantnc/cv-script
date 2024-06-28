import json
from utils import aws_utils, kms_utils
from db.database import get_db_conn

def renew_assumed_role():
    with open('input/assumed_role.json', 'r') as f:
        data = json.load(f)
        response = aws_utils.renew_assumed_role(data['roleArn'], data['RoleSessionName'], data['handshakeId'])
        print("Assumed Role Renewed Successfully ==>")
        print(response)

def renew_assumed_role_from_db(account_id):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute(f"""SELECT i."variant" FROM integration i WHERE i.id = {account_id}""")
    data = cur.fetchone()
    conn.close()
    variant = kms_utils.decrypt_data(data[0])
    role_session_name = variant['roleArn'].split('/')[-1]
    response = aws_utils.renew_assumed_role(variant['roleArn'], role_session_name, variant['handshakeId'])
    print("=====================================================")
    print("Assumed Role Renewed Successfully ==>")
    print(response)

