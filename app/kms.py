import json
from utils import kms_utils

# Decrypt data from json file
def decrypt_data():
    with open('input/encrypted.json', 'r') as f:
        encrypted_data = json.load(f)
        decrypted_data = kms_utils.decrypt_data(encrypted_data)
        print("Data Decrypted Successfully")
        print(decrypted_data)
