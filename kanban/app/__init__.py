import os

from flask import Flask

from app.base_model import Base
from app.create_engine import engine
from app.routes import route
from app.config import config, init_config, POSTGRES_CONF, db


def create_flask_app():
    app = Flask(__name__)
    app.config.update(POSTGRES_CONF)
    db.init_app(app)
    route(app)
    path = os.environ.get('CONFIG_PATH', "./settings.ini")
    init_config(path)
    try:
        app.config.update(dict(
            SECRET_KEY=str(config['FLASK_APP']['FLASK_APP_SECRET_KEY'])
        ))
        print(f"\n\033[32m Сервер запустился с конфигом:\n\033[32m {path}\n")
    except KeyError:
        print(f"\033[31m Файл {path} не найден или неверный")
    return app
