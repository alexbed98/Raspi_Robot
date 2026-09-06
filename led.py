# Alex Bedard & Jeremy Boucher
# Projet 3
# led.py
from rpi_ws281x import PixelStrip, Color
from gpiozero import DigitalOuputDevice


class ControleurLed:
    def __init__(self, count=16, pin=12, brightness=255):
        self.strip = PixelStrip(
            count, pin, 800000, 10, False, brightness, 0
        )
        self.strip.begin()
        

    def allumer_avancer(self):
        pass

    def allumer_reculer(self):
        pass

    def allumer_tous(self, r, g, b):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(r, g, b))
        self.strip.show()

    def eteindre_tous(self):
        self.set_all(0, 0, 0)