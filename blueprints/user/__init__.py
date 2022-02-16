import self as self
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import logout_user, login_required, current_user

from controllers.message_controller import get_user_messages, get_MQTT_messages
from controllers.user_controller import get_all_but_current_user, get_user_by_id
import json

bp_user = Blueprint('bp_user', __name__)


@bp_user.get('/profile')
@login_required
def user_get():
    users = get_all_but_current_user()
    return render_template("user.html", users=users)


@bp_user.get('/logout')
def logout_get():
    user = current_user
    user.online = False
    if user.online:
        pass
        # check messages.
        # if message != 0
        # load messages

    from app import db
    db.session.commit()
    logout_user()
    return redirect(url_for('bp_open.index'))


@bp_user.get('/message/<user_id>')
def message_get(user_id):
    user_id = int(user_id)
    receiver = get_user_by_id(user_id)
    return render_template('message.html', receiver=receiver, user_id=user_id)



@bp_user.post('/message/')
def message_post():
    from app import db
    from models import Message

    # jsonencrypted = request.json
    test = request.json
    rec_id = test["receiver_id"]
    #print(rec_id)
    message = Message(sender_id=current_user.id,
                      encrypted=test['body'],
                      title=test['title'],
                      receiver_id=test["receiver_id"])

    # print(message)
    db.session.add(message)
    db.session.commit()

    user_message(rec_id)

    # senderinf = message_recv(user_id=test["receiver_id"], message)
    # koda i databaser är reeeeeeeeeeeeeeeeeeeeeeeeeeeee

    return redirect(url_for('bp_user.messages_get_sent'))


def user_message(rec_id):
    from app import db
    from models import message_recv
    from models import Message
    obj = db.session.query(Message).order_by(Message.id.desc()).first()
    print(obj)
    print(obj)
    # msg = message_recv.insert().values([  # try this
    #     {"user_id": int(rec_id)},
    #     {"message_id": int(obj.id)}
    # ])
    # test1 = message_recv.insert().values(user_id=f"{int(rec_id)}")
    # test2 = message_recv.insert().values(message_id=f"{int(obj.id)}")
    # msg_recv = (
    #     sqlalchemy.sql.expression.insert(message_recv).
    #     values(user_id=receiver_id, message_id=obj.id)
    # )
    # print(msg_recv)
    # print(msg_recv)
    db.session.add(message_recv.insert().values(user_id=f"{int(rec_id)}"))
    db.session.add(message_recv.insert().values(message_id=f"{int(obj.id)}"))
    db.session.commit()


@bp_user.get('/messages/sent')
def messages_get_sent():
    return render_template('message_sent.html')


@bp_user.get("/mailbox")
def mailbox_get():
    messages = get_user_messages()
    return render_template("mailbox.html", messages=messages)


@bp_user.post("/chat")
def chat_post():
    # MQTT_Chatt.main()
    variabel_namn = request.form['body']
    lines = [variabel_namn]
    with open('MQTT/chatlog.txt', 'a') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
    return redirect(url_for('bp_user.chat_get'))


@bp_user.get("/chat")
def chat_get():
    messages = get_MQTT_messages()
    with open("MQTT/chatlog.txt", "r") as f:
        chatmessages = f.read()
    return render_template("chattbox.html", content=chatmessages)
