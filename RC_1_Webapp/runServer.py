#import RPi.GPIO as GPIO
from flask import Flask, render_template, Response, request, url_for
import sys
import time

app = Flask(__name__, static_url_path="", static_folder="templates")
app.config.from_pyfile('config.py')

in1, in2, ena, in3, in4, enb = (11, 12, 13, 15, 16, 18)
pwm_freq = 100
pwm_l = None
pwm_r = None
duty = 50


def initialize_gpio():
    global in1, in2, in3, in4, ena, enb, duty, pwm_l, pwm_r, pwm_freq
    GPIO.setmode(GPIO.BOARD)	# use board pin numbers
    gates = (in1, in2, in3, in4)
    # Initialize the IN gates to be output low
    GPIO.setup(gates, GPIO.OUT)
    GPIO.output(gates, GPIO.LOW)
    # Setup the PWM signals
    GPIO.setup((ena, enb), GPIO.OUT)
    pwm_l = GPIO.PWM(ena, pwm_freq)
    pwm_r = GPIO.PWM(enb, pwm_freq)
    pwm_l.start(duty)
    pwm_r.start(duty)

# Begin defining directions
def backward():
    global in1, in2, in3, in4, ena, enb, duty, pwm_l, pwm_r, pwm_freq
    # Set IN2 & IN4 low FIRST
    GPIO.output((in2, in4), GPIO.LOW)
    # Now set IN1 & IN3 high
    GPIO.output((in1, in3), GPIO.HIGH)

def forward():
    global in1, in2, in3, in4, ena, enb, duty, pwm_l, pwm_r, pwm_freq
    # Set IN1 & IN3 low
    GPIO.output((in1, in3), GPIO.LOW)
    # Now set IN2 & IN4 high
    GPIO.output((in2, in4), GPIO.HIGH)

def left():
    global in1, in2, in3, in4, ena, enb, duty, pwm_l, pwm_r, pwm_freq
    # Set IN1 & IN4 low first
    GPIO.output((in1, in4), GPIO.LOW)
    # Now set IN2 & IN3 high
    GPIO.output((in2, in3), GPIO.HIGH)

def right():
    global in1, in2, in3, in4, ena, enb, duty, pwm_l, pwm_r, pwm_freq
    # SET IN2 & IN3 low first
    GPIO.output((in2, in3), GPIO.LOW)
    # Now set IN1 & IN4 high
    GPIO.output((in1, in4), GPIO.HIGH)

def stop():
    global in1, in2, in3, in4, ena, enb, duty, pwm_l, pwm_r, pwm_freq
    # Set all inputs to low
    GPIO.output((in1, in2, in3, in4), GPIO.LOW)
    
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
#        forward()
        print("User requested forward movement...")
        return "Forward movement request successful!"
        
    elif content['zoom'] == "left":
#        left()
        print("User requested left movement...")
        return "Left movement request successful!"
        
    elif content['zoom'] == "right":
#        right()
        print("User requested right movement...")
        return "Right movement request successful!"
        
    elif content['zoom'] == "backward":
#        backward()
        print("User requested backward movement...")
        return "Backward movement request successful!"
        
    elif content['zoom'] == "stop":
#        stop()
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
#    GPIO.cleanup()
#    initialize_gpio()
    app.run(debug=True, port=80, host='0.0.0.0')