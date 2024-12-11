# import os
#
# class Config:
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///pylite.db')
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'assets')
import os

class Config:
    # General settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'mysecret')

    # Database settings
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///blog.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Asset directory
    ASSET_DIR = os.getenv('ASSET_DIR', os.path.join(os.path.dirname(__file__), 'assets'))

config = Config()
