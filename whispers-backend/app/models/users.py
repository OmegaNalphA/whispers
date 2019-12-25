from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(16), index=True, unique=True)
    num_whispers = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    whispers = db.relationship('Whisper', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.uuid)

    def to_dict(self):
        return {
            "id": self.id,
            "uuid": self.uuid,
            "num_whispers": self.num_whispers
        }