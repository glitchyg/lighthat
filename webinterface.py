from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


def web_interface_thread(settings):
    app.run()
