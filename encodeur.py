# Alex Bedard & Jeremy Boucher
# Projet 03
# encodeur.py
import RPi.GPIO as GPIO
import time

# encodeur gauche port 27
# encodeur droit port 22

circ = 207 #milimetres
statesPerRotation = 40
distancePerStep = circ / statesPerRotation

class Encodeur:

    def __init__(self, port):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        self.stateLast = GPIO.input(27)
        self.rotationCount = 0
        self.stateCount = 0
        self.stateCountTotal = 0

    def capter_rotation(self):
        stateCurrent = GPIO.input(27)
        if stateCurrent != self.stateLast:
            self.stateLast = stateCurrent
            self.stateCount += 1
            self.stateCountTotal += 1
        if self.stateCount == statesPerRotation:
            self.rotationCount += 1
            self.stateCount = 0

    def obtenir_distance(self):
        return distancePerStep * self.stateCountTotal