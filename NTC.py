from machine import ADC, Pin
import math
import time

BETA = 3950

adc = ADC(Pin(2))
adc.atten(ADC.ATTN_11DB)

def read_ntc_temperature():
    analog_value = adc.read()
    print(analog_value)
    temperature_celsius = 1 / (math.log(1 / (4096 / analog_value - 1)) / BETA + 1.0 / 298.15) - 273.15
    return temperature_celsius

while True:
    temperature = read_ntc_temperature()
    print("Temperature: {:.2f} ℃".format(temperature))
    time.sleep(1)
