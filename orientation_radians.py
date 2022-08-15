#Gets the current orientation in radians using the aircraft principal axes of pitch, roll and yaw.
#Returned type: Dictionary
#Explanation: A dictionary object indexed by the strings pitch, roll and yaw. The values are Floats representing the angle of the axis in radians.

from sense_hat import SenseHat

sense = SenseHat()
orientation_rad = sense.get_orientation_radians()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_rad))

# alternatives
print(sense.orientation_radians)