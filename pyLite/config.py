import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///pylite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
