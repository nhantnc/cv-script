import base64
import json
import secrets

import aws_encryption_sdk
from aws_encryption_sdk import CommitmentPolicy

from settings.settings import settings

def encrypt_data(data):
    client = aws_encryption_sdk.EncryptionSDKClient(commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT)
    key_id = settings['kms_key_id']
    salt = secrets.token_hex(16)
    kms_kwargs = dict(key_ids=[key_id])
    encryption_context = dict(salt=salt)
    master_key_provider = aws_encryption_sdk.StrictAwsKmsMasterKeyProvider(**kms_kwargs)
    ciphertext, _ = client.encrypt(source=data, key_provider=master_key_provider,
                                                  encryption_context=encryption_context)
    return {
        "cipher": base64.b64encode(ciphertext).decode("utf-8"),
        "salt": salt
    }


def decrypt_data(encrypted_data):
    if not encrypted_data:
        return None
    if encrypted_data.get('cipher') == None:
        return encrypted_data
    
    key_id = settings['kms_key_id']
    client = aws_encryption_sdk.EncryptionSDKClient(commitment_policy=CommitmentPolicy.REQUIRE_ENCRYPT_REQUIRE_DECRYPT)
    kms_kwargs = dict(key_ids=[key_id])

    master_key_provider = aws_encryption_sdk.StrictAwsKmsMasterKeyProvider(**kms_kwargs)
    cycled_plaintext, decrypted_header = client.decrypt(source=base64.b64decode(encrypted_data['cipher']),
                                                        key_provider=master_key_provider)

    salt = decrypted_header.encryption_context['salt']
    if (encrypted_data['salt'] != salt):
        raise Exception("Encryption Context does not match expected values")
    return json.loads(cycled_plaintext)


def get_client_from_key_id(arn):
    return arn.split(':')[3]
