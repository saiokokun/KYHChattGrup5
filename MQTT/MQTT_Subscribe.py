import paho.mqtt.client as paho
import random

from MQTT.MQTT_Chatt import on_connect

CLIENT_ID = f"kyh-mqtt-{random.randint(0, 1000)}"
USERNAME = 'test1'
PASSWORD = 'test1'
BROKER = 'o6a92cf9.eu-central-1.emqx.cloud'
PORT = 15372

def main():
    client = connect_mqtt()
    # Start the paho loop that will
    # spawn a new thread and send and receive messages
    client.loop_start()

def on_subscribe(client, userdata, mid, granted_qus):
    print(f"joined chat")

def connect_mqtt():
    # Create an MQTT client object
    # Every client has an id
    client = paho.Client(CLIENT_ID)

    # Set username and password to connect to broker
    client.username_pw_set(USERNAME, PASSWORD)

    # when connection response is received from broker
    # call the function on_connect
    client.on_connect = on_connect

    # connect to broker
    client.connect(BROKER, PORT)

    return client


if __name__ == "__main__":
    main()
