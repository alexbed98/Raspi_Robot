# Alex Bedard & Jeremy Boucher
# Projet 03
# moteur.py
from gpiozero import DigitalOutputDevice, DigitalInputDevice, PWMOutputDevice
import time

TEMPS = 0.01

class Moteur:
    def __init__(self, IN1, IN2, ENA):
        self.IN1 = DigitalOutputDevice(IN1)
        self.IN2 = DigitalOutputDevice(IN2)
        self.ENA = PWMOutputDevice(ENA)
        time.sleep(TEMPS)

    def avant(self, vitesse):
        self.ENA.value = vitesse
        self.IN1.on()
        self.IN2.off()

    def arriere(self, vitesse):
        self.ENA.value = vitesse
        self.IN1.off()
        self.IN2.on()

    def arret(self):
        self.ENA.value = 0
        self.IN1.on()
        self.IN2.on()


