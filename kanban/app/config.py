import os
import configparser

from flask_sqlalchemy import SQLAlchemy

config = configparser.ConfigParser()
POSTGRES_CONF = {
    "SQLALCHEMY_DATABASE_URI": "postgresql+psycopg2://admin:123@localhost/kanban",
}
db = SQLAlchemy()


def init_config(path):
    config.optionxform = str
    config.read(path)
