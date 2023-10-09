from vex import * 
class GsController(Controller):
    def __init__(self, *args):
        super().__init__(*args)
    def subscribe_to_event(self,event,result):
        event(result)
        return True







