import wiringpi as GPIO
from flask import Flask, render_template, Response, request, url_for
import sys
from signal import *
import time

app = Flask(__name__, static_url_path="", static_folder="templates")
app.config.from_pyfile('config.py')

# Define the pins
ENA = 22
ENB = 30
IN1 = 26
IN3 = 21

# Termination signal handler - makes sure motor is turned off
def clean(*args):
    print('Cleaning up GPIO')
#    GPIO.softPwmWrite(ENA, 0)
#    GPIO.softPwmWrite(ENB, 0)
    GPIO.digitalWrite(ENA, 0)
    GPIO.digitalWrite(ENB, 0)
    GPIO.digitalWrite(IN1, 0)
    GPIO.digitalWrite(IN3, 0)
    sys.exit(0)

for sig in (SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM, SIGQUIT, SIGTSTP):
    signal(sig, clean)


def initialize_gpio():
    # Call setup function
    GPIO.wiringPiSetup()
    # Initialize pins as outputs
    print(ENA, ENB, IN1, IN3)
    print('22, 30, 26, 21')
    GPIO.pinMode(ENA, GPIO.OUTPUT)
    GPIO.pinMode(ENB, GPIO.OUTPUT)
    GPIO.pinMode(IN1, GPIO.OUTPUT)
    GPIO.pinMode(IN3, GPIO.OUTPUT)
    # Create PWM signals
   # GPIO.softPwmCreate(ENA, 0, 100)
   # GPIO.softPwmCreate(ENB, 0, 100)

# Turn on PWM
def turn_on(duty=99):
    print('Duty cycle is', duty)
    #GPIO.softPwmWrite(ENA, duty)
    #GPIO.softPwmWrite(ENB, duty)
    GPIO.digitalWrite(ENA, GPIO.HIGH)
    GPIO.digitalWrite(ENB, GPIO.HIGH)

# Begin defining directions
def backward():
    # Set gates
    GPIO.digitalWrite(IN1, GPIO.LOW)
    GPIO.digitalWrite(IN3, GPIO.HIGH)
    # set pwm signals
    turn_on()

def forward():
    GPIO.digitalWrite(IN1, GPIO.HIGH)
    GPIO.digitalWrite(IN3, GPIO.LOW)
    turn_on()

def left():
    GPIO.digitalWrite(IN1, GPIO.HIGH)
    GPIO.digitalWrite(IN3, GPIO.HIGH)
    turn_on()

def right():
    GPIO.digitalWrite(IN1, GPIO.LOW)
    GPIO.digitalWrite(IN3, GPIO.LOW)
    turn_on()

def stop():
    # Turn off PWM signals
    #GPIO.softPwmWrite(ENA, 0)
    #GPIO.softPwmWrite(ENB, 0)
    GPIO.digitalWrite(ENA, GPIO.LOW)
    GPIO.digitalWrite(ENB, GPIO.LOW)
    
#-------------------------------------------------#
# Objective 1 Replay
#-------------------------------------------------#
@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/movement/', methods=['POST'])
def move_input():
    content = request.json
    
    if content['zoom'] == "forward":
        forward()
        print("User requested forward movement...")
        return "Forward movement request successful!"
        
    elif content['zoom'] == "left":
        left()
        print("User requested left movement...")
        return "Left movement request successful!"
        
    elif content['zoom'] == "right":
        right()
        print("User requested right movement...")
        return "Right movement request successful!"
        
    elif content['zoom'] == "backward":
        backward()
        print("User requested backward movement...")
        return "Backward movement request successful!"
        
    elif content['zoom'] == "stop":
        stop()
        print("User requested to stop movement...")
        return "Stopping movement!"
    
    else:    
        return "Bad movement request!"

#-------------------------------------------------#
# Objective 2 Cookie
#-------------------------------------------------#

@app.route('/cookie/')
def cookie():
    return render_template('cookie.html')

#-------------------------------------------------#
# Objective 3 ....
#-------------------------------------------------#
       
if __name__ == '__main__':
    initialize_gpio()
    app.run(debug=True, port=80, host='0.0.0.0')
    clean()
