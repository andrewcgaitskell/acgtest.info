#!/usr/bin/python

import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import ssl

import configparser
config = configparser.ConfigParser()
config.sections()
config.read('app.ini')


auth = {
  'username':"ciscohackhub.azure-devices.net/lora1",
  'password':"SharedAccessSignature sr=ciscohackhub.azure-devices.net%2Fdevices%2Flora1&sig=xxxx&se=1463048772"
}

tls = {
  'ca_certs':"/etc/ssl/certs/ca-certificates.crt",
  'tls_version':ssl.PROTOCOL_TLSv1
}

publish.single("devices/lora1/messages/events/",
  payload="hello world",
  hostname="acgtest.info",
  client_id="acgtest",
  auth=auth,
  tls=tls,
  port=8883,
  protocol=mqtt.MQTTv311)
