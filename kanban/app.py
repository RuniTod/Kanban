from flask import Flask

from kanban.app import create_flask_app

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "<h1>Hello, World!<h1>"


if __name__ == '__main__':
    create_flask_app().run(host='0.0.0.0')
