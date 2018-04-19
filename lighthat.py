#!/usr/bin/env python3

import RPi.GPIO as GPIO
import argparse
import thread
import time
import displaycontroller as hat_display
import webinterface as web
import settingscontroller as sc
from neopixel import Color

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
    print("State Thread Started")
    strip = hat_display.init_display_controller()

    thread.start_new_thread(web.web_interface_thread, (settings, strip))

    settings = sc.start_mode(settings, "kimbra")
    run_counter = 0
    last_mode_button_state = False
    hat_display.fill(strip, 0)
    strip.show()
    total_delay = 0;

    while True:
        mode = (settings["mode"])
        total_delay = 50

        #  --------  ADDONS --------
        if settings["rainbow_show"]:
            speed = settings["rainbow_speed"]
            hat_display.rainbow(strip, run_counter, speed)
        if settings["gradient_show"]:
            speed = settings["gradient_speed"]
            color_from = settings["gradient_color_from"]
            color_to = settings["gradient_color_to"]
            hat_display.gradient(strip, run_counter, speed, color_from, color_to)

        #  --------  MODE TEXT AND CHASE --------
        if mode == sc.MODE_TEXT_AND_CHASE:
            hat_display.fill(strip, 0)

        # --------  MODE CHASE --------
        if mode == sc.MODE_CHASE or mode == sc.MODE_TEXT_AND_CHASE:
            hat_display.fill(strip, 0)
            hat_display.theaterChase(strip, run_counter, settings["chase_color"], 50)
            if settings["chase_show_strip"]:
                strip.show()
            total_delay += settings["chase_delay"]

        #  --------  MODE TEXT --------
        if mode == sc.MODE_TEXT or mode == sc.MODE_TEXT_AND_CHASE:
            scroll_pos = settings["text_scroll_speed"] * run_counter
            if scroll_pos == 0:
                scroll_pos = settings["text_start_offset"]
            mask = settings["text_mask"]
            if not mask:
                hat_display.fill(strip, 0)
            hat_display.show_text(strip, settings["text"], scroll_pos, True, int(settings["text_text_color"]),
                                  settings["text_bg_color"], mask)
            if settings["text_show_strip"]:
                strip.show()
            # time.sleep(50 / 1000)

        #  --------  MODE WIPE --------
        if mode == sc.MODE_COLOR_WIPE:
            finished = hat_display.colorWipe(strip, run_counter, settings["wipe_color"], settings["wipe_delay"])
            if finished:
                run_counter = 0
                hat_display.fill(strip, 0)
                strip.show()
                settings = sc.trigger_next_mode(settings)

        #  --------  MODE IMAGE --------
        if mode == sc.MODE_IMAGE or settings["image_show"]:
            mask = settings["image_mask"]
            hat_display.show_image(strip, settings["image_file"], mask)
            if settings["image_show_strip"]:
                strip.show()

        # Take all the time we wanted to delay and do it at the end
        time.sleep(total_delay / 1000.0)

        run_counter += 1

        # Check for mode change
        input_state = GPIO.input(16)
        if input_state == False and last_mode_button_state == True:
            print("Button Pushed")
            run_counter = 0
            hat_display.fill(strip, 0)
            settings = sc.reset_settings(settings)
            settings = sc.trigger_next_mode(settings)

            # Check if we entered the mode to show text file
            if sc.is_custom_text_mode():
                content = "Failed"
                with open("custom_text.txt") as f:
                    content = f.readline()
                settings["text"] = content

        web_settings = web.get_settings_update()
        print(web_settings)
        if web_settings is not None:
            print("Updating settings from web")
            settings = sc.merge_two_dicts(settings, web_settings)

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
