from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from app.forms import FavoriteForm
from app.models import Favorite, Player
from app import db

favorites_bp = Blueprint('favorites', __name__)

@favorites_bp.route('/my-favorites')
@login_required
def my_favorites():
    form = FavoriteForm()
    favorites = Favorite.query.filter_by(user_id=current_user.id).all()
    favorite_players = [favorite.player for favorite in favorites]
    return render_template('favorites.html', players=favorite_players, form=form)

@favorites_bp.route('/favorite/<int:player_id>', methods=['POST'])
@login_required
def favorite_player(player_id):
    player = Player.query.get(player_id) 
    
    if not player:
        flash("Player not found", "danger")
        return redirect(url_for('players.show_players'))

    favorite = Favorite.query.filter_by(user_id=current_user.id, player_id=player_id).first()

    if favorite:
        flash("Player already in favorites", "warning")
    else:
        new_favorite = Favorite(user_id=current_user.id, player_id=player_id)
        db.session.add(new_favorite)
        db.session.commit()
        flash("Player added to favorites!", "success")
    
    return redirect(url_for('favorites.my_favorites'))

@favorites_bp.route('/unfavorite/<int:player_id>', methods=['POST'])
@login_required
def unfavorite_player(player_id):
    player = Player.query.get(player_id)

    favorite = Favorite.query.filter_by(user_id=current_user.id, player_id=player_id).first()

    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        flash("Player removed from favorites", "info")
    else:
        flash("Player not found in favorites", "danger")
    
    return redirect(url_for('favorites.my_favorites'))


