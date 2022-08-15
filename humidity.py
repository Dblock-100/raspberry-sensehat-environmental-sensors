from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()
#print("Humidity: %s %%rH" % humidity)

# alternatives
print("Humidity:",round(humidity,2))
 