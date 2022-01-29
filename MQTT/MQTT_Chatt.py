import paho.mqtt.client as paho
import random

from blueprints import user_get
from blueprints.open import login_post


USER = "user_test"
CRED = "\033[91m"
OKBLUE = '\033[94m'
MESSAGE = ""





def on_connect(client, userdata, flags, rc, ):
    if rc == 0:
        print('Connected to chat')

    else:
        print(f'Failed to connect to chat. Error code {rc}')




def on_message(client, userdata, msg):
    payload = msg.payload.decode()
   ## if USER not in str(payload):
  ## ##     return f"{payload}"


def subscribe(client, sub_topic):
    # Subscribe on topic temperature/room1
    client.subscribe(f"chat/{sub_topic}")
    client.on_message = on_message

from paho.mqtt import client
def main():
    username = "Greg"
    sub_topic = "aa"
    client.publish(f"chat/{sub_topic}", OKBLUE + f"{USER} joined the chat")
    print(f"Welcome {USER}")
    subscribe(client, sub_topic)
    while True:
        # Get current temperature

        message = f"{USER}: {MESSAGE}"
        # Publish to the topic temperature/room1 with temp

        # Publish to the topic temperature/room1 with temp
        # time.sleep(1)
        if "/exit" not in message:

            client.publish(f"chat/{sub_topic}", message)
        else:

                client.disconnect()


if __name__ == '__main__':
    main()
