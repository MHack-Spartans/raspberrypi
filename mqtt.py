import paho.mqtt.client as paho
import json
from . import serial

def on_connect(client, userdata, flags, rc):
    print("Connection returned result:", rc)

def on_message(client, userdata, msg):
    print(msg.topic, msg.payload)

def on_message_dispense_now(client, userdata, msg):
    data = json.loads(msg.payload.decode('utf-8'))
    print(data)
    slot = data['slot']
    print(slot)
    mqttc.publish("dispense/now", payload=json.dumps(msg), qos=0)

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "data.iot.us-east-1.amazonaws.com"
awsport = 8883
clientId = "PillBuddyRPi"
thingName = "PillBuddyRPi"
caPath = "certs/aws-iot-rootCA.crt"
certPath = "certs/certificate.pem.crt"
keyPath = "certs/private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)

mqttc.connect(awshost, awsport, keepalive=60)

mqttc.message_callback_add('dispense/now', on_message_dispense_now)

mqttc.subscribe("dispense/#")

# mqttc.loop_start() # moved to __init__.py