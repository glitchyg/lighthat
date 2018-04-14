#!/usr/bin/env python3

import argparse
import thread
import time
import displaycontroller as hat_display
import webinterface as web
from neopixel import Color

MODE_TEXT = 0

TEXT_MODE_SOLID = 0

settings = {
    "text": "hello world",
    "text_bg_mode": TEXT_MODE_SOLID,
    "text_bg_color": (0, 0, 0),
    "text_text_color": (255, 0, 0),
    "text_scroll_speed": -1,
    "mode": MODE_TEXT,
    "interrupt": False
}


# Used to tell if we should early out of whatever we are doing
# This is used for when we are in a mode we want out of
def interrupted(settings):
    if settings["interrupt"]:
        settings["interrupt"] = False
        return True
    return False


def main_state_thread(settings):
    strip = hat_display.init_display_controller()

    run_counter = 0

    while True:
        mode = (settings["mode"])
        if mode == MODE_TEXT:
            scroll_pos = settings["text_scroll_speed"] * run_counter
            hat_display.show_text(strip, settings["text"], scroll_pos, True, settings["text_text_color"], settings["text_bg_color"])
            # time.sleep(0.0)


        run_counter += 1


# Main program logic follows:
if __name__ == '__main__':
    try:
        thread.start_new_thread(main_state_thread, (settings,))
        # thread.start_new_thread(web.web_interface_thread, (settings,))
    except:
        print "Error: unable to start thread"

    while 1:
        pass

    # # Process arguments
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    # args = parser.parse_args()
    #
    # print('Press Ctrl-C to quit.')
    # if not args.clear:
    #     print('Use "-c" argument to clear LEDs on exit')
    #
    # try:
    #
    #     while True:
    #         # hatDisplay.colorWipe(strip, Color(0, 0, 0), 0)
    #         for x in range(0, -1000, -1):
    #             hatDisplay.show_text(strip, "HELLO WORLD", x, True)
    #             time.sleep(0.05)
    #         # time.sleep(60)
    #         # print('Color wipe animations.')
    #         # colorWipe(strip, Color(255, 0, 0), 10)  # Red wipe
    #         # colorWipe(strip, Color(0, 255, 0), 10)  # Blue wipe
    #         # colorWipe(strip, Color(0, 0, 255), 10)  # Green wipe
    #         # print('Theater chase animations.')
    #         # hatDisplay.theaterChase(strip, Color(127, 127, 127))  # White theater chase
    #         # hatDisplay.theaterChase(strip, Color(127, 0, 0))  # Red theater chase
    #         # hatDisplay.theaterChase(strip, Color(0, 0, 127))  # Blue theater chase
    #         # print('Rainbow animations.')
    #         # hatDisplay.rainbow(strip)
    #         # hatDisplay.rainbowCycle(strip)
    #         # hatDisplay.theaterChaseRainbow(strip)
    #
    # except KeyboardInterrupt:
    #     if args.clear:
    #         hatDisplay.colorWipe(strip, Color(0, 0, 0), 10)
