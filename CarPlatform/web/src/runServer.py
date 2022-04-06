from flask import Flask, render_template, Response, request, url_for
import sys
from signal import *
import time
import my_i2c
import socket

app = Flask(__name__, static_url_path="", static_folder="templates")
app.config.from_pyfile('config.py')

# Make the I2C bus and drop the speed
ic2_bus = my_i2c.make_bus()
my_i2c.motor_slow(ic2_bus)

# Begin defining directions
def backward():
    my_i2c.backward(ic2_bus)

def forward():
    my_i2c.forward(ic2_bus)

def left():
    my_i2c.turn_left(ic2_bus)

def right():
    my_i2c.turn_right(ic2_bus)

def stop():
    my_i2c.stop(ic2_bus)

def broadcast(msg):
    b_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    b_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    b_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, b'wlan0\0')
    server_address = ('255.255.255.255', 2022)
    msg = "[Broadcast] " + msg
    b_msg = bytes(msg, 'ascii')
    b_sock.sendto(b_msg, server_address)

#-------------------------------------------------#
# Objective 1 Storage
#-------------------------------------------------#
@app.route('/')
def index():
    broadcast("New Client Connected")
    print("New client is now connecting")
    return render_template('index.html')

@app.route('/movement/', methods=['POST'])
def move_input():
    content = request.json

    if content['zoom'] == "forward":
        forward()
        print("User requested forward movement...")
        broadcast("Car is moving forward")
        return "Forward movement request successful!"

    elif content['zoom'] == "left":
        left()
        print("User requested left movement...")
        broadcast("Car is moving left")
        return "Left movement request successful!"

    elif content['zoom'] == "right":
        right()
        print("User requested right movement...")
        broadcast("Car is moving right")
        return "Right movement request successful!"

    elif content['zoom'] == "backward":
        backward()
        print("User requested backward movement...")
        broadcast("Car is moving back")
        return "Backward movement request successful!"

    elif content['zoom'] == "stop":
        stop()
        print("User requested to stop movement...")
        broadcast("Car is stopping")
        return "Stopping movement!"

    else:
        broadcast("Strange traffic is reaching the car!")
        return "Bad movement request!"

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
