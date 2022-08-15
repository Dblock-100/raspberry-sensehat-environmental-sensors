from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature()

#alternatives
#print(sense.temp)
#print(sense.temperature)

###C to F###
celsius = sense.get_temperature()
fahrenheit = (celsius * 9/5) + 32
print('%0.2f°F-%.2f°C' %(fahrenheit, celsius)) 