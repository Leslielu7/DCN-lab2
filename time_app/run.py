from flask import Flask
app = Flask(__name__)

import datetime

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def current_time():
    current_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    
    return current_time

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
