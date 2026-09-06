# Alex Bedard & Jeremy Boucher
# Projet 3
# robot.py
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo
import numpy as np
import cv2
from abc import ABC, abstractmethod

class Robot(ABC):  

    @abstractmethod
    def avancer(self, time_sleep, vitesse):
        pass

    @abstractmethod
    def reculer(self, time_sleep, vitesse):
        pass

    @abstractmethod
    def tourner_droite(self, time_sleep, vitesse):
        pass

    @abstractmethod
    def tourner_gauche(self, time_sleep, vitesse):
        pass