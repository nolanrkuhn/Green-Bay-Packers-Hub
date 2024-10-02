import os
from app import create_app, db
from app.models import Player
import requests

def seed_data():
    api_key = os.getenv("SPORTS_DB_API_KEY")
    api_url = f"https://www.thesportsdb.com/api/v1/json/{api_key}/searchplayers.php?t=Green_Bay_Packers"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        for player_info in data.get("player", []):
            player = Player(
                name=player_info["strPlayer"],
                position=player_info["strPosition"],
                birthdate=player_info["dateBorn"],
                height=player_info["strHeight"],
                weight=player_info["strWeight"],
                team=player_info["strTeam"],
                player_thumb=player_info["strThumb"]
            )
            db.session.add(player)

        db.session.commit()
        print("Seeded players from API.")
    else:
        print("Failed to fetch data from API.")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_data()



