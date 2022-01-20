import paho.mqtt.client as paho
import random

from flask_login import login_user, current_user

from blueprints import user
from blueprints.open import login_post

CLIENT_ID = f"kyh-mqtt-{random.randint(0, 1000)}"
USERNAME = "grupp5chatt"
PASSWORD = "chatt"
BROKER = "r62b1b61-internet-facing-50dbcaf82667383e.elb.eu-central-1.amazonaws.com"
PORT = 1883
USER = current_user.name
CRED = "\033[91m"
OKBLUE = '\033[94m'


def on_subscribe(client, userdata, mid, granted_qus):
    print(f"joined chat")


def on_connect(client, userdata, flags, rc, ):
    if rc == 0:
        print('Connected to chat')

    else:
        print(f'Failed to connect to chat. Error code {rc}')


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


def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    if USER not in str(payload):
        return f"{payload}"


def subscribe(client, sub_topic):
    # Subscribe on topic temperature/room1
    client.subscribe(f"chat/{sub_topic}")
    client.on_message = on_message


def main():
    client = connect_mqtt()
    # Start the paho loop that will
    # spawn a new thread and send and receive messages
    client.loop_start()
    username = "Greg"
    sub_topic = "aa"
    client.publish(f"chat/{sub_topic}", OKBLUE + f"{USER} joined the chat")
    print(f"Welcome {USER}")
    subscribe(client, sub_topic)
    while True:
        # Get current temperature

        from blueprints.open import chat_send
        message = f"{USER}: {chat_send}"
        # Publish to the topic temperature/room1 with temp

        # Publish to the topic temperature/room1 with temp
        # time.sleep(1)
        if "/exit" not in message:
            client.publish(f"chat/{sub_topic}", message)
        else:
            print("do you wanna leave an exit message? \n yes/no")
            choice = input()
            if choice == "yes":
                print("Print your exit message:\n")
                exit_message = f"{input()}"
                client.publish(f"chat/{sub_topic}", CRED + f"{USER} left the server with the message: '{exit_message}'")
                print(f"You have left the  with the message: {exit_message}")
                client.disconnect()
            else:
                client.publish(f"chat/{sub_topic}", CRED + f"{USER} left the server")
                print("You left the server")
                client.disconnect()




if __name__ == '__main__':
    main()
