import types
from .eventimpl import EventImpl
from .events import Event
from .import events
class Dispatch():
    events = {}
    def addEventListener(self, handle:[types.FunctionType, EventImpl], event_name=""):
        if isinstance(handle, types.FunctionType):
            if not event_name in self.events.keys():
                self.events[event_name] = []
            self.events[event_name].append(handle)
        elif isinstance(handle, EventImpl):
             if not "instances" in self.events.keys():
                 self.events["instances"] = []
             self.events["instances"].append(handle)
    def dispatch(self, event_name, event:Event):
        if event_name in self.events.keys():
            for handle in self.events[event_name]:
                handle(event)
        elif "instances" in self.events.keys():
            for instance in self.events["instances"]:
                if isinstance(instance, EventImpl):
                    if event_name == events.INSERT_EVENT:
                        instance.insertHandle(event)
                    elif event_name == events.UPDATE_EVENT:
                        instance.updateHandle(event)
                    elif event_name == events.DELETE_EVENT:
                        instance.deleteHandle(event)