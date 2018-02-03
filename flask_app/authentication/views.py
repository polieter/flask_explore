from flask_app.authentication.forms import LoginForm
from flask_app.authentication.models import User

from flask import render_template
from flask import redirect
from flask import url_for
from flask import session
from flask import request
from flask import flash
from flask import g

from flask.views import MethodView

from flask_login import AnonymousUserMixin
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user

from flask_app import app
from flask_app import login_manager

from functools import wraps


@app.before_request
def before_request():
    g.user = current_user


def authenticated_user(func):
    @wraps(func)
    def wraps_function(*args, **kwargs):
        if g.user is not None and g.user.is_authenticated:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wraps_function


class Anonymous(AnonymousUserMixin):

    def __init__(self):
        self.username = 'None'


login_manager.anonymous_user = Anonymous


class Login(MethodView):

    def __init__(self):
        self.user = None
        self.form = None

    def get(self):
        self.form = LoginForm()
        return render_template('login.html', form=self.form,
                               user=g.user.username)

    def post(self):
        self.form = LoginForm(request.form)
        self.user = User.query.filter_by(username=self.form.username.data).first()
        if self._correct_credential():
            login_user(self.user)
            session['logged_in'] = True
            flash('Logged in successfully.')
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

    def _correct_credential(self):
        if self.user is not None and self.form.validate_on_submit():
            return self.user.check_password(self.form.password.data)
        return False


class Logout(MethodView):

    def get(self):
        logout_user()
        return redirect(url_for('index'))
