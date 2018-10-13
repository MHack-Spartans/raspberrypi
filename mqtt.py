import paho.mqtt.client as paho
import ssl
import json

import os.path
BASE = os.path.dirname(os.path.abspath(__file__))

def on_connect(client, userdata, flags, rc):
    print("Connection returned result:", rc)

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)

def on_message_dispense_now(client, userdata, msg):
    data = json.loads(msg.payload.decode('utf-8'))
    print(data)
    mqttc.publish("dispense/now", payload=json.dumps(msg), qos=0)

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "data.iot.us-east-1.amazonaws.com"
awsport = 8883
clientId = "PillBuddyRPi"
thingName = "PillBuddyRPi"
caPath = os.path.join(BASE, "certs/aws-iot-rootCA.crt")
certPath = os.path.join(BASE, "certs/certificate.pem.crt")
keyPath = os.path.join(BASE, "certs/private.pem.key")

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.subscribe("dispense/#")

# mqttc.loop_start() # moved to __init__.py