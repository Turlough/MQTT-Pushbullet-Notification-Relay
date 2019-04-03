
# MQTT-Pushbullet Relay

You will also need the publisher for this subscriber: https://github.com/Turlough/Object-Recognition-on-Pi-with-Movidius

Effectively, this filters the objects published by topic 'camera/person', 
and generates a notification for your phone and to your browser when a new person is detected, using [Pushbullet](https://www.pushbullet.com/). 

Ideal for an IP security camera. 

## Instructions
Get your Pushbullet Api Token from [Account -> Settings -> Access Tokens](https://www.pushbullet.com/#settings/account)

Edit config/fake-config.py, and save as config.py
Use your own credentials and broker for the MQTT section, and your own access token from Pushbullet


