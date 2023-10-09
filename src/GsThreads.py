from vex import * 
drivetrain_l_needs_to_be_stopped_controller = False
drivetrain_r_needs_to_be_stopped_controller = False
remote_control_code_enabled = True
class GsThreads:
    def __init__(self,left_drive_smart,right_drive_smart,drivetrain,controller):
        self.left_drive_smart=left_drive_smart
        self.right_drive_smart=right_drive_smart
        self.controller=controller
        self.drivetrain=drivetrain
    # define a task that will handle monitoring inputs from controller
    def rc_auto_loop(self):
        global drivetrain_l_needs_to_be_stopped_controller, drivetrain_r_needs_to_be_stopped_controller, remote_control_code_enabled
        # process the controller input every 20 milliseconds
        # update the motors based on the input values
        while True:
            if remote_control_code_enabled:
                
                # calculate the drivetrain motor velocities from the controller joystick axies
                # left = axisA
                # right = axisD
                drivetrain_left_side_speed = self.controller.axisA.position()
                drivetrain_right_side_speed = self.controller.axisD.position()
                
                # check if the value is inside of the deadband range
                if drivetrain_left_side_speed < 5 and drivetrain_left_side_speed > -5:
                    # check if the left motor has already been stopped
                    if drivetrain_l_needs_to_be_stopped_controller:
                        # stop the left drive motor
                        self.left_drive_smart.stop()
                        # tell the code that the left motor has been stopped
                        drivetrain_l_needs_to_be_stopped_controller = False
                else:
                    # reset the toggle so that the deadband code knows to stop the left motor next
                    # time the input is in the deadband range
                    drivetrain_l_needs_to_be_stopped_controller = True
                # check if the value is inside of the deadband range
                if drivetrain_right_side_speed < 5 and drivetrain_right_side_speed > -5:
                    # check if the right motor has already been stopped
                    if drivetrain_r_needs_to_be_stopped_controller:
                        # stop the right drive motor
                        self.right_drive_smart.stop()
                        # tell the code that the right motor has been stopped
                        drivetrain_r_needs_to_be_stopped_controller = False
                else:
                    # reset the toggle so that the deadband code knows to stop the right motor next
                    # time the input is in the deadband range
                    drivetrain_r_needs_to_be_stopped_controller = True
                
                # only tell the left drive motor to spin if the values are not in the deadband range
                if drivetrain_l_needs_to_be_stopped_controller:
                    self.left_drive_smart.set_velocity(drivetrain_left_side_speed, PERCENT)
                    self.left_drive_smart.spin(FORWARD)
                # only tell the right drive motor to spin if the values are not in the deadband range
                if drivetrain_r_needs_to_be_stopped_controller:
                    self.right_drive_smart.set_velocity(drivetrain_right_side_speed, PERCENT)
                    self.right_drive_smart.spin(FORWARD)
            # wait before repeating the process
            wait(20, MSEC)