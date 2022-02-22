#import RPi.GPIO as GPIO
from flask import Flask, render_template, Response, request, url_for
import sys
import time

app = Flask(__name__)

# GPIO Board Numbers
lock1, lock2, lock3, lock4 = (12, 16, 18, 22)

# Lock Control
def lock_box( ):
    global lock1, lock2, lock3, lock4
    GPIO.setmode(GPIO.BOARD)
    locks = (lock1, lock2, lock3, lock4)
    GPIO.setup(locks, GPIO.OUT)
    GPIO.output(locks, GPIO.LOW)

def unlock_step1():
    global lock1
    GPIO.output((lock1), GPIO.HIGH)

def unlock_step2():
    global lock2
    GPIO.output((lock2), GPIO.HIGH)

def unlock_step3():
    global lock3
    GPIO.output((lock3), GPIO.HIGH)
    
def unlock_step4():
    global lock4
    GPIO.output((lock4), GPIO.HIGH)
    


#-------------------------------------------------#
# Home Page
#-------------------------------------------------#
@app.route('/')
def home():
    """Hello World"""
    return render_template('home.html')

#-------------------------------------------------#
# Objective 1 Keypad
#-------------------------------------------------#
@app.route('/lock1/')
def keypad():
    """Keypad Brute Forcing Lesson"""
    return render_template('keypad.html')

    
#-------------------------------------------------#
# Unlock Step 1
#-------------------------------------------------#
@app.route('/unlock/', methods=['POST'])
def unlock1():
    content = request.json
    print(content)
    if content['pop'] == "9517":
        #unlock_step1()###############################################################
        return "Success", 200
    
    return "Unsuccessful", 404
    

    
#-------------------------------------------------#
# Objective 2 Coding
#-------------------------------------------------#
@app.route('/lock2/')
def coding():
    """Coding Lesson"""
    return render_template('coding.html')




if __name__=='__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')

