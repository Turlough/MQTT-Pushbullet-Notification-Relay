
# MQTT-Pushbullet Relay
Subscribes to a MQTT topic which publishes a URL (of a video feed) occasionally. 
When received, creates a [Pushbullet](https://www.pushbullet.com/#setup)
notification that will be delivered to your phone and browser,
with a link to the video feed so you can examine your new intruder.
A timer prevents repeated (< 30 seconds interval) notifications from plaguing you.

## Instructions
Edit config/fake-config.py, and save as config.py. 
Use your own credentials and broker. 

## 
I will create companion repositories for object recognition later today (6 Mar 2019).
These create the MQTT publications that this subscribes to.