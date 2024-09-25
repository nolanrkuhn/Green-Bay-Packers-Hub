from app import db, bcrypt
from flask_login import UserMixin

class Player(db.Model):
    __tablename__ = 'players'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.String(50))
    height = db.Column(db.String(20))
    weight = db.Column(db.String(20))
    team = db.Column(db.String(100), default="Green Bay Packers")  
    player_thumb = db.Column(db.String(255)) 
    
class Stat(db.Model):
    __tablename__ = 'stats'
    
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    games_played = db.Column(db.Integer)
    touchdowns = db.Column(db.Integer)
    yards = db.Column(db.Integer)
    player = db.relationship('Player', backref='stats')
    
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        
class Favorite(db.Model):
    __tablename__ = 'favorites'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('players.id'), nullable=False)
    
    user = db.relationship('User', backref='favorites')
    player = db.relationship('Player', backref='favorited_by')