# Alex Bedard & Jeremy Boucher
# Projet 3
# hexapode.py
from robot import Robot
from controleur import Controleur
from controleur_led import ControleurLed
from camera import Camera
import time

time_sleep_camera = 0.5
time_sleep_calibrage = 0.001

class Hexapode(Robot):

    def __init__(self):
        self.controleur = Controleur()
        self.led = ControleurLed()
        self.camera = Camera()
        self.calibrer()

    def calibrer(self):
        print('calibrage')
        for s in self.controleur.servos:
            s.angle = 90
            time.sleep(time_sleep_calibrage)

    def camera_haut(self):
        self.controleur.bouger_cam_plus(13)
        time.sleep(time_sleep_camera)

    def camera_gauche(self):
        self.controleur.bouger_cam_plus(12)
        time.sleep(time_sleep_camera)

    def camera_bas(self):
        self.controleur.bouger_cam_moins(13)
        time.sleep(time_sleep_camera)

    def camera_droite(self):
        self.controleur.bouger_cam_moins(12)
        time.sleep(time_sleep_camera)
    
    def avancer(self, time_sleep, vitesse):
        print('avancer')
        self.controleur.monter_triade_a()
        self.controleur.baisser_triade_b()
        time.sleep(time_sleep)
        self.controleur.avancer_triade_a()
        self.controleur.reculer_triade_b()
        time.sleep(time_sleep)
        self.controleur.baisser_triade_a()
        self.controleur.monter_triade_b()
        time.sleep(time_sleep)
        self.controleur.reculer_triade_a()
        self.controleur.avancer_triade_b()
        time.sleep(time_sleep)

    def reculer(self, time_sleep, vitesse):
        print('reculer')
        self.controleur.monter_triade_a()
        self.controleur.baisser_triade_b()
        time.sleep(time_sleep)
        self.controleur.reculer_triade_a()
        self.controleur.avancer_triade_b()
        time.sleep(time_sleep)
        self.controleur.baisser_triade_a()
        self.controleur.monter_triade_b()
        time.sleep(time_sleep)
        self.controleur.avancer_triade_a()
        self.controleur.reculer_triade_b()
        time.sleep(time_sleep)

    def danser(self, time_sleep):
        print('tourner a gauche')
        self.controleur.monter_cote_g()
        self.controleur.baisser_cote_d()
        time.sleep(time_sleep)
        self.controleur.avancer_cote_g()
        self.controleur.reculer_cote_d()
        time.sleep(time_sleep)
        self.controleur.baisser_cote_g()
        self.controleur.monter_cote_d()
        time.sleep(time_sleep)
        self.controleur.reculer_cote_g()
        self.controleur.avancer_cote_d()
        time.sleep(time_sleep)

    def tourner_droite(self, time_sleep, vitesse):
        print('tourner a droite')
        self.calibrer()
        self.controleur.monter_triade_b()
        time.sleep(time_sleep)
        self.controleur.triade_b_tourner_droite()
        time.sleep(time_sleep)
        self.controleur.baisser_triade_b()
        time.sleep(time_sleep)
        self.controleur.monter_triade_a()
        time.sleep(time_sleep)
        self.controleur.triade_a_tourner_droite()
        time.sleep(time_sleep)
        self.controleur.baisser_triade_a()
        time.sleep(time_sleep)
        self.controleur.avancer_cote_d()
        time.sleep(time_sleep)
        self.controleur.reculer_cote_g()
        time.sleep(time_sleep)

    def tourner_gauche(self, time_sleep, vitesse):
        print('tourner a gauche')
        self.calibrer()
        self.controleur.monter_triade_a()
        time.sleep(time_sleep)
        self.controleur.triade_a_tourner_gauche()
        time.sleep(time_sleep)
        self.controleur.baisser_triade_a()
        time.sleep(time_sleep)
        self.controleur.monter_triade_b()
        time.sleep(time_sleep)
        self.controleur.triade_b_tourner_gauche()
        time.sleep(time_sleep)
        self.controleur.baisser_triade_b()
        time.sleep(time_sleep)
        self.controleur.avancer_cote_g()
        time.sleep(time_sleep)
        self.controleur.reculer_cote_d()
        time.sleep(time_sleep)


