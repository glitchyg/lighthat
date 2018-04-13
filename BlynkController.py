import BlynkLib
import time
import logging

logging.basicConfig(level=logging.DEBUG)

auth_token = '8827f3156d054ed4b9eb899e8ad9c17f'

def virtual_write_callback(value, pin, state, blynk_ref):
    print(value)
    # access the neccessary virtual output and write the value
    return


def now_in_ms():
    millis = int(round(time.time() * 1000))
    return millis


def init_blynk():
    blynk = BlynkLib.Blynk(auth_token)
    blynk.add_virtual_pin(pin=0, write=virtual_write_callback)
    return blynk


def blinkay(blynk, delay):
    start = now_in_ms()
    end = start + delay
    while now_in_ms() < end:
        # Do Nothing
        blynk.stride()
