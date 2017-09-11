from peewee import *
import config

mysql_db = MySQLDatabase(config.db_database)

class BaseModel(Model):
    class Meta:
        database = mysql_db

class dnszone(BaseModel):
    name = TextField(),
    type = 'A',
    content = TextField