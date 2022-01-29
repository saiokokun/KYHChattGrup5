from flask_login import current_user

from app import db
from controllers.user_controller import get_user_by_id
from models import Message

user = current_user


def create_message(title, body, receiver_id):
    message = Message(title=title, body=body, sender_id=user.id)
    receiver_id = int(receiver_id)
    receiver = get_user_by_id(receiver_id)
    message.receivers.append(receiver)
    db.session.add(message)
    db.session.commit()


def get_user_messages():
    return current_user.recv_messages


##def chatboxCTR(body, receiver_id):
##    message = Message(body=body, sender_id=user.id)
##    receiver_id = int(receiver_id)
##    receiver = get_user_by_id(receiver_id)
##    message.receivers.append(receiver)
##    db.session.add(message)
##    db.session.commit()
