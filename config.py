import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    
    # Use the DATABASE_URL environment variable provided by Render
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres@localhost/packers_db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

