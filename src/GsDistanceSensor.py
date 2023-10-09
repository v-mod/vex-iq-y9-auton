from vex import *
class GsDistanceSensor(Distance):
    def __init__(self, port):
        super().__init__(port)
        