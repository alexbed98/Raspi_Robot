from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import numpy as np
import cv2
from picamera2 import Picamera2
from camera import Camera
import time
from robot import Robot
from hexapode import Hexapode
from voiture import Voiture
from controleur import Controleur
from enum import Enum
from encodeur import Encodeur

class Model(Enum):
    HEXAPODE = 0
    VOITURE = 1

# les ports a envoyer aux constructeurs
class Ports:
    # les ports pour les moteurs
    IN1 = 6
    IN2 = 5
    IN3 = 15
    IN4 = 14
    ENA = 13
    ENB = 18

    # les ports pour les capteurs infrarouges
    IRG = 23
    IRD = 24

time_sleep = 0.1
vitesse_voiture = 0.5
type_robot = None

def get_pi_model():
    try:
        with open("/proc/device-tree/model", "r") as f:
            return f.read().strip("\x00").strip()
    except FileNotFoundError:
        return None

model = get_pi_model()
print(model)

if model and "Pi 3" in model:
    print('Bienvenue, hexapode')
    robot = Hexapode()
    type_robot = Model.HEXAPODE

elif model and "Pi Zero" in model:
    print('Bienvenue, robotmobile')
    robot = Voiture(Ports.IN1, Ports.IN2, Ports.IN3, Ports.IN4, Ports.ENA, Ports.ENB)
    type_robot = Model.VOITURE
else:
    print('modele de robot introuvable')
    exit()

hexapode = type_robot == Model.HEXAPODE

if not hexapode:
    encodeur = Encodeur(27)

time.sleep(0.1)
key = cv2.waitKeyEx(30)

while not key == ord('x'):
    yuv = robot.camera.capture()  
    img = cv2.cvtColor(yuv, cv2.COLOR_YUV2RGB_I420)
    cv2.imshow("Robot", img)
    key = cv2.waitKeyEx(30)

    #bouger robot Hexapode
    if key == ord('w'):
        robot.avancer(time_sleep, vitesse_voiture)
        if hexapode:
            robot.led.allumer_avancer()

    elif key == ord('a'):
        robot.tourner_gauche(time_sleep, vitesse_voiture)
        if hexapode:
            robot.led.allumer_tourner_gauche()

    elif key == ord('d'):
        robot.tourner_droite(time_sleep, vitesse_voiture)
        if hexapode:
            robot.led.allumer_tourner_droite()

    elif key == ord('s'):
        robot.reculer(time_sleep, vitesse_voiture)
        if hexapode:
            robot.led.allumer_reculer()

    # petite danse
        elif key == ord('p'):
            robot.danser(time_sleep)

    # bouger camera
    if hexapode:
        if key == ord('j'):
            robot.camera_gauche()

        elif key == ord('i'):
            robot.camera_haut()

        elif key == ord('l'):
            robot.camera_droite()

        elif key == ord('k'):
            robot.camera_bas()

    # if not hexapode:
    #   encodeur.capter_rotation()
    #   encodeur.obtenir_distance()
    
    else:
        if not hexapode:
            robot.arreter()

if hexapode:
    robot.led.eteindre_tous()
cv2.waitKey(1)
cv2.destroyAllWindows()
robot.calibrer()

print("Au revoir!")