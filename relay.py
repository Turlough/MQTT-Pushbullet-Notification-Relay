"""
	Python MQTT subsciber, using paho client.
	Subscribes to messages from object recognition,
	and relays it as a Pushbullet notification on receipt.
	A timer mechanism prevents flooding from subsequent detections
"""
import paho.mqtt.client as mqtt
import time

# Remember to create config/config.py (copy and edit fake-config.py)
from config import config
# Replace these with your own configuration
broker = config.broker
port = config.port
topic = config.topic
user = config.user
password = config.password
pb_token = config.pb_token

interval = 30

from pushbullet import Pushbullet

pb = Pushbullet(pb_token)
last = 0


def on_message(mosq, obj, msg):
    global last
    now = time.time()
    elapsed = now - last
    payload = msg.payload.decode("utf-8") 
    # print(payload)
    # print('{} - {} = {}'.format(now, last, elapsed))
    if elapsed > interval:
        print('Intruder!')
        pb.push_link("Intruder !", payload.strip())
    last = now

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic, 0)

if __name__ == '__main__':

    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect

    client.username_pw_set(user, password)
    client.connect(broker, port, 60)
    client.loop_forever()