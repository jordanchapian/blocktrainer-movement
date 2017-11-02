import connexion
from connexion.resolver import RestyResolver
from models.connection import db

if __name__ == '__main__':
    connexionApp = connexion.App(__name__, specification_dir='swagger/')
    connexionApp.add_api('v1.yaml', resolver=RestyResolver('api.v1'))

    connexionApp.app.config.update(
        SECRET_KEY='btMovement',
        MONGODB_DB='btMovement',
        MONGODB_HOST='mongodb'
    )

    db.init_app(connexionApp.app)
    connexionApp.run(port=9090, debug=True)

