#!/usr/bin/python

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import ssl

import configparser
config = configparser.ConfigParser()
config.sections()
config.read('app.ini')

username = config['app']['MQTT_USERNAME']
password = config['app']['MQTT_PASSWORD']

auth = {
  'username':username,
  'password':password
}

tls = {
  'ca_certs':"/etc/ssl/certs/ca-certificates.crt",
  'tls_version':ssl.PROTOCOL_TLSv1
}

publish.single("devices/events/",
  payload="hello world",
  hostname="acgtest.info",
  client_id="acgtest",
  auth=auth,
  tls=tls,
  port=8883,
  protocol=mqtt.MQTTv311)
