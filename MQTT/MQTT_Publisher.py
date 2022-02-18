import paho.mqtt.client as paho
import random
import time
from controllers import message_controller as MC
from controllers.message_controller import save_offline

CLIENT_ID = f'kyh-mqtt-{random.randint(0, 1000)}'
USERNAME = ''
PASSWORD = ''
BROKER = ''
PORT = 123
USER = CLIENT_ID
CRED = "\033[91m"
OKBLUE = '\033[94m'
sub_topic = "kyh/greg/"


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

    # Publish to the topic temperature/room1 with temp


def main():
    client = connect_mqtt()
    # Start the paho loop that will
    # spawn a new thread and send and receive messages
    client.loop_start()

    sub_topic = save_offline()
    new_message = 0

    # time.sleep(10)
    while True:
        if new_message != 0:
            # Get current temperature
            temp = MC.save_offline()
            # Publish to the topic temperature/room1 with temp
            client.publish(f'kyh/greg/{sub_topic}', temp)
            # Interval to publish messages
            time.sleep(1)

    client.loop_stop()


if __name__ == '__main__':
    main()
