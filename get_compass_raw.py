#Gets the raw x, y and z axis magnetometer data.

# Returned type: Dictionary
#Explanation A dictionary object indexed by the strings x, y and z. The values are Floats representing the magnetic intensity of the axis in microteslas (µT).

from sense_hat import SenseHat

sense = SenseHat()
raw = sense.get_compass_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))

# alternatives
print(sense.compass_raw)