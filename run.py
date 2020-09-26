from app import app
from db import db

db.init_app(app)

@app.before_first_request  #To create data.db file and all the tables in it using SQLAlchemy
def create_tables():
    db.create_all()
