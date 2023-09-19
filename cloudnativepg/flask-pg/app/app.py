from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:3TzKciq7s8T3yBmOzXMEYYeqCZceIGhq3mQGs5Uwmpq4apof3qhO4CIhBefv0ljl@cluster-example-rw/app'
db = SQLAlchemy(app)

# Define a simple model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __init__(self, username):
        self.username = username

@app.route('/')
def index():
    return 'Hello, Flask SQLAlchemy PostgreSQL Demo!'

@app.route('/add_user/<username>')
def add_user(username):
    new_user = User(username)
    db.session.add(new_user)
    db.session.commit()
    return f'User {username} added to the database.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
