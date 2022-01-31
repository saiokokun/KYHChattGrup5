from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import logout_user, login_required, current_user

from controllers.message_controller import create_message, get_user_messages, chatboxCTR, get_MQTT_messages
from controllers.user_controller import get_all_but_current_user, get_user_by_id

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

    from app import db
    db.session.commit()
    logout_user()
    return redirect(url_for('bp_open.index'))


@bp_user.get('/message/<user_id>')
def message_get(user_id):
    user_id = int(user_id)
    receiver = get_user_by_id(user_id)
    return render_template('message.html', receiver=receiver)


@bp_user.post("/message")
def message_post():
    title = request.form["title"]
    body = request.form["body"]
    receiver = request.form["user_id"]
    create_message(title, body, receiver)

    return redirect(url_for("bp_user.user_get"), receiver=receiver)


@bp_user.get("/mailbox")
def mailbox_get():
    messages = get_user_messages()
    return render_template("mailbox.html", messages=messages)


from MQTT import MQTT_Chatt


@bp_user.post("/chat")
def chat_post():
    #MQTT_Chatt.main()
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
