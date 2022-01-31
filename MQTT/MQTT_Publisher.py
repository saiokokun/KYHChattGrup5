import paho.mqtt.client as paho
import random
import time



CLIENT_ID = f'kyh-mqtt-{random.randint(0, 1000)}'
USERNAME = 'test1'
PASSWORD ="test1"
BROKER = 'o6a92cf9.eu-central-1.emqx.cloud'
PORT = 15372
USER = CLIENT_ID
CRED = "\033[91m"
OKBLUE = '\033[94m'
sub_topic = "kyh/joakim"


def on_connect(client, userdata, flags, rc):
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


    sub_topic = "temp"
    while True:
        # Get current temperature
        from controllers import message_controller as MC
        from blueprints.user import chat_post
        content = chatboxCRT
        content = chat_post
        if content != None :

            client.publish(f'temperature/{sub_topic}', str(content))
            # Interval to publish messages
            time.sleep(1)
        else:
            time.sleep(5)
            return



    #client.loop_stop()
def messages():

            messages()

if __name__ == '__main__':
    main()