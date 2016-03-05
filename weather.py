import urllib2
import json
import Image
import ImageDraw
from rgbmatrix import Adafruit_RGBmatrix
from time import gmtime, strftime
import os

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
image_period = Image.open("Assets/Alphabet/period.jpg")

images = {
    'a': image_a,
    'b': image_b,
    'c': image_c,
    'd': image_d,
    'e': image_e,
    'f': image_f,
    'g': image_g,
    'h': image_h,
    'i': image_i,
    'j': image_j,
    'k': image_k,
    'l': image_l,
    'm': image_m,
    'n': image_n,
    'o': image_o,
    'p': image_p,
    'q': image_q,
    'r': image_r,
    's': image_s,
    't': image_t,
    'u': image_u,
    'v': image_v,
    'w': image_w,
    'x': image_x,
    'y': image_y,
    'z': image_z,
    '1': image_1,
    '2': image_2,
    '3': image_3,
    '4': image_4,
    '5': image_5,
    '6': image_6,
    '7': image_7,
    '8': image_8,
    '9': image_9,
    '0': image_0,
    '-': image_minus,
    ':': image_colon,
    '.': image_period
}

for key, value in images:
    value.load()

while True:
    if update_minute != minute:
        # if 5 minutes have passed, update the weather
        if new_minute >= 5:
            f = urllib2.urlopen(url)
            json_string = f.read()
            parsed_json = json.loads(json_string)
            weather = parsed_json['current_observation']['weather']
            temperature_string = parsed_json['current_observation']['temp_f']
            feelslike_string = parsed_json['current_observation']['feelslike_f']
            new_minute = 0
            f.close()
        else:
            new_minute += 1

        time = strftime("%I:%M")

        matrix.Clear()
        #display time
        count = 0
        for c in time:
            matrix.SetImage(images[c].im.id, count, 0)
            count += 5

        # display 'temp: '
        matrix.SetImage(image_t.im.id,0,6)
        matrix.SetImage(image_e.im.id,5,6)
        matrix.SetImage(image_m.im.id,10,6)
        matrix.SetImage(image_p.im.id,15,6)
        matrix.SetImage(image_colon.im.id,20,6)
        #display actual temperature
        count = 0
        for c in str(temperature_string):
            matrix.SetImage(images[c].im.id, count,12)
            count +=5

        print strftime("%I:%M")
        minute = strftime("%M")
        print weather.lower()
        print "Temp: " + str(temperature_string)
        print "Feels like	" + str(feelslike_string)

    update_minute = strftime("%M")





















