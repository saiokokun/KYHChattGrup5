from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
username = "Alice"
friends = ["Bob", "Carl", "Dina", "Eric", "You"]


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/user")
def user_get():
    return render_template("user.html", name=username, friends=friends)


@app.get("/login")
def login_get():
    return render_template("login.html", name=username, friends=friends)


@app.get("/mailbox")
def mailbox_get():
    return render_template("user.html", name=username, friends=friends)


@app.get("/settings")
def settings_get():
    return render_template("user.html", name=username, friends=friends)


@app.post("/user")
def user_post():
    friend = request.form["friend_name"]
    friends.append(friend)
    return redirect(url_for("user_get"))


@app.post("/login")
def login_post():
    pass
    # tuple from the browser? or array? json?
    # "flask run" in the terminal
