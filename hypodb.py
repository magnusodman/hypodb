import json
from pathlib import Path
import pymysql
import tomllib
import boto3

db_config = tomllib.loads(Path("~/db.toml").expanduser().read_text())


def connect(environment: str):
    secret_name = db_config[environment]["secretName"]
    secret_manager = boto3.client("secretsmanager")
    password = json.loads(
        secret_manager.get_secret_value(SecretId=secret_name)["SecretString"]
    )["key"]
    return pymysql.connect(
        host=db_config[environment]["host"],
        user=db_config[environment]["user"],
        password=password,
        db=db_config[environment]["database"],
        cursorclass=pymysql.cursors.DictCursor,
    )


if __name__ == "__main__":
    print(db_config)
    print(connect("hypoprod"))
