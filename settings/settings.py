from environs import Env

env = Env()
env.read_env()

settings = {
    "kms_generator_key_id": env.str("AWS_KMS_GENERATOR_KEY_ID"),
    "kms_key_id": env.str("AWS_KMS_KEY_ID"),
    "host": env.str("DB_HOST"),
    "database": env.str("DB_DATABASE"),
    "user": env.str("DB_USER"),
    "password": env.str("DB_PASSWORD"),
    "options": env.str("DB_OPTIONS"),
}
