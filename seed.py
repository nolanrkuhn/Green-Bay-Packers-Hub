import os
from app import create_app, db
from app.models import Player
from dotenv import load_dotenv
import requests

load_dotenv()

# Fetch the API key from the environment variable
API_KEY = os.getenv("SPORTS_DB_API_KEY")

def fetch_player_data():
    if not API_KEY:
        print("API key not found! Ensure it's set in the .env file.")
        return []

    url = f"https://www.thesportsdb.com/api/v1/json/{API_KEY}/searchplayers.php?t=Green_Bay_Packers"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json().get('player', [])
        print(f"Fetched data: {data}") 
        return data
    else:
        print("Failed to fetch data from API.")
        return []

def seed_data():
    # Mock players as fallback data
    mock_players = [
        {
            "name": "Aaron Rodgers",
            "position": "Quarterback",
            "birthdate": "1983-12-02",
            "height": "6'2\"",
            "weight": "225 lbs",
            "team": "Green Bay Packers",
            "player_thumb": "https://example.com/aaron_rodgers.jpg",
        },
    ]

    players = fetch_player_data()

    if not players:
        print("API response is empty or invalid. Using mock data for testing.")
        players = mock_players

    for player_info in players:
        print(f"Seeding player: {player_info}")  # Debugging player data
        print(f"Parsed fields: Name={player_info.get('strPlayer')}, Position={player_info.get('strPosition')}, Thumb={player_info.get('strThumb')}")
        player = Player(
            name=player_info.get("strPlayer", "Unknown"),
            position=player_info.get("strPosition", "Unknown"),
            birthdate=player_info.get("dateBorn"),
            height=player_info.get("strHeight"),
            weight=player_info.get("strWeight"),
            team=player_info.get("strTeam", "Green Bay Packers"),
            player_thumb=player_info.get("strThumb") or player_info.get("strCutout") or "/static/images/default-player.png",
        )
        db.session.add(player)

    db.session.commit()
    
    print("Seeding complete.")
    print("Database contents after seeding:")
    players_in_db = Player.query.all()
    for p in players_in_db:
        print(f"Name={p.name}, Position={p.position}, Thumb={p.player_thumb}")




