from sense_hat import SenseHat
import time

sense = SenseHat()
humidity = sense.get_humidity()
#print("Humidity: %s %%rH" % humidity)

# alternatives
print("Humidity:",round(humidity,2))

##########Data to Sense Hat######

green = (0, 255, 0)
white = (255, 255, 255)
humidity = sense.humidity
humidity_value = 64 * humidity / 100
pixels = [green if i < humidity_value else white for i in range(64)]
sense.set_pixels(pixels)
time.sleep(5)

#####Data to turn off Sense LCD#####
off = (0, 0, 0)
humidity = 0
humidity_value = 64 * humidity / 100
pixels = [off if i < humidity_value else off for i in range(64)]
sense.set_pixels(pixels)

 
