from ldap3 import Server, Connection, ALL
from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms import validators
from app import db, app


# def get_ldap_connection():
#     server = Server(app.config['LDAP_PROVIDER_URL'], get_info=ALL)
#     conn = Connection(server, auto_bind=True)
#     return conn


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))

    def __init__(self, username, password):
        self.username = username

    @staticmethod
    def try_login(username, password):
        server = Server(app.config['LDAP_PROVIDER_URL'], get_info=ALL)
        Connection(server,
                   user=f'cn={username},dc=example,dc=org',
                   password=password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
