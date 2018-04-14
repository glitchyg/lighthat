from neopixel import Color, PColor

MODE_TEXT = 0
MODE_COLOR_WIPE = 1

TEXT_MODE_SOLID = 0

default_settings = {
    "text": "hello world",
    "text_bg_mode": TEXT_MODE_SOLID,
    "text_bg_color": PColor(0, 0, 0),
    "text_text_color": PColor(0, 255, 0),
    "text_scroll_speed": -0.5,
    "wipe_color": Color(0, 255, 0),
    "wipe_delay": 10,
    "mode": MODE_TEXT,
    "interrupt": False
}

modes = {
    "default2": {
        "text": "Works",
        "text_scroll_speed": -1,
        "text_text_color": 800
    },
    "default": {
        "text": "Hello World",
        "mode": MODE_TEXT,
        "text_bg_color": PColor(0, 0, 0),
        "text_text_color": PColor(0, 40, 25),
        "text_scroll_speed": -0.5
    },
    "penis": {
        "text": "penis",
        "mode": MODE_TEXT,
        "text_bg_color": PColor(0, 0, 0),
        "text_text_color": PColor(255, 255, 255),
        "text_scroll_speed": -2
    }
}

mode_playlist = ["default", "penis"]

current_mode = 0


def merge_two_dicts(x, y):
    x["text_text_color"] = PColor(90,0,255)

    # print(type(x["text_text_color"]))
    # z = x.copy()  # start with x's keys and values
    # z.update(y)  # modifies z with y's keys and values & returns None
    # print(type(z["text_text_color"]))
    return x


def start_mode(settings, mode):
    global modes
    mode_data = modes[mode]
    # print(mode_data)
    # print(mode, mode_data, settings)
    settings = merge_two_dicts(settings, mode_data)
    print(settings)
    return settings


def trigger_next_mode(settings):
    print("Next Mode")
    global current_mode, mode_playlist
    current_mode += 1
    if current_mode >= len(mode_playlist):
        current_mode = 0
    return start_mode(mode_playlist[current_mode])
