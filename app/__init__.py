import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_smorest import Api

from app.celery_app import make_celery

# -------- Extensions -------- #
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
jwt = JWTManager()


def create_app():

    flask_app = Flask(__name__)

    # -------- ENV-based DB selection -------- #
    env = os.getenv("APP_ENV", "develop")

    if env == "master":
        db_uri = "sqlite:///test_master.db"
    else:
        db_uri = "sqlite:///test_develop.db"

    # -------- Config -------- #
    flask_app.config.from_mapping(
        SECRET_KEY='supersecretkey',
        SQLALCHEMY_DATABASE_URI=db_uri,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        JWT_SECRET_KEY='super-secret-jwt-key',

        # Swagger / OpenAPI
        API_TITLE="Task Manager API",
        API_VERSION="v1",
        OPENAPI_VERSION="3.0.3",
        OPENAPI_JSON_PATH="openapi.json",
        OPENAPI_URL_PREFIX="/api/docs",
        OPENAPI_SWAGGER_UI_PATH="/swagger-ui",
        OPENAPI_SWAGGER_UI_URL="https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

    # -------- Initialize extensions -------- #
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)
    login_manager.init_app(flask_app)
    jwt.init_app(flask_app)

    # Celery
    celery = make_celery(flask_app)
    flask_app.celery = celery

    login_manager.login_view = 'login'

    # -------- Models (IMPORTANT: import after app init) -------- #
    with flask_app.app_context():
        from app.models import User

        @login_manager.user_loader
        def load_user(user_id):
            return db.session.get(User, int(user_id))

    # -------- Blueprints / API -------- #
    from app.blueprints import user_blp, task_blp
    import app.routes

    api = Api(flask_app)
    api.register_blueprint(user_blp)
    api.register_blueprint(task_blp)

    # -------- Error Handlers -------- #
    @flask_app.errorhandler(400)
    def bad_request(e):
        return {"error": "Bad Request"}, 400

    @flask_app.errorhandler(404)
    def not_found(e):
        return {"error": "Not Found"}, 404

    @flask_app.errorhandler(500)
    def server_error(e):
        return {"error": "Internal Server Error"}, 500

    return flask_app