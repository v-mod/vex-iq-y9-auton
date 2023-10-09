from vex import *
UNSPECIFIED_VELOCITY = 150
class GsSmartDrive(SmartDrive):
    def __init__(self, lm, rm, g, driveVelocity: vexnumber, turnVelocity: vexnumber, stopType: BrakeType.BrakeType, wheelTravel: vexnumber = 300, trackWidth: vexnumber = 320, wheelBase: vexnumber = 320, units=DistanceUnits.MM, externalGearRatio=1):
        super().__init__(lm, rm, g, wheelTravel, trackWidth, wheelBase, units, externalGearRatio)
        self.driveVelocity=driveVelocity
        self.turnVelocity=turnVelocity
        self.set_stopping(stopType)
    def GenDrive(self,velocity=UNSPECIFIED_VELOCITY,angle=0):
        if velocity == UNSPECIFIED_VELOCITY and angle == 0:
            velocity=self.driveVelocity
        elif velocity == UNSPECIFIED_VELOCITY and angle != 0:
            velocity=self.turnVelocity
        else:
            velocity=velocity
        self.set_drive_velocity(velocity)
        self.set_turn_velocity(velocity)
        if angle == 0:
            self.drive(FORWARD)
            return True
        else:
            self.turn_to_rotation(angle)
            return True
    