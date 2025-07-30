# instance/config.py
import os
db_host = os.getenv("DB_HOST", "localhost")
# Configurações do banco de dados (ex: Amazon RDS)
DATABASE_URI = 'mysql://admin:admin123@{db_host}/contatos_db'

# Configurações de ambiente
DEBUG = False  # Em produção, desative o modo debug
