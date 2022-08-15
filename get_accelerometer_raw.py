#Gets the raw x, y and z axis accelerometer dat
#Returned type: Dictionary
#Explanation: A dictionary object indexed by the strings x, y and z. The values are Floats representing the acceleration intensity of the axis in Gs.

from sense_hat import SenseHat

sense = SenseHat()
raw = sense.get_accelerometer_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))

# alternatives
print(sense.accel_raw)
print(sense.accelerometer_raw)