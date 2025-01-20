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
secretName=<secretsmanager secret name>
```