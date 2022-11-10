
import random

def get_temperature_pressure_humidity():
    return (random.randint(0, 40),random.randint(9, 60),random.randint(0, 3))
def moisture_sensor():
    return (random.randint(0, 40))
def vanne_on():
    print('vanne on')

def vanne_off():
    print('vanne off')