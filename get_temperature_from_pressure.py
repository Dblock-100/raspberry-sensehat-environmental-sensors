from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature_from_pressure()
print("Temperature: %s C" % temp)

###C to F###
celsius = sense.get_temperature_from_pressure()
fahrenheit = (celsius * 9/5) + 32
print('%0.2f°F-%.2f°C' %(fahrenheit, celsius))