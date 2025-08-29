from flask_login import UserMixin
from predoc_app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),\
                            nullable=False, server_default=db.func.now())
    profile_photo = db.Column(db.String, nullable=False, default='default.jpg')

    def get_id(self):
        return str(self.user_id)

