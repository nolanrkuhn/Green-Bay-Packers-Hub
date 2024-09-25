# Green Bay Packers Stats

## Project Overview

**URL**: https://green-bay-packers-hub.onrender.com

The Green Bay Packers Stats website is a comprehensive platform that allows users to explore detailed information about Green Bay Packers players, view and manage their favorite players, and add custom stats for players. The project demonstrates a full-stack application using Flask for the backend, PostgreSQL for the database, and a clean, responsive frontend with Bootstrap.

## Website Features

- **Player Search**: Users can search for players by name or position and view detailed information about each player.
- **Favorites Management**: Users can add or remove players from their favorites list, providing easy access to the players they follow closely.
- **Custom Stats**: Registered users can add and update custom stats for players, allowing them to track performance metrics not available through the API.
- **Authentication**: Secure login and registration system using Flask-Login and Bcrypt for password hashing.
- **Responsive Design**: The site uses Bootstrap for a responsive, mobile-friendly interface.

## User Flow

1. **Home Page**: Users are greeted with a hub that links to various sections like Players, Favorites, and Stats.
2. **Player Search**: Users can filter players by name or position, view details, and add them to their favorites.
3. **Favorites**: Users can manage their favorite players, unfavorite them if needed, and access stats directly from this page.
4. **Add Stats**: Logged-in users can add or update custom stats for players, enhancing the data available on each player.
5. **Login/Logout**: Secure authentication ensures user data is protected. Users need to log in to manage favorites and add stats.

## Technology Stack

- **Backend**: Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-WTF, Flask-Bcrypt, Flask-Login
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: PostgreSQL
- **API**: The Sports DB API (for fetching player data)
- **Deployment**: Deployed using a WSGI server like Gunicorn, and potentially behind Nginx for production environments.

## API Usage

The site uses The Sports DB API to fetch data on Green Bay Packers players, including names, positions, and basic stats. Due to API limitations on certain stat categories, custom stats functionality was implemented to allow users to add their own data.

## How to Use the Site

1. **Navigate** to the home page to explore the main features.
2. **Search for Players** using the search bar on the Players page.
3. **Add to Favorites** to keep track of players you care about.
4. **Log In/Register** to add stats and manage your favorites.
5. **Update Stats** on the player stats page to track performance over time.

## Why These Features?

- **Player Search** and **Favorites Management** provide an easy way for fans to keep track of their favorite Packers players.
- **Custom Stats** allow users to add personalized stats, filling in gaps not covered by the available API.
- **Secure Authentication** ensures that user data and stat entries are protected, adding a personalized experience.

## Additional Notes

- The application is currently running on a development server. For production deployment, ensure to use a WSGI server like Gunicorn and configure it properly with a reverse proxy like Nginx.
- All forms include CSRF protection using Flask-WTF to ensure secure form submissions.

## Repository Organization

- **app/**: Main application folder containing routes, models, templates, and static files.
- **static/**: Contains all static files like images, CSS, and JavaScript.
- **templates/**: Contains HTML files structured for each route.
- **requirements.txt**: Lists all dependencies for the project.
- **config.py**: Configuration file for environment variables and application settings.

## Final Review

Before submitting the project:

- Ensure all features are tested and working as expected.
- Check that all routes redirect correctly and that flash messages appear as intended.
- Review the README for completeness and ensure that it provides a full overview of the application.

---

Congratulations on building and documenting your first Capstone Project! Be sure to include this README in your GitHub repository and submit it to your mentor for evaluation.
