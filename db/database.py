import psycopg2
import math
import json
import time
from settings.settings import settings

def get_db_conn():
    # establishing the connection
    return psycopg2.connect(
        host=settings["host"],
        database=settings["database"],
        user=settings["user"],
        password=(settings["password"]),
        options=settings["options"],
    )

