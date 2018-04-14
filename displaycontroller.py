#!/usr/bin/env python3


import time
from neopixel import *
from PIL import Image
import textcontroller as tc
import argparse
import math

# LED strip configuration:
LED_COUNT = 512  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 20  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

HAT_WIDTH = 64
HAT_HEIGHT = 8

pixelIndexes = []


def setupCorrectedPixelIndex():
    def pushIt(start, end):
        if start > end:
            for i in range(start, end - 1, -1):
                pixelIndexes.append(i)
        else:
            for i in range(start, end + 1):
                pixelIndexes.append(i)

    pushIt(0, 31)
    pushIt(480, 511)
    pushIt(63, 32)
    pushIt(479, 448)
    pushIt(64, 95)
    pushIt(416, 447)
    pushIt(127, 96)
    pushIt(415, 384)
    pushIt(128, 159)
    pushIt(352, 383)
    pushIt(191, 160)
    pushIt(351, 320)
    pushIt(192, 223)
    pushIt(288, 319)
    pushIt(255, 224)
    pushIt(287, 256)


def getCorrectedPixelIndex(i):
    if i >= len(pixelIndexes):
        return pixelIndexes[len(pixelIndexes) - 1]
    else:
        return pixelIndexes[i]


# Define functions which animate LEDs in various ways.
def colorWipe(strip, run_counter, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    total_pixels = strip.numPixels()
    i = run_counter % total_pixels
    # for i in range(strip.numPixels()):
    strip.setPixelColor(getCorrectedPixelIndex(i), color)
    strip.show()
    time.sleep(wait_ms / 1000.0)
    if i == (total_pixels - 1):
        return True
    return False


# Define functions which animate LEDs in various ways.
def fill(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    # strip.show()


def theaterChase(strip, run_counter, color, wait_ms=50):
    for q in range(3):
        for i in range(0, strip.numPixels(), 3):
            strip.setPixelColor(getCorrectedPixelIndex(i + q), color)
        strip.show()
        time.sleep(wait_ms / 1000.0)
        for i in range(0, strip.numPixels(), 3):
            strip.setPixelColor(getCorrectedPixelIndex(i + q), 0)


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(getCorrectedPixelIndex(i), wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(getCorrectedPixelIndex(i), wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(getCorrectedPixelIndex(i + q), wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(getCorrectedPixelIndex(i + q), 0)


def show_rgb_image(strip, rgb_img, mask=False):
    i = 0
    for y in range(HAT_HEIGHT):
        for x in range(HAT_WIDTH):
            r, g, b = rgb_img.getpixel((x, y))
            if not mask or ((r + g + b) > 0):
                strip.setPixelColor(getCorrectedPixelIndex(i), Color(g, r, b))  #G, R, B
            i += 1


def show_text(strip, text, offset, wrap, text_color, bg_color, mask=False):
    rgb_img = tc.get_text_image(text, HAT_WIDTH, HAT_HEIGHT, offset, wrap, False, text_color, bg_color)
    show_rgb_image(strip, rgb_img, mask)


def show_simple_text(strip, text):
    rgb_img = tc.get_text_image(text, HAT_WIDTH, HAT_HEIGHT)
    show_rgb_image(strip, rgb_img)


def init_display_controller():
    # Setup all the pixels to be corrected for the orientation on the hat
    setupCorrectedPixelIndex()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

    # Initialize the library (must be called once before other functions).
    strip.begin()

    return strip
