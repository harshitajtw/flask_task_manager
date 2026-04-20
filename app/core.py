from app import db
from app.models import Task, User
from app.models import User

from flask_login import current_user
from flask import request,jsonify
from flask_jwt_extended import get_jwt_identity
from app.tasks import send_welcome_email
# ---------------- TASK ---------------- #


def create_task_service(data):
    user_id=int(get_jwt_identity())
    task = Task(title=data['title'], user_id=user_id)

    db.session.add(task)
    db.session.commit()

    return task


def get_tasks_service():
    user_id=get_jwt_identity() 
    return Task.query.filter_by(user_id=current_user.id).all()


# -------- USER -------- #

def register_user_service(data):
    existing_user = User.query.filter_by(username=data['username']).first()

    if existing_user:
        return None

    user = User(username=data['username'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()
    send_welcome_email.delay(user.username) 
    return user


def login_user_service(data):
    user = User.query.filter_by(username=data['username']).first()

    if not user:
        return None

    if not user.check_password(data['password']):
        return None

    return user