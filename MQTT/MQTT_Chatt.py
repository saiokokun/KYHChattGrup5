import paho.mqtt.client as paho
import random

CLIENT_ID = f'kyh-mqtt-{random.randint(0, 1000)}'
USERNAME = '*'
PASSWORD = ''
BROKER = ''
PORT = 123
USER = CLIENT_ID
CRED = "\033[91m"
OKBLUE = '\033[94m'
sub_topic = "temp"


def on_connect(rc):
    if rc == 0:
        print('Connected to MQTT Broker')
    else:
        print(f'Failed to connect to Broker. Error code {rc}')


def connect_mqtt():
    # Create a MQTT client object.
    # Every client has an id
    client = paho.Client(CLIENT_ID)
    # Set username and password to connect to broker
    client.username_pw_set(USERNAME, PASSWORD)

    # When connection response is received from broker
    # call the function on_connect
    client.on_connect = on_connect

    # Connect to broker
    client.connect(BROKER, PORT)

    return client


def on_subscribe(mid, granted_qos):
    print('Subscribed')
    print('mid:', mid)
    print('qos:', granted_qos)


def on_message(msg):
    payload = msg.payload.decode()
    print(f'Current temp in {msg.topic}: {payload}')


def subscribe(client):
    # Subscribe on topic temperature/room1
    client.subscribe('temp')
    client.on_message = on_message


def main():
    client = connect_mqtt()
    # When we have subscribed to a topic, call this function
    client.on_subscribe = on_subscribe

    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    main()