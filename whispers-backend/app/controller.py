from app.models import User, Whisper
from app import db

def create_user(uuid):
    new_user = User(uuid=uuid)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_user(uuid):
    print(User.query.one_or_none())