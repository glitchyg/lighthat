from flask import Flask

app = Flask(__name__)

strip = None


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/bright/<int:brightness>')
def set_brightness(brightness):
    strip.setBrightness(60)
    return "Brightness set to: " + brightness


def web_interface_thread(settings, input_strip):
    global strip
    strip = input_strip
    app.run(host='0.0.0.0')
