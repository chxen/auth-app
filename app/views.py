from flask import render_template, redirect, request, session
from flask_appbuilder.security.manager import BaseSecurityManager
from flask_appbuilder.security.sqla.manager import SecurityManager
from flask_appbuilder.security.views import UserDBModelView
from flask_appbuilder.security.sqla.models import User

from . import app, appbuilder, db

class CustomSecurityManager(SecurityManager):
    def auth_user_db(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            return True
        return False

appbuilder.security_manager = CustomSecurityManager(appbuilder)

@app.route('/login_form', methods=['GET', 'POST'])
def login_form():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if appbuilder.sm.auth_user_db(username, password):
            session['username'] = username
            return redirect('/dashboard')
        else:
            return render_template('oauth.html', error='Invalid username or password')
    return render_template('oauth.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return f'Welcome to the dashboard, {username}!'
    else:
        return redirect('/login_form')

@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

db.create_all()
