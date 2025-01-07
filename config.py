import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    
    # Use the DATABASE_URL environment variable provided by Render
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://packers_sql_user:RL7fYgEnKAlAsATvZDhnUp0pLA6ggJQj@dpg-ctrbj5ogph6c73cvi12g-a.oregon-postgres.render.com/packers_sql'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

