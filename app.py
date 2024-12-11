# from flask import Flask, render_template, jsonify, request
# from database import get_db, init_db
# import random
#
# app = Flask(__name__)
# init_db()
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/random_number')
# def random_number():
#     number = random.randint(1, 100)
#     return jsonify(number=number)
#
# @app.route('/reverse_string', methods=['POST'])
# def reverse_string():
#     data = request.get_json()
#     reversed_string = data['string'][::-1]
#     return jsonify(reversed_string=reversed_string)
#
# @app.route('/add_user', methods=['POST'])
# def add_user():
#     data = request.get_json()
#     name = data['name']
#     db = get_db()
#     new_user = db.User(name=name)
#     db.session.add(new_user)
#     db.session.commit()
#     return jsonify(id=new_user.id, name=new_user.name)
#
# @app.route('/get_users', methods=['GET'])
# def get_users():
#     db = get_db()
#     users = db.session.query(db.User).all()
#     return jsonify(users=[{"id": user.id, "name": user.name} for user in users])
#
# if __name__ == '__main__':
#     app.run(port=5000, debug=True)


from flask import Flask

from components.blog.url import blog_service
from pyLite.config import Config
from flask_sqlalchemy import SQLAlchemy
from database import init_db


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# Initialize the database
init_db(app)

# Ensure all tables are created
with app.app_context():
    db.create_all()

# Register blueprints
app.register_blueprint(blog_service, url_prefix='/api/blog')


@app.route('/')
def index():
    return "Welcome to PyLite!"

if __name__ == "__main__":

    db.create_all()# Create the tables
    app.run(debug=True)
