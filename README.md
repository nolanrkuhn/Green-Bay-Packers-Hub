
# Green Bay Packers Stats

## Project Overview

**URL**: https://green-bay-packers-hub.onrender.com

The Green Bay Packers Stats website is a comprehensive platform that allows users to explore detailed information about Green Bay Packers players, view and manage their favorite players, and add custom stats for players. The project demonstrates a full-stack application using Flask for the backend, PostgreSQL for the database, and a clean, responsive frontend with Bootstrap.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- PostgreSQL
- Virtual environment (optional but recommended)

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/nolanrkuhn/Green-Bay-Packers-Hub.git
    cd Green-Bay-Packers-Hub
    ```

2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For MacOS/Linux
    venv\Scripts\activate  # For Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the `.env` file with the following variables:
    ```
    FLASK_ENV=development
    SECRET_KEY=your_secret_key
    DATABASE_URL=your_postgresql_url
    SPORTS_DB_API_KEY=your_api_key
    ```

5. Initialize the database:
    ```bash
    flask db upgrade
    python seed.py
    ```

6. Run the application:
    ```bash
    flask run
    ```

### Database Schema
Here's the structure of the main database table used:

- **Player**
  - `id`: Primary Key (Integer)
  - `name`: Player's name (String)
  - `position`: Player's position (String)
  - `birthdate`: Player's birthdate (String)
  - `height`: Player's height (String)
  - `weight`: Player's weight (String)
  - `team`: Team name (String, default: "Green Bay Packers")
  - `player_thumb`: Player's thumbnail URL (String)

## Testing
To run tests:
```bash
pytest
```

## Contributors
- Nolan Kuhn
