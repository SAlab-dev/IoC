#!/usr/bin/env python
import random
import smbus
import time
import blynklib

BLYNK_AUTH = 'K77DebNuafyHDCHZM9qput2XGzWQvaiO'
blynk = blynklib.Blynk(BLYNK_AUTH)



addr = 0x23
bus = smbus.SMBus(1)


@blynk.handle_event('read V11')
def read_virt_pin(pin):
    data = bus.read_i2c_block_data(addr, 0x23)
    result = (data[1] + (256*data[0]))/1.2
    formatedResult = format(result, '.2f')
    
    blynk.virtual_write(pin, formatedResult)

while True:
    blynk.run()
