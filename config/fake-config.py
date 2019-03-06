'''
	Keeps congiguration separate from code
'''
port = 1883
topic = 'camera/person'

# Use your own credentials and broker here, e.g. 
# A list of public brokers can be found here, for prototyping
# https://github.com/mqtt/mqtt.github.io/wiki/public_brokers
broker = '172.16.92.200'
user = 'fakeuser' 
password = 'secretpassword'
# Generate token here: https://www.pushbullet.com/#settings/account
pb_token = 'api-key'