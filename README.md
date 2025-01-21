# hypedb
minimal library to connect to Hypo DB

This library expects the following file to exists in the home diretory of the user running the script:

db.toml
```
[environemnt]
host = <host>
port = <port>
user = <username>
database = <database name>
password = <password>
secretName=<secretsmanager secret name> # optional for using AWS Secrets Manager
```

## Usage

The `connect` function allows you to connect to the Hypo DB. It takes the following parameters:

- `environment` (str): The environment configuration to use.

Example:
```python
from hypodb import connect

connection = connect("production")
```
