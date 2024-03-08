from environs import Env

env = Env()
env.read_env()

settings = {
    "kms_generator_key_id": env.str("AWS_KMS_GENERATOR_KEY_ID"),
    "kms_key_id": env.str("AWS_KMS_KEY_ID"),
}
