from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # ili tvoja baza
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()  # Kreira tabele ako ne postoje

    return app


if __name__ == '__main__':
    # Kreiraj app i context
    app = create_app()

    with app.app_context():
        from scraper.gog_scraper import scrape_all_games  # importuj funkciju scrappera
        scrape_all_games()
