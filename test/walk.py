import cozmo
from cozmo.util import distance_mm, speed_mmps,degrees

def cozmo_program(robot: cozmo.robot.Robot):
    robot.drive_straight(distance_mm(150),speed_mmps(100)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(150),speed_mmps(100)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(150),speed_mmps(100)).wait_for_completed()
    robot.turn_in_place(degrees(90)).wait_for_completed()
    robot.drive_straight(distance_mm(150),speed_mmps(100)).wait_for_completed()

cozmo.run_program(cozmo_program)
