#!/usr/bin/env python3

import argparse
import time
import displaycontroller as hatDisplay
from neopixel import Color

# Main program logic follows:
if __name__ == '__main__':

    strip = hatDisplay.init_display_controller()

    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            # hatDisplay.colorWipe(strip, Color(0, 0, 0), 0)
            for x in range(64):
                hatDisplay.show_text(strip, "HELLO WORLD", x, True)
                time.sleep(0.1)
            time.sleep(60)
            # print('Color wipe animations.')
            # colorWipe(strip, Color(255, 0, 0), 10)  # Red wipe
            # colorWipe(strip, Color(0, 255, 0), 10)  # Blue wipe
            # colorWipe(strip, Color(0, 0, 255), 10)  # Green wipe
            print('Theater chase animations.')
            hatDisplay.theaterChase(strip, Color(127, 127, 127))  # White theater chase
            hatDisplay.theaterChase(strip, Color(127, 0, 0))  # Red theater chase
            hatDisplay.theaterChase(strip, Color(0, 0, 127))  # Blue theater chase
            print('Rainbow animations.')
            hatDisplay.rainbow(strip)
            hatDisplay.rainbowCycle(strip)
            hatDisplay.theaterChaseRainbow(strip)

    except KeyboardInterrupt:
        if args.clear:
            hatDisplay.colorWipe(strip, Color(0, 0, 0), 10)
