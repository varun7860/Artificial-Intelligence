import cv2
import numpy as np

class BoxCalculator(object):

    def __init__(self):
        
        self._image_path = "C:/Users/Admin/Desktop/Computer Vision/Count the Number of Boxes in an Image/Images/Boxes.jpg"
        self.output_path = "C:/Users/Admin/Desktop/Computer Vision/Count the Number of Boxes in an Image/Output/output.jpg"
        self._width = 600
        self._height = 600
        self.boxes = 0
        
        self.image = None
        self.gray_image = None
        self.binary_image = None
        self.border_image = None
        
        self.sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
        
    def get_image(self):
        self.image = cv2.imread(self._image_path, 1)
        self.image = cv2.resize(self.image, (self._width,self._height))
        return self.image

    def convert_binary(self, image):
        
        MIN = np.array([55, 0, 0])
        MAX = np.array([160, 255, 255])

        self.binary_image = cv2.inRange(image, MIN, MAX)
        return self.binary_image

    def remove_noise(self, image):
        blur_image = cv2.bilateralFilter(image, 13, 17, 17)
        sharpen_image = cv2.filter2D(blur_image, -1, self.sharpen_kernel)
        return blur_image

    def calculate_boxes(self, image):
        contours,_ = cv2.findContours(image.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018*peri, True)
            
            if len(approx) <= 9:
                x,y,w,h = cv2.boundingRect(approx)
                if w>11 and h>12 and h<27 and w<50:
                   self.border_image = cv2.rectangle(self.image, (x,y), (x+w, y+h), (0,0,0),2)
                   self.boxes += 1
        print("There are"+ " " + str(self.boxes) + " " + "Boxes present in the image")
        return self.border_image

    def save_output(self, image):
        cv2.imwrite(self.output_path, image)
        
    def show_image(self, image):
        cv2.imshow("Output", image)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

def main():

    #Make the Object
    counter = BoxCalculator()

    #Get the image with boxes.
    image = counter.get_image()

    #Remove the noise from the image.
    image = counter.remove_noise(image)

    #Convert image to HSV Space.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #Perform image thresholding.
    image = counter.convert_binary(image)

    #Calculate the number of boxes present in the image.
    image = counter.calculate_boxes(image)

    #Display the output.
    counter.show_image(image)
    

if __name__ == "__main__":
    main()
