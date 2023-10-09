from vex import *
class GsBrain(Brain):
    def __init__(self, *args):
        super().__init__(*args)
    def subscribe_to_event(self,event,result):
        event(result)
        return True
    def write_to_file(self,fileobject,data):
        fileobject.write(data)
        return fileobject.close()
    def read_file(self,fileobject):
        return fileobject.read()
    def create_file_object(self,file,mode):
        return open(file,mode)
