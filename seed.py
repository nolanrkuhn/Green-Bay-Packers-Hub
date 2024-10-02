import os
from app import create_app, db
from app.models import Player
import requests

# Fetch the API key from the environment variable
API_KEY = os.getenv("SPORTS_DB_API_KEY")

if not API_KEY:
    raise ValueError("API key not found! Ensure it's set in the .env file.")

def fetch_player_data():
    url = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/searchplayers.php?t=Green_Bay_Packers"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get('player', [])
    else:
        print("Failed to fetch data from API.")
        return []

def seed_data():
    players = fetch_player_data()

    if players:
        for player_info in players:
            player = Player(
                name=player_info.get("strPlayer"),
                position=player_info.get("strPosition"),
                birthdate=player_info.get("dateBorn"),
                height=player_info.get("strHeight"),
                weight=player_info.get("strWeight"),
                team=player_info.get("strTeam"),
                player_thumb=player_info.get("strThumb")
            )
            db.session.add(player)

        db.session.commit()
        print("Seeded players from API.")
    else:
        print("No players found.")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_data()



