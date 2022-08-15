#Gets the current orientation in degrees using the aircraft principal axes of pitch, roll and yaw.

#Returned type: Dictionary
#Explanation: A dictionary object indexed by the strings pitch, roll and yaw. The values are Floats representing the angle of the axis in degrees.

from sense_hat import SenseHat

sense = SenseHat()
orientation = sense.get_orientation_degrees()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))