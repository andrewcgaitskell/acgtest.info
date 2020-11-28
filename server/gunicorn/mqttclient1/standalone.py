import paho.mqtt.client as mqttClient
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
PUBLISH_TOPIC = "TakeAPicture"
SUBSCRIBE_TOPIC = "PICTURE"

TLS_CERT_PATH = config['app']['MQTT_TLS_CA_CERTS']

def on_connect(client, userdata, flags, rc):
    global connected  # Use global variable
    if rc == 0:

        print("[INFO] Connected to broker")
        connected = True  # Signal connection
    else:
        print("[INFO] Error, connection failed")

    client.subscribe("PICTURE")
    ###client.loop_forever() - wrong place
    
def on_publish(client, userdata, result):
    print("Published!")
    
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print("Topic : ", msg.topic)
    f = open("/var/www/acgtest.info/server/gunicorn/mqttclient1/output.jpg", "wb")  #there is a output.jpg which is different
    f.write(msg.payload)
    f.close()
    
    
def connect(mqtt_client, mqtt_username, mqtt_password, broker_endpoint, port):
    global connected

    if not mqtt_client.is_connected():
        mqtt_client.username_pw_set(mqtt_username, password=mqtt_password)
        mqtt_client.on_connect = on_connect
        mqtt_client.on_publish = on_publish
        mqtt_client.on_subscribe = on_subscribe
        mqtt_client.on_message = on_message
        mqtt_client.tls_set(ca_certs=TLS_CERT_PATH, certfile=None,
                            keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                            tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        mqtt_client.tls_insecure_set(False)
        mqtt_client.connect(broker_endpoint, port=port)
        mqtt_client.loop_start()

        attempts = 0

        while not connected and attempts < 5:  # Wait for connection
            print(connected)
            print("Attempting to connect...")
            time.sleep(1)
            attempts += 1

    if not connected:
        print("[ERROR] Could not connect to broker")
        return False

    return True


def publish(mqtt_client, topic, payload):

    try:
        mqtt_client.publish(topic, payload)

    except Exception as e:
        print("[ERROR] Could not publish data, error: {}".format(e))


def main(mqtt_client):
    ##payload = json.dumps({"tls_publish_test": 20})
    ##topic = "{}{}".format(TOPIC, DEVICE_LABEL)

    if not connect(mqtt_client, MQTT_USERNAME,
                   MQTT_PASSWORD, BROKER_ENDPOINT, TLS_PORT):
        return False

    return True

if __name__ == '__main__':
    mqtt_client = mqttClient.Client()
    while True:
        main(mqtt_client)
        now = datetime.now()
        seconds = now.strftime("%S")
        print(seconds)
        print("-------")
        print(seconds[-1])
        print("========")
        if seconds[-1] == "0":
            publish(mqtt_client, "TakeAPicture", 1)
            time.sleep(1)
