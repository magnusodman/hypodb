import json
from pathlib import Path

import boto3
import pymysql
import tomllib

db_config = tomllib.loads(Path("~/db.toml").expanduser().read_text())


def configs():
    return db_config.keys()


def get_config(environment: str):
    return db_config[environment]


def connect(environment: str):
    secret_name = db_config[environment].get(
        "secretName", None
    )  # Support AWS Secrets Manager
    if secret_name is not None:
        secret_manager = boto3.client("secretsmanager")
        password = json.loads(
            secret_manager.get_secret_value(SecretId=secret_name)["SecretString"]
        )["key"]
    else:
        password = db_config[environment]["password"]
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
