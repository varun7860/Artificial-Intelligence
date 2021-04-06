'''
About the project
-----------------
- This is a simple project for playing Dino T-rex game with gestures. The gestures used in
  this project are not of hand but of coloured object in the image. In this project I used
  Red colour colour object to control/play the game. You can use your own coloured object to
  control the game if you want. To autopress the keys on your laptop a library called pyautogui
  is used.
  
How to play T-Rex game(Controls):
---------------------------------
- To JUMP : Moving the coloured object up in the image.
'''

import cv2
import numpy as np
import pygame
import pyautogui as gui

class GestureRecognizer(object):
    
    def __init__(self):
        self.CX = 0
        self.CY = 0

        self.image = None
        self.hsv = None
        self.binary = None
        self.output = None
        self.moment = None

        self.min = np.array([0, 100, 100])
        self.max = np.array([20, 255, 255])

        self.cap = cv2.VideoCapture(0)

    def extract_image(self): 
        _, self.image = self.cap.read()

    def convert_hsv(self):
        self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

    def remove_noise(self):
        self.hsv = cv2.medianBlur(self.hsv, 3)

    def remove_background(self):
        self.output = cv2.bitwise_and(self.image, self.image, mask = self.binary)

    def convert_binary(self):
        self.binary = cv2.inRange(self.hsv, self.min, self.max)

    def detect_position(self):
        self.moment = cv2.moments(self.binary)
        
        self.CX = int(self.moment["m10"]/self.moment["m00"])
        self.CY = int(self.moment["m01"]/self.moment["m00"])

        cv2.circle(self.output, (self.CX,self.CY), 3, (255,0,0), -1)

    def recognize_gesture(self):

        if self.CX < 210:
            print("Left")

        elif self.CX > 400:
            print("Right")

        elif self.CY < 120:
            print("Up")
            gui.press('up')

        elif self.CY > 340:
            print("Down")

    def detect_pointer(self):
        contours, _ = cv2.findContours(self.binary.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour = max(contours, key = cv2.contourArea)
        x, y , w, h = cv2.boundingRect(contour)
        cv2.rectangle(self.image, (x,y), (x+w, y+h), (0,0,255),2)

    def begin(self):

        while True:
           self.extract_image()

           self.convert_hsv()

           self.remove_noise()

           self.convert_binary()

           self.detect_pointer()

           self.detect_position()

           self.recognize_gesture()

           self.show_image()

           if cv2.waitKey(1) & 0xFF == ord('q'):
               break

        self.cap.release()
        cv2.destroyAllWindows()

    def show_image(self):
        cv2.imshow("Output Image", self.image)           

    def __del__(self):
        print("Object deleted")

def main():

    #Make the Class object.
    recognizer = GestureRecognizer()

    #Start detecting Gestures.
    recognizer.begin()    


if __name__ == '__main__':
    main()

