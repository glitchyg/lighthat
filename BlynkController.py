import BlynkLib
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG)

auth_token = 'e2c8b529c9574d5f9a732fe97d810b4a'

blynk = BlynkLib.Blynk(auth_token, server='192.168.43.80', port=8440, ssl=False)


def virtual_write_callback(value, pin, state, blynk_ref):
    print(value)
    # access the neccessary virtual output and write the value
    return


blynk.add_virtual_pin(pin=0, write=virtual_write_callback)

logging.getLogger().info("Running...")
blynk.run()
