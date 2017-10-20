from flask_sqlalchemy import SQLAlchemy
from connexion import AbstractApp

db = SQLAlchemy()

def configureAppForDB(app: AbstractApp):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@172.17.8.101/testdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
