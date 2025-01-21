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