import json

class customer_record:
    customer_id: int      = None
    first_name: str       = None
    last_name: str        = None
    address_line_1: str   = None
    address_line_2: str   = None      
    address_city:str      = None
    address_state:str     = None
    address_zipcode:str   = None

    def __init__(self, customer_id: int = None,
                       first_name: str = None,
                       last_name: str = None,
                       address_line_1: str = None,
                       address_line_2: str = None,
                       address_city:str = None,
                       address_state:str = None,
                       address_zipcode:str = None):
        self.customer_id: int      = customer_id
        self.first_name: str       = first_name
        self.last_name: str        = last_name
        self.address_line_1: str   = address_line_1
        self.address_line_2: str   = address_line_2      
        self.address_city:str      = address_city
        self.address_state:str     = address_state
        self.address_zipcode:str   = address_zipcode
    
    @classmethod
    def fromJson(cls, json_str):
        return cls (
            first_name       = json_str['first_name'],
            last_name        = json_str['last_name'],
            address_line_1   = json_str['address_line_1'],
            address_line_2   = json_str['address_line_2'],     
            address_city     = json_str['address_city'],
            address_state    = json_str['address_state'],
            address_zipcode  = json_str['address_zipcode']
        )

    def setFirstName(self, first_name: str):
        self.first_name = first_name
        return self

    def setLastName(self, last_name: str):
        self.last_name = last_name
        return self

    def toCsv(self):
        return '"{}","{}","{}","{}","{}","{}","{}","{}"'.format(
        self.customer_id,
        self.first_name,
        self.last_name,
        self.address_line_1,
        self.address_line_2,
        self.address_city,
        self.address_state,
        self.address_zipcode)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=2)

    def toJsonDb(self):
        return "'{" + '"' + self.__class__.__name__ + '":' + \
                 json.dumps(self, default=lambda o: o.__dict__, indent=2).replace("'", '"') + "}'" 