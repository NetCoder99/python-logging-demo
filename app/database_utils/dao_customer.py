import sqlite3

from  models.customer import customer_record

class dao_customer_functions():
    database:str = None

    __instance = None
    def __new__(cls, *args):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

    def __init__(self):
        super().__init__() # for python 3.X
        self.database = 'customers_data.db'
        self.table = 'customers'
        create_table_sql = dao_customer_functions.getCustomerTableDefinition()
        conn = sqlite3.connect(self.database)
        conn.execute(create_table_sql)
        conn.commit()
        conn.close()

    def insertNewCustomer(self, customer_record: customer_record):
        insert_sqlstr = dao_customer_functions.getCustomerInsertString(customer_record)
        conn = sqlite3.connect(self.database)
        curr = conn.cursor()
        curr.execute(insert_sqlstr)
        #print(customer_record)
        customer_record.customer_id = curr.lastrowid
        conn.commit()
        conn.close()
        

    @staticmethod
    def getCustomerInsertString(customer_record: customer_record):
        return '''
            INSERT INTO customers
            (customer_id, first_name, last_name, address_line_1, address_line_2, address_city, address_state, address_zipcode, create_date)
            VALUES(null, '{}', '{}', '{}', '{}', '{}', '{}', '{}', CURRENT_TIMESTAMP);
        '''.format(
               customer_record.first_name,
               customer_record.last_name,
               customer_record.address_line_1,
               customer_record.address_line_2,
               customer_record.address_city,
               customer_record.address_state,
               customer_record.address_zipcode
            )


    @staticmethod
    def getCustomerTableDefinition():
        return """
            CREATE TABLE IF NOT EXISTS customers (
                customer_id     integer  PRIMARY KEY,
                first_name      text,
                last_name       text,
                address_line_1  text,
                address_line_2  text,    
                address_city    text,
                address_state   text,
                address_zipcode text,
                create_date     date    DATETIME NOT NULL DEFAULT (CURRENT_TIMESTAMP) 
            ); 
        """