from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app.models import Player, Stat
from app.forms import PlayerStatForm
from app import db

stats_bp = Blueprint('stats', __name__)

@stats_bp.route('/add-stats', methods=['GET', 'POST'])
@login_required
def add_stats():
    players = Player.query.all()

    player_id = request.args.get('player_id')
    selected_player = Player.query.get(player_id) if player_id else None

    form = PlayerStatForm()

    if form.validate_on_submit() and selected_player:
        stat = Stat.query.filter_by(player_id=selected_player.id).first()

        if not stat:
            stat = Stat(
                player_id=selected_player.id,
                games_played=form.games_played.data,
                touchdowns=form.touchdowns.data,
                yards=form.yards.data
            )
            db.session.add(stat)
        else:
            stat.games_played = form.games_played.data
            stat.touchdowns = form.touchdowns.data
            stat.yards = form.yards.data

        db.session.commit()
        flash("Stats saved successfully!", "success")
        return redirect(url_for('stats.player_stats', player_id=selected_player.id))

    return render_template('add_stats.html', form=form, players=players, selected_player=selected_player)

@stats_bp.route('/player-stats/<int:player_id>')
@login_required
def player_stats(player_id):
    player = Player.query.get(player_id)
    stats = Stat.query.filter_by(player_id=player_id).all()

    if not player:
        flash('Player not found', 'danger')
        return redirect(url_for('stats.add_stats'))

    return render_template('player_stats.html', player=player, stats=stats)