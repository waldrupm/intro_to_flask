from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(100), nullable=False, unique=True)
  password = db.Column(db.String(200), nullable=False)

  def __repr__(self):
    return f"User: {self.name}"

  def generate_password(self, password):
    self.password = generate_password_hash(password)

  def check_password(self, pw_to_check):
    return check_password_hash(self.password, pw_to_check)

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))
