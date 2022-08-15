#Calls set_imu_config to disable the gyroscope and accelerometer then gets the direction of North from the magnetometer in degrees.

#Returned type: Float
#Explanation: The direction of North.

from sense_hat import SenseHat

sense = SenseHat()
north = sense.get_compass()
print("North: %s" % north)

# alternatives
print(sense.compass)