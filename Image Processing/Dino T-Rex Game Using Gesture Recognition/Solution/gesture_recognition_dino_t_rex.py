'''
About the project
-----------------
- This is a simple project for playing Dino T-rex game with gestures. The gestures used in
  this project are not of hand but of coloured object in the image. In this project I used
  Red colour coloured object to control/play the game. You can use your own coloured object to
  control the game if you want. To autopress the keys on your laptop a library called pyautogui
  is used.
  
How to play T-Rex game(Controls):
---------------------------------
- To JUMP : Moving the coloured object up in the image.

Author of this Project
----------------------
- Varun Ajay Walimbe
'''

import cv2
import numpy as np
import pygame
import pyautogui as gui

class GestureRecognizer(object):
    '''
    Description
    -----------
    - This class will be used for detecting where the object(x,y)
      lies in the image and then convert them into appropriate
      gestures.
      
    Attributes
    ----------
    - None
    
    Methods
    -------
    - extract_image()
    - convert_hsv()
    - remove_noise()
    - remove_background()
    - convert_binary()
    - detect_position()
    - recognize_gestures()
    - detect_pointer()
    - begin()
    - show_image()
    '''
    
    def __init__(self):
      
        '''
        Description
        -----------
        - This is a Constructor. This function is executed as soon as 
          the class object is made or initialized.
        '''
        
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
      
        '''
        Description
        -----------
        - Captures the video frame and then saves it as image in a class variable
          called self.image.
        
        Parameters
        ----------
        - None
        '''
        
        _, self.image = self.cap.read()

    def convert_hsv(self):
      
        '''
        Description
        -----------
        - Converts the image from BGR Colorspace to HSV Colorspace.
        
        Parameters
        ----------
        - None
        
        Returns
        -------
        - None
        '''
        
        self.hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

    def remove_noise(self):
      
        '''
        Description
        -----------
        - Applies the median filter for removing noise from the 
          Image.
        
        Parameters
        ----------
        - None
        
        Returns
        -------
        - None
        '''
        
        self.hsv = cv2.medianBlur(self.hsv, 3)

    def remove_background(self):
      
        '''
        Description
        -----------
        - Removes the background using bitwise_and function of opencv and 
          only keeps the coloured object in the image.
        
        Parameters
        ----------
        - None
        
        Returns
        -------
        - None
        '''
        
        self.output = cv2.bitwise_and(self.image, self.image, mask = self.binary)

    def convert_binary(self):
      
        '''
        Description
        -----------
        - Converts the HSV colour space image to binary format.
        
        Parameters
        ----------
        - None
        
        Returns
        -------
        - None
        '''
        
        self.binary = cv2.inRange(self.hsv, self.min, self.max)

    def detect_position(self):
      
        '''
        Description
        -----------
        - Detects the position of controller or coloured object in 
          the image in (x,y) cordinates.
        
        Parameters
        ----------
        - None
        
        Returns
        -------
        - None
        '''
        
        self.moment = cv2.moments(self.binary)
        
        self.CX = int(self.moment["m10"]/self.moment["m00"])
        self.CY = int(self.moment["m01"]/self.moment["m00"])

        cv2.circle(self.output, (self.CX,self.CY), 3, (255,0,0), -1)

    def recognize_gesture(self):
        '''
        Description
        -----------
        - Converts the position of the controller obtained into 
          Gestures. For example - UP means when self.CY < 120
        
        Parameters
        ----------
        - None
        
        Returns
        -------
        - None
        '''

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
      
        '''
        Description
        -----------
        - Draws a red coloured rectangle over detected controller.
        
        Parameters
        ----------
        - None
        
        Returns
        -------
        - None
        '''
        
        contours, _ = cv2.findContours(self.binary.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour = max(contours, key = cv2.contourArea)
        x, y , w, h = cv2.boundingRect(contour)
        cv2.rectangle(self.image, (x,y), (x+w, y+h), (0,0,255),2)

    def begin(self):
      
        '''
        Description
        -----------
        - This is like the main function of this class. When called,
          you can start playing the game using hand gestures.
        
        Parameters
        ----------
        - None
        
        Returns
        -------
        - None
        '''

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
      
        '''
        Description
        -----------
        - Displays the output image on the terminal. Calling this 
          function is optional. Call it if you want to check if the 
          output is correct.
        
        Parameters
        ----------
        - None
        
        Returns
        -------
        - None
        '''
        
        cv2.imshow("Output Image", self.image)           

    def __del__(self):
        print("Object deleted")

def main():
  
    '''
    Main Function
    '''

    #Make the Class object.
    recognizer = GestureRecognizer()

    #Start detecting Gestures.
    recognizer.begin()    


if __name__ == '__main__':
    main()

