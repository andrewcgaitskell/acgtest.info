import paho.mqtt.client as mqtt

import time
from datetime import datetime
import json
import ssl

import configparser
config = configparser.ConfigParser()
config.sections()
config.read('app.ini')

import eventlet

eventlet.monkey_patch()

MQTT_BROKER_URL = config['app']['MQTT_BROKER_URL']
MQTT_USERNAME = config['app']['MQTT_USERNAME']
MQTT_PASSWORD = config['app']['MQTT_PASSWORD']

connected = False  # Stores the connection status
BROKER_ENDPOINT = MQTT_BROKER_URL
TLS_PORT = 8883  # Secure port
PUBLISH_TOPIC = "Pong"
SUBSCRIBE_TOPIC = "Ping"

TLS_CERT_PATH = config['app']['MQTT_TLS_CA_CERTS']

def on_message_msgs(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $SYS/broker/messages/#
    print("MESSAGES: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_message_bytes(mosq, obj, msg):
    # This callback will only be called for messages with topics that match
    # $SYS/broker/bytes/#
    print("BYTES: " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_message(mosq, obj, msg):
    # This callback will be called for messages that we receive that do not
    # match any patterns defined in topic specific callbacks, i.e. in this case
    # those messages that do not have topics $SYS/broker/messages/# nor
    # $SYS/broker/bytes/#
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    
    if msg.topic == "Ping":
        mqttc.publish("Pong", 0)
    
mqttc = mqtt.Client()

# Add message callbacks that will only trigger on a specific subscription match.
##mqttc.message_callback_add("$SYS/broker/messages/#", on_message_msgs)
##mqttc.message_callback_add("$SYS/broker/bytes/#", on_message_bytes)
mqttc.username_pw_set(MQTT_USERNAME, password=MQTT_PASSWORD)
mqttc.on_message = on_message
mqttc.tls_set(ca_certs=TLS_CERT_PATH, certfile=None,
                    keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                    tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqttc.tls_insecure_set(False)
mqttc.connect(BROKER_ENDPOINT, port=TLS_PORT)
mqttc.subscribe("$SYS/#", 0)
mqttc.subscribe("Ping", 0)

mqttc.loop_forever()
