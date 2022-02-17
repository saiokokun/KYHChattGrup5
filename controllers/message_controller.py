from flask_login import current_user

from app import db
from controllers.user_controller import get_user_by_id
from models import Message

user = current_user


# userID = db.sqlite.user_ID

def save_offline():
    pass
#pling client or sumth


# def create_message(title, bbody, receiver_id):
#     message = Message(title=title, bbody=bbody, sender_id=user.id)
#     receiver_id = int(receiver_id)
#     receiver = get_user_by_id(receiver_id)
#     message.receivers.append(receiver)
#
#     if receiver.online == False:
#         save_offline()
#
#     db.session.add(message)
#     db.session.commit()


def get_user_messages():
    return current_user.recv_messages





def get_MQTT_messages():
    with open("MQTT/chatlog.txt") as f:
        lines = f.readlines()
        return lines


def get_unread_msg_count():
    user = current_user
    msg_count = 0

    for msg in user.recv_messages:
        if not msg.read:
            msg_count += 1

    return msg_count
