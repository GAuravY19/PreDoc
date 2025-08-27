from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

host = os.getenv("host")
dbname = os.getenv('db_name')
user = os.getenv('user')
password = os.getenv('password')
port = os.getenv('port')

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{dbname}'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

conn = psycopg2.connect(host = host,
                        dbname = dbname,
                        user = user,
                        password = password,
                        port = port)

curr = conn.cursor()
