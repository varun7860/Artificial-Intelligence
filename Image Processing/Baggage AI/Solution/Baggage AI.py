'''
Baggage AI module
'''

#import the necessary libraries
import cv2
import os
import numpy as np
from PIL import Image

class Baggage(object):
    'Baggage Class'
    def __init__(self):
        self.background_images = []
        self.threat_images = []
        self.output_images = []
        self.mask_images = []
        self.masks = []
        
        self.file_path_1 = "C:/Users/Admin/Desktop/Computer Vision/BaggageAI_CV_Hiring_Assignment/background_images"
        self.file_path_2 = "C:/Users/Admin/Desktop/Computer Vision/BaggageAI_CV_Hiring_Assignment/threat_images"
        self.file_path_3 = "C:/Users/Admin/Desktop/Computer Vision/BaggageAI_CV_Hiring_Assignment/output_images"
        self.file_path_4 = "C:/Users/Admin/Desktop/Computer Vision/BaggageAI_CV_Hiring_Assignment/masks"

    def get_threat_image(self, image_name):
        image = cv2.imread(self.file_path_2 + '/' + image_name)
        return image

    def get_background_image(self, image_name):
        image = cv2.imread(self.file_path_1 + '/' + image_name)
        return image

    def get_mask_images(self):
        return self.masks
    
    def get_background_images(self):
        for filename in os.listdir(self.file_path_1):
            image = Image.open(os.path.join(self.file_path_1, filename))
            image_copy = image
            if image_copy is not None:
                self.background_images.append(image_copy)
        return self.background_images

    def get_threat_images(self):
        for filename in os.listdir(self.file_path_2):
            image = Image.open(os.path.join(self.file_path_2, filename))
            image_copy = image
            if image_copy is not None:
                self.threat_images.append(image_copy)
        return self.threat_images

    def make_translucent(self, threat_images_list, alpha = 128):
        for i in range(len(threat_images_list)):
            threat_images_list[i].putalpha(alpha)

        print("All Images are made translucent")
        return threat_images_list

    def scale_images(self, threat_images_list):
        for i in range(len(threat_images_list)):
            threat_images_list[i] = threat_images_list[i].resize((300,400))

        print("All Images are scaled down.")
        return threat_images_list

    def remove_background(self):
        
        for filename in os.listdir(self.file_path_2):
            image = cv2.imread(os.path.join(self.file_path_2, filename),1)
            image_copy = image.copy()
            self.mask_images.append(image_copy)

        for i in range(len(self.mask_images)):
            gray_image = cv2.cvtColor(self.mask_images[i],cv2.COLOR_BGR2GRAY)
            ret,thresh = cv2.threshold(gray_image, 240,255,cv2.THRESH_BINARY_INV)
            #contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            
            #mask = np.zeros(self.mask_images[i].shape[:2], np.uint8)
            #cv2.drawContours(mask, contours[0], -1, 255, -1)
            
            #final_image = cv2.bitwise_and(self.mask_images[i], self.mask_images[i], mask = mask)
            thresh = Image.fromarray(thresh)
            print(type(thresh))
            os.chdir(self.file_path_4)
            self.masks.append(thresh)
            thresh.save(str(i)+ '.jpg')

    def rotate_images(self, threat_images_list, angle):
        for i in range(len(threat_images_list)):
            threat_images_list[i] = threat_images_list[i].rotate(angle, expand = True)

        print("All Images are rotated by 45 degrees.")

        return threat_images_list
    
    def merge_images(self, back_images_list, threat_images_list, masks_list):
        repeat = len(threat_images_list)

        for i in range(repeat):
            image_1 = threat_images_list[i]
            image_2 = back_images_list[i]
            mask = masks_list[i].resize(image_1.size)

            if i == 0 or i == 1 or i == 2 or i == 4:
                image_2.paste(image_1, (50,50), mask)

            if i == 3:
                image_2.paste(image_1, (500,250), mask)

            self.output_images.append(image_2)

        print("Images merged successfully")

        return self.output_images
        
        
def main():

    AI = Baggage()

    AI.remove_background()

    mask_images = AI.get_mask_images()

    mask_images = AI.rotate_images(mask_images, 45)

    threat_images = AI.get_threat_images()

    background_images = AI.get_background_images()

    threat_images = AI.rotate_images(threat_images, 45)

    threat_images = AI.scale_images(threat_images)

    threat_images = AI.make_translucent(threat_images)

    final_images = AI.merge_images(background_images, threat_images, mask_images)

    final_images[0].show()
    

if __name__ == '__main__':
    main()
