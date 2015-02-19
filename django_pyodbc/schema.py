
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
import pyodbc as Database

class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    '''TODO: add these for sql server'''
    #sql_create_sequence = "CREATE SEQUENCE %(sequence)s"
    #sql_delete_sequence = "DROP SEQUENCE IF EXISTS %(sequence)s CASCADE"
    #sql_set_sequence_max = "SELECT setval('%(sequence)s', MAX(%(column)s)) FROM %(table)s"
    #sql_create_varchar_index = "CREATE INDEX %(name)s ON %(table)s (%(columns)s varchar_pattern_ops)%(extra)s"
    #sql_create_text_index = "CREATE INDEX %(name)s ON %(table)s (%(columns)s text_pattern_ops)%(extra)s"
    
    def create_model(self,model):

        '''todo'''
