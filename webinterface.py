from flask import Flask

app = Flask(__name__)

strip = None

@app.route("/")
def hello():
    strip.setBrightness(60)
    return "Hello World!"


def web_interface_thread(settings, input_strip):
    global strip
    strip = input_strip
    app.run(host='0.0.0.0')
