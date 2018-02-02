from flask_app import db
from flask_app.authentication.models import User


def create_db():
    db.create_all()

    test_user = User('test', 'default')
    db.session.add(test_user)
    db.session.commit()


if __name__ == '__main__':
    create_db()
