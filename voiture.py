# Alex Bedard & Jeremy Boucher
# Projet 3
# voiture.py
from robot import Robot
from camera import Camera
from gpiozero import DigitalOutputDevice, DigitalInputDevice, PWMOutputDevice
from moteur import Moteur
import time

TEMPS_ROTATION = 0.04
TEMPS_DELAI = 0.3
TEMPS = 0.01

class Voiture(Robot):

    def __init__(self, IN1, IN2, IN3, IN4, ENA, ENB):
        self.camera = Camera()
        self.moteurGauche = Moteur(IN1, IN2, ENA)
        self.moteurDroite = Moteur(IN3, IN4, ENB)

    def avancer(self, time_sleep, vitesse):
        self.moteurGauche.avant(vitesse)
        self.moteurDroite.avant(vitesse)
        time.sleep(TEMPS)

    def reculer(self, time_sleep, vitesse):
        self.moteurGauche.arriere(vitesse)
        self.moteurDroite.arriere(vitesse)
        time.sleep(TEMPS)

        
    def tourner_gauche(self, time_sleep, vitesse):
        self.moteurGauche.arriere(vitesse)
        self.moteurDroite.avant(vitesse)
        time.sleep(TEMPS)

    def tourner_droite(self, time_sleep, vitesse):
        self.moteurGauche.avant(vitesse)
        self.moteurDroite.arriere(vitesse)
        time.sleep(TEMPS)

    def arreter(self):
        self.moteurGauche.arret()
        self.moteurDroite.arret() 
     