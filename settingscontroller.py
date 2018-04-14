from neopixel import Color, PColor

MODE_TEXT = 0
MODE_COLOR_WIPE = 1
MODE_CHASE = 2
MODE_TEXT_AND_CHASE = 3

TEXT_MODE_SOLID = 0

default_settings = {
    "text": "hello world",
    "text_bg_mode": TEXT_MODE_SOLID,
    "text_bg_color": (0, 0, 0),
    "text_text_color": (0, 255, 0),
    "text_scroll_speed": -0.5,
    "text_start_offset": 0,
    "wipe_color": Color(0, 255, 0),
    "wipe_delay": 10,
    "chase_color": Color(0, 255, 0),
    "chase_delay": 20,
    "mode": MODE_TEXT,
    "interrupt": False
}

modes = {
    "default": {
        "mode": MODE_TEXT,
        "text": "WORKS",
        "text_bg_color": (0, 0, 0),
        "text_text_color": (0, 0, 255),
        "text_scroll_speed": -0.5
    },
    "penis": {
        "mode": MODE_TEXT,
        "text": "PENIS",
        "text_bg_color": (0, 0, 0),
        "text_text_color": (255, 255, 255),
        "text_start_offset": 23,
        "text_scroll_speed": 0
    },
    "wipe": {
        "mode": MODE_COLOR_WIPE,
        "wipe_color": Color(0, 255, 0),
        "wipe_delay": 1,
    },
    "chase": {
        "mode": MODE_CHASE,
        "chase_color": Color(255, 0, 0),  # G, R, B
        "chase_delay": 20,
    },
    "text_and_chase": {
        "mode": MODE_TEXT_AND_CHASE
    }

}

mode_playlist = ["default", "penis", "wipe"]

current_mode = 0


def merge_two_dicts(current, new):
    updated = current.copy()  # start with x's keys and values
    updated.update(new)  # modifies z with y's keys and values & returns None

    # Uhhg, some kind of bug. Have to do this shit to get around it
    if "text_text_color" in new:
        ttc = new["text_text_color"]
        updated["text_text_color"] = PColor(ttc[0], ttc[1], ttc[2])

    if "text_bg_color" in new:
        tbc = new["text_bg_color"]
        updated["text_bg_color"] = PColor(tbc[0], tbc[1], tbc[2])

    return updated


def start_mode(settings, mode):
    global modes
    mode_data = modes[mode]
    # print(mode_data)
    # print(mode, mode_data, settings)
    settings = merge_two_dicts(settings, mode_data)
    # print(settings)
    return settings


def trigger_next_mode(settings):
    print("Next Mode")
    global current_mode, mode_playlist
    current_mode += 1
    if current_mode >= len(mode_playlist):
        current_mode = 0
    print("Loaded Mode: " + mode_playlist[current_mode])
    return start_mode(settings, mode_playlist[current_mode])
