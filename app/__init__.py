import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_appbuilder.security.manager import AUTH_OAUTH, AUTH_DB
from flask_appbuilder.security.views import AuthOAuthView

app = Flask(__name__)
app.config.from_object("config")

db = SQLA(app)
appbuilder = AppBuilder(app, db.session)


class MyOAuthView(AuthOAuthView):
    login_template = "oauth.html"


appbuilder.add_view(MyOAuthView, "OAuth", icon="fa-google", label="OAuth Login")

appbuilder.sm.authentications = [AUTH_DB, AUTH_OAUTH]

from . import views
