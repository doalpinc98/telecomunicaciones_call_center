import pandas as pd
from sqlalchemy import create_engine, inspect
import os
from dotenv import load_dotenv
load_dotenv()
db_config = {'user':os.getenv('tripleten_sql_user'),         # nombre de usuario
             'pwd': os.getenv('tripleten_sql_pwd'), # contraseña
             'host': os.getenv('tripleten_sql_host'),
             'port': 6432,              # puerto de conexión
             'db': os.getenv('tripleten_sql_db')}          # nombre de la base de datos

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
                                                                     db_config['pwd'],
                                                                       db_config['host'],
                                                                       db_config['port'],
                                                                       db_config['db'])


engine = create_engine(connection_string, connect_args={'sslmode':'require'},pool_size=10, max_overflow=20)
inspector=inspect(engine)
schemas=inspector.get_schema_names()

for schema in schemas:
    print("schema: %s" % schema)
    for table_name in inspector.get_table_names(schema=schema):
        print(f'table_name: ',table_name, f'----------------------------')
        for column in inspector.get_columns(table_name,schema=schema):
            print("Column: %s" % column)
