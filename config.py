import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    
    # Use the DATABASE_URL environment variable provided by Render
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://green_bay_packer_database_user:2Wui3XrzGZnpFmSxUqql1yBi1oNKiWyY@dpg-cruf69tumphs73emb5ag-a.oregon-postgres.render.com/green_bay_packer_database'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

