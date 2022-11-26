import json
import logging
import inspect

from   pathlib import Path
from   models.customer import customer_record
from   database_utils.dao_customer import dao_customer_functions

logger = logging.getLogger("app_logger")
dao_customer_functions = dao_customer_functions()

def createNewCustomerFromJson():
    function_name = inspect.stack()[0][3]
    logger.info  ("--- {}".format(function_name))

    base_path = Path(__file__).parent
    file_path = (base_path / "../data/customer001.json").resolve()
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        
    customer_rec = customer_record.fromJson(data)
    #print('customer_rec: {}'.format(customer_rec.toJson()))
    dao_customer_functions.insertNewCustomer(customer_rec)

    print(customer_rec.toJsonDb())

    logger.info("New customer id: {}".format(customer_rec.customer_id))
