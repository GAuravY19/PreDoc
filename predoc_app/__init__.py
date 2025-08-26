from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SECRET_KEY'] = '4015fab54c59c9f12e6096763ec201fc65219f0d9b2e0a317df0bb4714c00547'
bcrypt = Bcrypt(app)
