import BlynkLib
import time
import logging

logging.basicConfig(level=logging.DEBUG)

auth_token = 'e2c8b529c9574d5f9a732fe97d810b4a'


def virtual_write_callback(value, pin, state, blynk_ref):
    print(value)
    # access the neccessary virtual output and write the value
    return


def now_in_ms():
    millis = int(round(time.time() * 1000))
    return millis


def init_blynk():
    blynk = BlynkLib.Blynk(auth_token, server='192.168.4.1', port=8440, ssl=False)
    blynk.add_virtual_pin(pin=0, write=virtual_write_callback)
    return blynk



if __name__ == '__main__':
    blynk = init_blynk()
    while True:
        blynk.run()
