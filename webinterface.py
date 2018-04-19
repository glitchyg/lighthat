from flask import Flask
import settingscontroller as sc

app = Flask(__name__)

strip = None
needs_settings_update = False
settings_to_update = {}


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/test")
def hello():
    settings = {"text": "O YEA"}
    set_settings_update(settings)
    return "Test Set"


@app.route('/bright/<int:brightness>')
def set_brightness(brightness):
    strip.setBrightness(brightness)
    return "Brightness set to: " + str(brightness)


def web_interface_thread(settings, input_strip):
    global strip
    strip = input_strip
    app.run(host='0.0.0.0')


def set_settings_update(new_settings):
    global settings_to_update, needs_settings_update
    settings_to_update = new_settings


def get_settings_update():
    global settings_to_update, needs_settings_update
    if needs_settings_update:
        settings_to_update = False
        return settings_to_update
    return None
