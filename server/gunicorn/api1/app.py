from flask import Flask, render_template, request
#from flask_restful import Resource, Api
from markupsafe import escape

from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, static_url_path='')
auth = HTTPBasicAuth()

#api = Api(app)

import eventlet
import json
from flask_mqtt import Mqtt

from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

import configparser
config = configparser.ConfigParser()
config.sections()
config.read('app.ini')

eventlet.monkey_patch()

app.config['SECRET'] = config['app']['SECRET']
app.config['TEMPLATES_AUTO_RELOAD'] = config['app']['SECRET']
app.config['MQTT_BROKER_URL'] = config['app']['MQTT_BROKER_URL']
app.config['MQTT_USERNAME'] = config['app']['MQTT_USERNAME']
app.config['MQTT_PASSWORD'] = config['app']['MQTT_PASSWORD']
app.config['MQTT_KEEPALIVE'] = int(config['app']['MQTT_KEEPALIVE'])
app.config['MQTT_CLEAN_SESSION'] = config['app']['MQTT_CLEAN_SESSION']

# Parameters for SSL enabled
app.config['MQTT_BROKER_PORT'] = int(config['app']['MQTT_BROKER_PORT'])
app.config['MQTT_TLS_ENABLED'] = config['app']['MQTT_TLS_ENABLED']
app.config['MQTT_TLS_INSECURE'] = config['app']['MQTT_TLS_INSECURE']
app.config['MQTT_TLS_CA_CERTS'] = config['app']['MQTT_TLS_CA_CERTS']

users = {
    "webuser": generate_password_hash("w3Bus3R")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

mqtt = Mqtt(app)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    mqtt.subscribe('home/light/status')
    
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    current_state = data.payload

@app.route('/lighton')
@auth.login_required
def lighton():
    mqtt.publish('home/light/command', '1')
    return 'light on'

@app.route('/lightoff')
def lightoff():
    mqtt.publish('home/light/command', '0') 
    return 'light off'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#api.add_resource(HelloWorld, '/')
@app.route('/index')
def index():
    return app.send_static_file('index.html')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do the login'
    else:
        return 'show the form'

if __name__ == '__main__':
    #app.run(debug=True)
    socketio.run(app)#, host='0.0.0.0', port=5000, use_reloader=False, debug=False)
