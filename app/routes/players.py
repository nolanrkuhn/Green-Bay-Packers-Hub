from flask import Blueprint, render_template, request
from app.models import Player
from app.forms import PlayerSearchForm, get_positions

players_bp = Blueprint('players', __name__)

def get_positions():
    positions = Player.query.with_entities(Player.position).distinct().all()
    return [('', 'All Positions')] + [(pos.position, pos.position) for pos in positions]

@players_bp.route('/players', methods=['GET', 'POST'])
def show_players():
    form = PlayerSearchForm()
    form.position.choices = get_positions()
    players_query = Player.query  

    if form.validate_on_submit():
        name_query = form.name.data
        position_query = form.position.data

        print(f"Name Query: {form.name.data}")
        print(f"Position Query: {form.position.data}")

        if name_query:
            players_query = players_query.filter(Player.name.ilike(f'%{name_query}%'))

        if position_query:
            players_query = players_query.filter_by(position=position_query)

    players = players_query.all()

    print("Filtered Players:")
    for player in players:
        print(f"Name={player.name}, Position={player.position}, Image={player.player_thumb}")

    for player in players:
        player.name = player.name or "N/A"
        player.position = player.position or "N/A"
        player.player_thumb = player.player_thumb or "/static/images/default-player.png"

    return render_template('players.html', players=players, form=form)


