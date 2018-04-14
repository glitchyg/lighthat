#!/usr/bin/env python3

import RPi.GPIO as GPIO
import argparse
import thread
import time
import displaycontroller as hat_display
import webinterface as web
import settingscontroller as sc

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Used to tell if we should early out of whatever we are doing
# This is used for when we are in a mode we want out of
def interrupted(settings):
    if settings["interrupt"]:
        settings["interrupt"] = False
        return True
    return False


def main_state_thread(settings):
    strip = hat_display.init_display_controller()
    settings = sc.start_mode(settings, "text_and_chase")
    run_counter = 0
    last_mode_button_state = False
    hat_display.fill(strip, 0)
    strip.show()

    while True:
        mode = (settings["chase"])

        #  --------  MODE TEXT AND CHASE --------
        if mode == sc.MODE_TEXT_AND_CHASE:
            hat_display.fill(strip, 0)

        # --------  MODE CHASE --------
        if mode == sc.MODE_CHASE or mode == sc.MODE_TEXT_AND_CHASE:
            hat_display.theaterChase(strip, run_counter, settings["chase_color"], settings["chase_delay"])
            if settings["chase_show_strip"]:
                strip.show()

        #  --------  MODE TEXT --------
        # if mode == sc.MODE_TEXT or mode == sc.MODE_TEXT_AND_CHASE:
        #     scroll_pos = settings["text_scroll_speed"] * run_counter
        #     if scroll_pos == 0:
        #         scroll_pos = settings["text_start_offset"]
        #     mask = (mode == sc.MODE_TEXT_AND_CHASE)
        #     hat_display.show_text(strip, settings["text"], scroll_pos, True, int(settings["text_text_color"]),
        #                           settings["text_bg_color"], True)
        #     if settings["text_show_strip"]:
        #         strip.show()
        #     time.sleep(50 / 1000)

        #  --------  MODE WIPE --------
        if mode == sc.MODE_COLOR_WIPE:
            finished = hat_display.colorWipe(strip, run_counter, settings["wipe_color"], settings["wipe_delay"])
            if finished:
                run_counter = 0
                hat_display.fill(strip, 0)
                strip.show()
                settings = sc.trigger_next_mode(settings)



        run_counter += 1

        # Check for mode change
        input_state = GPIO.input(16)
        if input_state == False and last_mode_button_state == True:
            print("Button Pushed")
            run_counter = 0
            hat_display.fill(strip, 0)
            settings = sc.trigger_next_mode(settings)

        last_mode_button_state = input_state


# Main program logic follows:
if __name__ == '__main__':
    try:
        thread.start_new_thread(main_state_thread, (sc.default_settings,))
        # thread.start_new_thread(web.web_interface_thread, (settings,))
    except:
        print "Error: unable to start thread"

    while 1:
        pass
