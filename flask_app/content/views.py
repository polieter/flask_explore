from flask.views import MethodView

from flask import render_template
from flask import g

from flask_app.authentication.views import authenticated_user


class MainContent(MethodView):

    @authenticated_user
    def get(self):
        return render_template('content.html', user=str(g.user.username))


class Index(MethodView):

    def get(self):
        return render_template('index.html', user=str(g.user.username))