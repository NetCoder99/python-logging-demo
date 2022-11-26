import json


class dbLogRecord:
    name: str       = None
    msg: str        = None
    levelname: str  = None
    asctime: str    = None      
    relativeCreated:float = None
    thread:int      = None
    threadName:str  = None
    funcName:str    = None
    filename:str    = None

    def __init__(self, record):
        self.name      = record.name
        self.msg       = record.msg
        self.levelname = record.levelname
        self.asctime   = record.asctime
        self.relativeCreated = record.relativeCreated
        self.thread     = record.thread
        self.threadName = record.threadName
        self.funcName   = record.funcName
        self.filename   = record.filename

    def toString(self):
        return '{}:{}:{}:{}:{}:{}:{}:{}:{}\n'.format(
            self.name, 
            self.msg, 
            self.levelname, 
            self.asctime, 
            self.relativeCreated, 
            self.thread, 
            self.threadName,
            self.funcName,
            self.filename
        )

    def toCsv(self):
        print('\nself.msg:{}\n\n'.format(self.msg))
        try:
            json.loads(self.msg)
        except ValueError as err:
            return self.msgAsString()
        return self.msgAsJson()

        # return '"{}","{}","{}","{}","{}","{}","{}","{}","{}"'.format(
        #     self.name, 
        #     self.msg, 
        #     self.levelname, 
        #     self.asctime, 
        #     self.relativeCreated, 
        #     self.thread, 
        #     self.threadName,
        #     self.funcName,
        #     self.filename
        # )

    def msgAsJson(self):
        return "'{}",'{}',"{}","{}","{}","{}","{}","{}","{}'".format(
            self.name, 
            self.msg, 
            self.levelname, 
            self.asctime, 
            self.relativeCreated, 
            self.thread, 
            self.threadName,
            self.funcName,
            self.filename
        )

    def msgAsString(self):
        return '"{}","{}","{}","{}","{}","{}","{}","{}","{}"'.format(
            self.name, 
            self.msg, 
            self.levelname, 
            self.asctime, 
            self.relativeCreated, 
            self.thread, 
            self.threadName,
            self.funcName,
            self.filename
        )
