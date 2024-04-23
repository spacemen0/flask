from flask import Flask
from flask.helpers import hello_word

app = Flask(__name__)


@app.route("/")
def hello():
    return hello_word()


if __name__ == "__main__":
    app.run()
