import urllib2
import json
import Image
import ImageDraw
from rgbmatrix import Adafruit_RGBmatrix
from time import gmtime, strftime

key = "14fb6128f6219c5f"
zip = "50011"
url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/PA/' + zip + '.json'
minute = strftime("%M")
new_minute = 5
update_minute = -1

matrix = Adafruit_RGBmatrix(32,1)
image = Imagenew("1", (32,32))
draw = ImageDraw.Draw(image)

while True:
    if new_minute >= 5:
        f = urllib2.urlopen(url)
	json_string = f.read()
	parsed_json = json.loads(json_string)
	city = parsed_json['location']['city']
	state = parsed_json['location']['state']
	weather = parsed_json['current_observation']['weather']
	temperature_string = parsed_json['current_observation']['temp_f']
	feelslike_string = parsed_json['current_observation']['feelslike_f']
	new_minute = 0
	f.close()

    if update_minute != minute:
        matrix.Clear()
        matrix.print(strftime("%H:%M"))
	print strftime("%H:%M")
	minute = strftime("%M")
	print weather.lower()
	print "Temp: " + str(temperature_string)
	print "Feels like	" + str(feelslike_string)
	new_minute += 1

    update_minute = strftime("%M")
