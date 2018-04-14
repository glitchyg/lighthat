#!/usr/bin/env python3

import argparse
import thread
import time
import displaycontroller as hat_display
import webinterface as web
import settingscontroller as sc


# Used to tell if we should early out of whatever we are doing
# This is used for when we are in a mode we want out of
def interrupted(settings):
    if settings["interrupt"]:
        settings["interrupt"] = False
        return True
    return False


def main_state_thread(settings):
    strip = hat_display.init_display_controller()

    settings = sc.start_mode(settings, "default2")

    print(settings)

    run_counter = 0

    while True:
        mode = (settings["mode"])
        if mode == sc.MODE_TEXT:
            # print("a")
            scroll_pos = settings["text_scroll_speed"] * run_counter
            hat_display.show_text(strip, settings["text"], scroll_pos, True, settings["text_text_color"],
                                  settings["text_bg_color"])
            time.sleep(50 / 1000)
        elif mode == sc.MODE_COLOR_WIPE:
            # print("b")
            finished = hat_display.colorWipe(strip, run_counter, settings["wipe_color"], settings["wipe_delay"])
            if finished:
                settings = sc.trigger_next_mode(settings)

        run_counter += 1


# Main program logic follows:
if __name__ == '__main__':
    try:
        thread.start_new_thread(main_state_thread, (sc.default_settings,))
        # thread.start_new_thread(web.web_interface_thread, (settings,))
    except:
        print "Error: unable to start thread"

    while 1:
        pass
