from decoupled import config
import psycopg2


def get_connection():
    try:
        return psycopg2.connect(
            host=config("POSTGRES_HOST"),
            user=config("POSTGRES_USER"),
            password=config("POSTGRES_PASS"),
            db=config("POSTGRES_DB"),
        )
    except Exception as e:
        print(e)
