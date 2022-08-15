#Returned type: Dictionary
#Explanation: A dictionary object indexed by the strings x, y and z. The values are Floats representing the rotational intensity of the axis in radians per second.

from sense_hat import SenseHat

sense = SenseHat()
raw = sense.get_gyroscope_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))

# alternatives
print(sense.gyro_raw)
print(sense.gyroscope_raw)