import mysql.connector
# Configura la conexión a MySQL
db_config = {
    "user": "root",
    "password": "micaelacorolaire",
    "host": "localhost",
    "database": "validationpersonaldatafastapi",
}

conn=mysql.connector.connect(**db_config)