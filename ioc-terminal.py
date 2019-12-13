import random
import smbus
import time
import RPi.GPIO as GPIO

motion_gpio = 23
noise_gpio = 24
gas_gpio = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(motion_gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(noise_gpio, GPIO.IN)
GPIO.setup(gas_gpio, GPIO.IN)

addr = 0x23
bus = smbus.SMBus(1)

def get_data():
    data = bus.read_i2c_block_data(addr, 0x23)
    result = (data[1] + (256*data[0]))/1.2
    formatedLightDataResult = format(result, '.2f')
    motion_data = GPIO.input(motion_gpio)
    noise_data = GPIO.input(noise_gpio)
    gas_data = GPIO.input(gas_gpio)

    print('Motion sensor data: ' + str(motion_data))
    print('Noise sensor data: ' + str(noise_data))
    print('Gas sensor data: ' + str(gas_data))
    print('Light sensor data: ' + str(formatedLightDataResult) + ' lux')
    

while True:
    get_data()
    time.sleep(1)
    
