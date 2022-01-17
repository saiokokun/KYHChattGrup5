from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
username = "Alice"
friends = ["Alice", "Carl", "Dina", "Poppe"]


@app.get('/')
def index():
    return render_template("index.html")


@app.get('/user')
def user_get():
    return render_template("user.html", name=username, friends=friends)


@app.post("/user")
def user_post():
    friend = request.form["friend_name"]
    friends.append(friend)
    return redirect(url_for("user_get"))


