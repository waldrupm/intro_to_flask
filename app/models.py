from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  password = db.Column(db.String(200), nullable=False)

  def generate_password(self, password):
    self.password = generate_password_hash(password)
