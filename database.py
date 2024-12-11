from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def create_table(model):
    model.__table__.create(db.engine)
