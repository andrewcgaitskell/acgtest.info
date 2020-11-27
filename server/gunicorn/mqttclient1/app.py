import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

import eventlet
import json
from flask import Flask, render_template
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap

import configparser
config = configparser.ConfigParser()
config.sections()
config.read('app.ini')

eventlet.monkey_patch()

app = Flask(__name__)
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

mqtt = Mqtt(app)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('publish')
def handle_publish(json_str):
    data = json.loads(json_str)
    mqtt.publish(data['topic'], data['message'])


@socketio.on('subscribe')
def handle_subscribe(json_str):
    data = json.loads(json_str)
    mqtt.subscribe(data['topic'])


@socketio.on('unsubscribe_all')
def handle_unsubscribe_all():
    mqtt.unsubscribe_all()


@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    socketio.emit('mqtt_message', data=data)
    ##f = open("/tmp/output.jpg", "w")  #there is a output.jpg which is different
    ##f.write(message.payload)
    ##f.close()

@mqtt.on_log()
def handle_logging(client, userdata, level, buf):
    print(level, buf)


if __name__ == '__main__':
    # important: Do not use reloader because this will create two Flask instances.
    # Flask-MQTT only supports running with one instance
    socketio.run(app,port=5005,use_reloader=False, debug=False)
