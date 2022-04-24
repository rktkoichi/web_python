from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    create_at = db.Column(db.datetime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    @property
    def password(self):
        raise AttributeError("読み取り不可")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)