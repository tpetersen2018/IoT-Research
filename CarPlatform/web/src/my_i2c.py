import time
from smbus2 import SMBus

I2C_ADDRESS = 0x18
I2C_COMMAND = 0xFF

# Motor
I2C_STOP = 0x210A
I2C_FORWARD = 0x220A
I2C_BACKWARD = 0x230A
I2C_LEFT = 0x240A
I2C_RIGHT = 0x250A


# TODO - Create an I2C_Bus class which inherits from SMBus


# Functions
def make_bus():
	bus = SMBus(1)
	return bus

def turn_right(i2c_bus):
	i2c_bus.write_word_data(I2C_ADDRESS, I2C_COMMAND, I2C_RIGHT)

def turn_left(i2c_bus):
	i2c_bus.write_word_data(I2C_ADDRESS, I2C_COMMAND, I2C_LEFT)

def forward(i2c_bus):
        i2c_bus.write_word_data(I2C_ADDRESS, I2C_COMMAND, I2C_FORWARD)

def backward(i2c_bus):
        i2c_bus.write_word_data(I2C_ADDRESS, I2C_COMMAND, I2C_BACKWARD)

def stop(i2c_bus):
        i2c_bus.write_word_data(I2C_ADDRESS, I2C_COMMAND, I2C_STOP)


