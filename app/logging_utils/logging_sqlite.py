import logging
import sqlite3
from   models.logging_models import dbLogRecord

class sqlite_db_handler(logging.Handler):
    def __init__(self, database, table):
        super().__init__() # for python 3.X
        self.database = database
        self.table = table

        create_table_sql = sqlite_db_handler.getLogTableDefinition()
        conn = sqlite3.connect(self.database)
        conn.execute(create_table_sql)
        conn.commit()
        conn.close()

    def emit(self, record: logging.LogRecord):
        logRec = dbLogRecord(record)
        insert_sql = 'INSERT INTO logs(name,msg,levelname,asctime,relativeCreated,thread,threadName,funcName,filename) ' + \
            'VALUES (' + logRec.toCsv() + ');'

        print('insert_sql: {}'.format(insert_sql))    
        
        conn = sqlite3.connect(self.database)
        conn.execute(insert_sql)
        conn.commit()
        conn.close()        

    @staticmethod
    def getLogTableDefinition():
        return """
            CREATE TABLE IF NOT EXISTS logs (
                id integer  PRIMARY KEY,
                name        text,
                msg         text, 
                levelname   text, 
                asctime     text, 
                relativeCreated float,
                thread      int,
                threadName  text, 
                funcName    text, 
                filename    text 
            ); 
        """