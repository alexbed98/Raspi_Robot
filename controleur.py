# Alex Bedard & Jeremy Boucher
# Projet 3
# controleur.py
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import time

# Réglages de base
PCA_ADDR = 0x40
PWM_FREQ = 50  # 50 Hz pour servos
# Plage d'impulsions typique
MIN_US = 500
MAX_US = 2500

# coter gauche de l'hexapode est celui 
# quand la camera est vers nous
MONTER_G = 120
MONTER_D = 60
BAISSER = 90
AVANCER_G = 70
AVANCER_D = 110
RECULER_G = 110
RECULER_D = 70
AVANT_LARGE_D = 130
AVANT_LARGE_G = 50
ARRIERE_LARGE_D = 50
ARRIERE_LARGE_G = 130


class Controleur:
    
    def __init__(self):
        i2c = busio.I2C(SCL, SDA)
        pca = PCA9685(i2c, address=PCA_ADDR)
        pca.frequency = PWM_FREQ

        self.servos = []
        for ch in range(14):
            s = servo.Servo(pca.channels[ch],
                            min_pulse=MIN_US,
                            max_pulse=MAX_US,
                            actuation_range=180)

            self.servos.append(s)    

    # mouvements de camera
    def bouger_cam_plus(self, port):
        if self.servos[port].angle <= 175:
            self.servos[port].angle = self.servos[port].angle + 5

    def bouger_cam_moins(self, port):
        if self.servos[port].angle >= 5:
            self.servos[port].angle = self.servos[port].angle - 5

    # mouvements par triades
    def monter_triade_a(self):
        self.servos[1].angle = MONTER_D
        self.servos[5].angle = MONTER_D
        self.servos[9].angle = MONTER_G

    def avancer_triade_a(self):
        self.servos[0].angle = AVANCER_D
        self.servos[4].angle = AVANCER_D
        self.servos[8].angle = AVANCER_G

    def baisser_triade_a(self):
        self.servos[1].angle = BAISSER
        self.servos[5].angle = BAISSER
        self.servos[9].angle = BAISSER

    def reculer_triade_a(self):
        self.servos[0].angle = RECULER_D
        self.servos[4].angle = RECULER_D
        self.servos[8].angle = RECULER_G

    def monter_triade_b(self):
        self.servos[11].angle = MONTER_G
        self.servos[7].angle = MONTER_G
        self.servos[3].angle = MONTER_D

    def avancer_triade_b(self):
        self.servos[10].angle = AVANCER_G
        self.servos[6].angle = AVANCER_G
        self.servos[2].angle = AVANCER_D

    def baisser_triade_b(self):
        self.servos[11].angle = BAISSER
        self.servos[7].angle = BAISSER
        self.servos[3].angle = BAISSER

    def reculer_triade_b(self):
        self.servos[10].angle = RECULER_G
        self.servos[6].angle = RECULER_G
        self.servos[2].angle = RECULER_D

    # mouvement par côté
    def monter_cote_g(self):
        self.servos[7].angle = MONTER_G
        self.servos[9].angle = MONTER_G
        self.servos[11].angle = MONTER_G

    def monter_cote_d(self):
        self.servos[5].angle = MONTER_D
        self.servos[3].angle = MONTER_D
        self.servos[1].angle = MONTER_D

    def baisser_cote_g(self):
        self.servos[7].angle = BAISSER
        self.servos[9].angle = BAISSER
        self.servos[11].angle = BAISSER

    def baisser_cote_d(self):
        self.servos[5].angle = BAISSER
        self.servos[3].angle = BAISSER
        self.servos[1].angle = BAISSER
        
    def avancer_cote_g(self):
        self.servos[6].angle = AVANCER_G
        self.servos[8].angle = AVANCER_G
        self.servos[10].angle = AVANCER_G

    def avancer_cote_d(self):
        self.servos[4].angle = AVANCER_D
        self.servos[2].angle = AVANCER_D
        self.servos[0].angle = AVANCER_D

    def reculer_cote_g(self):
        self.servos[6].angle = RECULER_G
        self.servos[8].angle = RECULER_G
        self.servos[10].angle = RECULER_G

    def reculer_cote_d(self):
        self.servos[4].angle = RECULER_D
        self.servos[2].angle = RECULER_D
        self.servos[0].angle = RECULER_D

    def triade_a_tourner_droite(self):
        self.servos[0].angle = AVANT_LARGE_D
        self.servos[8].angle = AVANT_LARGE_D
        self.servos[4].angle = AVANT_LARGE_D

    def triade_b_tourner_droite(self):
        self.servos[10].angle = ARRIERE_LARGE_G
        self.servos[2].angle = ARRIERE_LARGE_G
        self.servos[6].angle = ARRIERE_LARGE_G

    def triade_a_tourner_gauche(self):
        self.servos[0].angle = AVANT_LARGE_G
        self.servos[8].angle = AVANT_LARGE_G
        self.servos[4].angle = AVANT_LARGE_G

    def triade_b_tourner_gauche(self):
        self.servos[10].angle = ARRIERE_LARGE_D
        self.servos[2].angle = ARRIERE_LARGE_D
        self.servos[6].angle = ARRIERE_LARGE_D