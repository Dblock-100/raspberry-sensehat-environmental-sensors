#Calls set_imu_config to disable the magnetometer and accelerometer then gets the current orientation from the gyroscope only.

#Returned type: Dictionary
#Explanation: A dictionary object indexed by the strings pitch, roll and yaw. The values are Floats representing the angle of the axis in degrees.

from sense_hat import SenseHat

sense = SenseHat()
gyro_only = sense.get_gyroscope()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))

# alternatives
print(sense.gyro)
print(sense.gyroscope)