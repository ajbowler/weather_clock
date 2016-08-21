# Weather Clock
A small project to create a weather clock from a raspberry pi and an LED matrix.

## Required materials
1. Raspberry Pi (tested on 2 B+ and 3)
2. Adafruit LED matrix and HAT kit, all assembled as shown in [Adafruit's guide](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi)

## Instructions
1. Get your Wunderground API key [here](https://www.wunderground.com/weather/api/d/docs). This is how the current weather for your area is obtained. The free version should be fine.
2. In `config`, replace `your_key_here` and `your_zip_code_here` with the key you obtained in step 1 and your zip code.
3. `python weather.py`
