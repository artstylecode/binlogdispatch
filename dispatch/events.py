from google.protobuf.internal import enum_type_wrapper

INSERT_EVENT="insert"
UPDATE_EVENT="update"
DELETE_EVENT="delete"

class Event():
    args = {}
    def __init__(self, args):
        self.args = args
class InsertEvent(Event):
    def __init__(self, args):
        super().__init__(args)
class UpdateEvent(Event):
    def __init__(self, args):
        super().__init__(args)
