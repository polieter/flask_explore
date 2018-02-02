from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password_hash = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.set_password(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    @staticmethod
    def set_password(password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return str(self.id)
