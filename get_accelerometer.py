#Calls set_imu_config to disable the magnetometer and gyroscope then gets the current orientation from the accelerometer only.
#Returned type: Dictionary
#Explanation: A dictionary object indexed by the strings pitch, roll and yaw. The values are Floats representing the angle of the axis in degrees.

from sense_hat import SenseHat

sense = SenseHat()
accel_only = sense.get_accelerometer()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))

# alternatives
print(sense.accel)
print(sense.accelerometer)