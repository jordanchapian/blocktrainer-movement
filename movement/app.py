import connexion
from connexion.resolver import RestyResolver
from models.db import db, configureAppForDB


if __name__ == '__main__':
    connexionApp = connexion.App(__name__, specification_dir='swagger/')
    connexionApp.add_api('v1.yaml', resolver=RestyResolver('api.v1'))

    # Configure MongoEngine
    # app here is the Flask instance
    configureAppForDB(connexionApp.app)
    db.init_app(connexionApp.app)
    db.create_all(app=connexionApp.app)

    connexionApp.run(port=9090)
