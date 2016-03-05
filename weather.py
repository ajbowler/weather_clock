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
image_a = Image.open("Assets/Alphabet/a.jpg")
image_b = Image.open("Assets/Alphabet/b.jpg")
image_c = Image.open("Assets/Alphabet/c.jpg")
image_d = Image.open("Assets/Alphabet/d.jpg")
image_e = Image.open("Assets/Alphabet/e.jpg")
image_f = Image.open("Assets/Alphabet/f.jpg")
image_g = Image.open("Assets/Alphabet/g.jpg")
image_h = Image.open("Assets/Alphabet/h.jpg")
image_i = Image.open("Assets/Alphabet/i.jpg")
image_j = Image.open("Assets/Alphabet/j.jpg")
image_k = Image.open("Assets/Alphabet/k.jpg")
image_l = Image.open("Assets/Alphabet/l.jpg")
image_m = Image.open("Assets/Alphabet/m.jpg")
image_n = Image.open("Assets/Alphabet/n.jpg")
image_o = Image.open("Assets/Alphabet/o.jpg")
image_p = Image.open("Assets/Alphabet/p.jpg")
image_q = Image.open("Assets/Alphabet/q.jpg")
image_r = Image.open("Assets/Alphabet/r.jpg")
image_s = Image.open("Assets/Alphabet/s.jpg")
image_t = Image.open("Assets/Alphabet/t.jpg")
image_u = Image.open("Assets/Alphabet/u.jpg")
image_v = Image.open("Assets/Alphabet/v.jpg")
image_w = Image.open("Assets/Alphabet/w.jpg")
image_x = Image.open("Assets/Alphabet/x.jpg")
image_y = Image.open("Assets/Alphabet/y.jpg")
image_z = Image.open("Assets/Alphabet/x.jpg")
image_1 = Image.open("Assets/Alphabet/1.jpg")
image_2 = Image.open("Assets/Alphabet/2.jpg")
image_3 = Image.open("Assets/Alphabet/3.jpg")
image_4 = Image.open("Assets/Alphabet/4.jpg")
image_5 = Image.open("Assets/Alphabet/5.jpg")
image_6 = Image.open("Assets/Alphabet/6.jpg")
image_7 = Image.open("Assets/Alphabet/7.jpg")
image_8 = Image.open("Assets/Alphabet/8.jpg")
image_9 = Image.open("Assets/Alphabet/9.jpg")
image_0 = Image.open("Assets/Alphabet/0.jpg")
image_minus = Image.open("Assets/Alphabet/minus.jpg")
image_colon = Image.open("Assets/Alphabet/colon.jpg")

image_a.load()
image_b.load()
image_c.load()
image_d.load()
image_e.load()
image_f.load()
image_g.load()
image_h.load()
image_i.load()
image_j.load()
image_k.load()
image_l.load()
image_m.load()
image_n.load()
image_o.load()
image_p.load()
image_q.load()
image_r.load()
image_s.load()
image_t.load()
image_u.load()
image_v.load()
image_w.load()
image_x.load()
image_y.load()
image_z.load()
image_1.load()
image_2.load()
image_3.load()
image_4.load()
image_5.load()
image_6.load()
image_7.load()
image_8.load()
image_9.load()
image_0.load()
image_minus.load()
image_colon.load()

while True:
    if update_minute != minute:
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
        else:
            new_minute += 1

        matrix.Clear()
        matrix.SetImage(image_t.im.id,0,0)
        matrix.SetImage(image_e.im.id,5,0)
        matrix.SetImage(image_m.im.id,10,0)
        matrix.SetImage(image_p.im.id,15,0)
        matrix.SetImage(image_colon.im.id,20,0)
        matrix.SetImage(image_3.im.id,0,6)
        matrix.SetImage(image_4.im.id,0,6)

        print strftime("%H:%M")
        minute = strftime("%M")
        print weather.lower()
        print "Temp: " + str(temperature_string)
        print "Feels like	" + str(feelslike_string)

    update_minute = strftime("%M")
