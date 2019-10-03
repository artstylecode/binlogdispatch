import time, types

from canal.client import Client
from canal.protocol import EntryProtocol_pb2
from canal.protocol import CanalProtocol_pb2
from .events import Event
from . import events
from .eventimpl import EventImpl
from .dispatch import Dispatch

class BinlogDispatch(Dispatch):
    client = None
    def __init__(self, host, port):
        self.client = Client()
        self.client.connect(host=host, port=port)
        self.client.check_valid(username=b'', password=b'')
        self.client.subscribe(client_id=b'1001', destination=b'example', filter=b'.*\\..*')
    def Start(self):
        while True:
            message = self.client.get(100)
            entries = message['entries']
            for entry in entries:
                entry_type = entry.entryType
                if entry_type in [EntryProtocol_pb2.EntryType.TRANSACTIONBEGIN, EntryProtocol_pb2.EntryType.TRANSACTIONEND]:
                    continue
                row_change = EntryProtocol_pb2.RowChange()
                row_change.MergeFromString(entry.storeValue)
                event_type = row_change.eventType
                header = entry.header
                database = header.schemaName
                table = header.tableName
                event_type = header.eventType
                for row in row_change.rowDatas:
                    format_data = dict()
                    if event_type == EntryProtocol_pb2.EventType.DELETE:
                        for column in row.beforeColumns:
                            format_data[column.name] = column.value
                        #派遣事件
                        event = Event(format_data, table, database)
                        self.dispatch(events.DELETE_EVENT, event)
                    elif event_type == EntryProtocol_pb2.EventType.INSERT:
                        for column in row.afterColumns:
                            format_data[column.name] = column.value
                        event = Event(format_data, table, database)
                        self.dispatch(events.INSERT_EVENT, event)
                    elif event_type == EntryProtocol_pb2.EventType.UPDATE:
                         for column in row.afterColumns:
                            format_data[column.name] = column.value
                         event = Event(format_data, table, database)
                         self.dispatch(events.UPDATE_EVENT, event)
                    else:
                        format_data['before'] = format_data['after'] = dict()
                        for column in row.beforeColumns:
                            format_data['before'][column.name] = column.value
                        for column in row.afterColumns:
                            format_data['after'][column.name] = column.value
                    data = dict(
                        db=database,
                        table=table,
                        event_type=event_type,
                        data=format_data,
                    )
            time.sleep(1)

        self.client.disconnect()
