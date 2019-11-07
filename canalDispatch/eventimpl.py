from .events import Event
## EventImpl 事件接口
class EventImpl():
    ## 插入事件处理方法
    def insertHandle(self, event:Event):
        print("event message : {}".format(event.debugstring()))
        raise NotImplementedError('method not implements')
    ## 更新事件处理方法
    def updateHandle(self, event:Event):
        print("event message : {}".format(event.debugstring()))
        raise NotImplementedError
    ## 删除事件处理方法
    def deleteHandle(self, event:Event):
        raise NotImplementedError