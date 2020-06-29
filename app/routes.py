from app import app, db
from app.models import User
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    name = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
      return redirect(url_for('register'))
    u = User(name=name, email=email, password=password)
    u.generate_password(u.password)

    db.session.add(u)
    db.session.commit()
    print(name, email, password, confirm_password)
    return redirect(url_for('login'))
  return render_template('register.html')