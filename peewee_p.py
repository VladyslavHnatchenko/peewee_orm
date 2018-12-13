from peewee import *


user = 'root'
password = 'root'
db_name = 'peewee_demo'

db_handle = MySQLDatabase(
    db_name, user=user,
    password=password,
    host='localhost'
)
