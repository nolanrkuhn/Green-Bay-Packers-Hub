from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app.models import Player

def get_positions():
    positions = Player.query.with_entities(Player.position).distinct().all()
    return [('', 'All Positions')] + [(pos.position, pos.position) for pos in positions]

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
class PlayerStatForm(FlaskForm):
    games_played = IntegerField('Games Played', validators=[DataRequired()])
    touchdowns = IntegerField('Touchdowns', validators=[DataRequired()])
    yards = IntegerField('Yards', validators=[DataRequired()])
    submit = SubmitField('Save Stats')

class PlayerSearchForm(FlaskForm):
    name = StringField('Player Name')
    position = SelectField('Position', choices=[])
    submit = SubmitField('Search')

class FavoriteForm(FlaskForm):
    submit = SubmitField('Favorite')
