#Jérémy Boucher & Alex Bédard
from rpi_ws281x import PixelStrip, Color
from gpiozero import DigitalOutputDevice


class ControleurLed:
    def __init__(self, count=16, pin=12, brightness=255):
        self.strip = PixelStrip(
            count, pin, 800000, 10, False, brightness, 0
        )
        self.strip.begin()

    def allumer_avancer(self): #bleu
        self.allumer_tous(0, 0, 255)

    def allumer_reculer(self): #vert
        self.allumer_tous(0, 255, 0)

    def allumer_tourner_gauche(self): #red
        self.allumer_tous(255, 0, 0)

    def allumer_tourner_droite(self):
        self.allumer_tous(150, 150, 150)

    def allumer_tous(self, r, g, b):
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, Color(r, g, b))
        self.strip.show()

    def eteindre_tous(self):
        self.allumer_tous(0, 0, 0)