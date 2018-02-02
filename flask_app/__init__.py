from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__, instance_relative_config=True, static_url_path='/static')
app.config.from_pyfile('config.py', silent=True)

csrf = CSRFProtect()
csrf.init_app(app)

db = SQLAlchemy(app)

from flask_app.authentication.models import User

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from flask_app.authentication.views import Login, Logout
from flask_app.content.views import Index, MainContent


app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/logout', view_func=Logout.as_view('logout'))
app.add_url_rule('/', view_func=Index.as_view('index'))
app.add_url_rule('/content', view_func=MainContent.as_view('content'))
