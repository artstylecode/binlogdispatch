from .binlogdispatch import  BinlogDispatch
from .events import Event
from . import events
from .eventimpl import EventImpl

class SampleEventHandle(EventImpl):
    def insertHandle(self, event:Event):
        print(event.debugstring())
    def updateHandle(self, event:Event):
        return super().updateHandle(event)
    def deleteHandle(self, event:Event):
        return super().deleteHandle(event)
def main():
    dispatch = BinlogDispatch("127.0.0.1", 11111)
    ##dispatch.addEventListener(events.INSERT_EVENT, insertHandle)
    dispatch.addEventListener(handle = SampleEventHandle())
    dispatch.Start()
if __name__=="__main__":
    main()