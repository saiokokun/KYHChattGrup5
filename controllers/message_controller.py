from flask_login import current_user
user = current_user

def save_offline():
    pass


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
