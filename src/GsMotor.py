from vex import *
class GsMotor(Motor):
    def __init__(self, port: int, *args):
        super().__init__(port, *args)
        