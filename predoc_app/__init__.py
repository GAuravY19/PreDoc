from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

host = os.getenv("DB_HOST")
dbname = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
port = os.getenv('DB_PORT')

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('APP_SECRET_KEY')
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
