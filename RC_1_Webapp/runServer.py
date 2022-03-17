from flask import Flask, render_template, Response, request, url_for
import sys
from signal import *
import time
import my_i2c

app = Flask(__name__, static_url_path="", static_folder="templates")
app.config.from_pyfile('config.py')

#ic2_bus = my_i2c.make_bus()


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
        #forward()
        print("User requested forward movement...")
        return "Forward movement request successful!"
        
    elif content['zoom'] == "left":
        #left()
        print("User requested left movement...")
        return "Left movement request successful!"

    elif content['zoom'] == "right":
        #right()
        print("User requested right movement...")
        return "Right movement request successful!"
        
    elif content['zoom'] == "backward":
        #backward()
        print("User requested backward movement...")
        return "Backward movement request successful!"
        
    elif content['zoom'] == "stop":
        #stop()
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
# Objective 3
#-------------------------------------------------#

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/movement/', methods=['POST'])
def sql_query():

@app.route('/inject/')
def inject():
    return render_template('inject.html')

#-------------------------------------------------#
# Objective 4
#-------------------------------------------------#
    
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
    clean()
