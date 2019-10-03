from google.protobuf.internal import enum_type_wrapper

INSERT_EVENT="insert"
UPDATE_EVENT="update"
DELETE_EVENT="delete"



class Event():
    data = {}
    table = ""
    db  = ""
    def __init__(self, data, table, db):
        self.data = data
        self.table = table
        self.db = db
    def debugstring(self):
        print("event info:\n data:{}\n table:{}\n db:{}\n".format(self.data, self.table, self.db))
class InsertEvent(Event):
    def __init__(self, data, table, db):
        super().__init__(data, table, db)
class UpdateEvent(Event):
    def __init__(self, data, table, db):
        super().__init__(data, table, db)
