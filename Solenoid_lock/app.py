#import RPi.GPIO as GPIO
from flask import Flask, render_template, Response, request, url_for, make_response, redirect
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

def lock_box():
    global lock1, lock2, lock3, lock4
    GPIO.output((lock1), GPIO.LOW)
    GPIO.output((lock2), GPIO.LOW)
    GPIO.output((lock3), GPIO.LOW)
    GPIO.output((lock4), GPIO.LOW)


#-------------------------------------------------#
# Home Page
#-------------------------------------------------#
@app.route('/')
def home():
    """Hello World"""
    return render_template('home.html')

#-------------------------------------------------#
# Admin Page
#-------------------------------------------------#
@app.route('/admin')
def admin():
    """Admin usage"""
    #lock_box() #######################################################################
    return render_template('admin.html')

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
@app.route('/unlock1', methods=['POST'])
def unlock1():
    content = request.json
    
    if content['pop'] == "9517":
        #unlock_step1()###############################################################
        return "Success", 200
    
    return "Unsuccessful", 404
    
    
#-------------------------------------------------#
# Objective 2 Coding
#-------------------------------------------------#
@app.route('/lock2/')
def task2():
    """Coding Lesson"""
    return render_template('coding.html')


#-------------------------------------------------#
# Unlock Step 2
#-------------------------------------------------#
@app.route('/unlock2', methods=['POST'])
def unlock2():
    content = request.json
    
    if content['pop'] == "9517":
        #unlock_step2()###############################################################
        return "Success", 200
    
    return "Unsuccessful", 404


#-------------------------------------------------#
# Objective 3 Cookie
#-------------------------------------------------#
@app.route('/lock3/')
def task4():
    """Cookie Lesson"""
    return render_template('cookie.html')


#-------------------------------------------------#
# Setting Cookie
#-------------------------------------------------#
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    """Unlocked Deserves a Flag"""
    if request.method == 'POST':
        user = request.form['nm']
        
        response = make_response(render_template('readcookie.html'))
      
        try:
        	name = request.cookies.get('userID')
        	response.set_cookie('userID', name)
        except:
        	response.set_cookie('userID', user)
        
        return response


#-------------------------------------------------#
# Getting Cookie
#-------------------------------------------------#
@app.route('/getcookie')
def getcookie():
    """Unlocked Deserves a Flag"""
    
    name = request.cookies.get('userID')
    
    if name == 'admin':
    	#unlock_step3()#############################################################
        return render_template('unlock.html')
    else:
        return render_template('cookie2.html')


if __name__=='__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')

