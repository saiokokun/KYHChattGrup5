from flask_login import current_user


def get_all_but_current_user():
    from models import User
    user = current_user
    return User.query.filter(User.id != user.id).all()


def get_all_users():
    from models import User
    return User.query.all()


def get_user_by_id(user_id):
    from models import User
    return User.query.filter(User.id == user_id).first()


def post_user_public_key(public_key):
    """ Gets the users public key and stores it in the database"""
    from models import User
    from app import db

    user_id = User.get_id(current_user)
    user = get_user_by_id(user_id)
    user.public_key = public_key
    db.session.commit()
