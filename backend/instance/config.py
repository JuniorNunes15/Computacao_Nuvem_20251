import os

db_user = os.getenv("MYSQL_USER", "admin")
db_password = os.getenv("MYSQL_PASSWORD", "admin123")
db_host = os.getenv("MYSQL_HOST", "localhost")
db_name = os.getenv("MYSQL_DB", "contatos_db")


