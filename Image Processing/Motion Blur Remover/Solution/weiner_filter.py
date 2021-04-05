import cv2
import numpy as np
from numpy.fft import *


class WeinerFilter(object):

    def __init__(self):
        self.image_path = "C:/Users/Admin/Desktop/Computer Vision/Motion Blur Removal/Images/selfie.jpg"
        
        self.image = None
        self.kernel = None
        self.deblurred_image = None
        self.padded_image =  None
        self.SB = None
        self.SG = None
        self.SR = None

        self.alpha = 2
        self.beta = 10
        self.gamma = 2500

        self.filter_height = 30
        self.filter_width = 30
        self.axis = (0,15)
        self.theta = 0

    def get_image(self):
        self.image = cv2.imread(self.image_path, 1)

    def resize_image(self):
        shape = self.output_image.shape
        h,w = shape[0], shape[1]
        aspect_ratio = w/h
        w = 730
        h = int(w/aspect_ratio)
        self.output_image = cv2.resize(self.output_image, (w,h))
        self.image = cv2.resize(self.image, (w,h))
        return self.output_image, self.image

    def blur_image(self):
        blur_kernel = np.zeros((100,100))
        blur_kernel[:,int((100 - 1)/2)] = np.ones(100)
        blur_kernel /= 100
        blurred_image = cv2.filter2D(self.image, -1, blur_kernel)
        return blurred_image

    def make_kernel(self):
        self.kernel = np.zeros((self.filter_height, self.filter_width))
        y,x = int(self.filter_height /2), int(self.filter_width / 2)
        self.kernel = cv2.ellipse(self.kernel, (y,x), self.axis, self.theta, 0, 360,
                                  255, cv2.FILLED)
        sum_h = cv2.sumElems(self.kernel)[0]
        self.kernel = self.kernel / sum_h

    def change_contrast(self):
        self.image = cv2.convertScaleAbs(self.image, alpha=self.alpha,
                                         beta=self.beta)

    def pad_image(self):
        orig_img = self.image.copy()
        c_y, c_x = orig_img.shape[:2]
        pad_y, pad_x = int(self.image.shape[0] - c_y), int(self.image.shape[1] - c_x)
        self.padded_image = np.pad(orig_img, ((0,pad_y), (0,pad_x),(0,0)), constant_values = (255))
        

    def calculate_power_spectral_density(self):
        
        self.SB = (np.absolute(fftshift(fft2(self.padded_image[...,0])))**2)/self.gamma
        self.SG = (np.absolute(fftshift(fft2(self.padded_image[...,1])))**2)/self.gamma
        self.SR = (np.absolute(fftshift(fft2(self.padded_image[...,2])))**2)/self.gamma
        return self.SB, self.SG, self.SR

    def get_power_spectral_density(self):
        
        self.S = self.calculate_power_spectral_density()
        

    def deblur_image(self,img,kernel,psd):
        kernel /= np.sum(kernel)
        dummy = fft2(np.copy(img))
        kernel = fft2(kernel, s = np.array(psd.shape))
        x = (np.abs(kernel)**2)*psd
        m,n = x.shape

        for i in range(m):
            for j in range(n):
                if int(x[i][j]) == 0:
                    x[i][j] = 1

        kernel = (np.conj(kernel)*psd)/x
        dummy = dummy*kernel
        self.deblurred_image = np.abs(ifft2(dummy))
        return self.deblurred_image
    

    def clean_image(self):
        self.output_image = cv2.fastNlMeansDenoisingColored(self.output_image,None,10,7,3)
        return self.output_image

    def apply_weiner_filter(self):
        
        self.output_image = np.zeros(self.image.shape)
        
        self.output_image[...,0] = self.deblur_image(self.image[...,0],self.kernel,self.S[0])
        self.output_image[...,1] = self.deblur_image(self.image[...,1],self.kernel,self.S[1])
        self.output_image[...,2] = self.deblur_image(self.image[...,2],self.kernel,self.S[2])


    def remove_ringing_effect(self):
        
        self.output_image = cv2.normalize(self.output_image,None, alpha = 0,beta=255,
                                             norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_8U)
        
        #self.output_image = cv2.medianBlur(self.output_image, 3)
        #self.output_image= cv2.bilateralFilter(self.output_image, 15, 3, 3)
        self.output_image = cv2.convertScaleAbs(self.output_image, alpha=2.5, beta=3)
        
        return self.output_image


def main():
    
    #Make class object
    Filter = WeinerFilter()

    #Get the blurred Image.
    Filter.get_image()

    #Blur the image if it is not blurred.
    #image = Filter.blur_image()
    
    #Change the contrast of the Image.
    #Filter.change_contrast()

    #Zero Pad the Image.
    Filter.pad_image()

    #Calculate Power Spectral Density(PSD).
    Filter.get_power_spectral_density()

    #Make the Weiner Filter Kernel.
    Filter.make_kernel()

    #Get the Deblurred Image.
    Filter.apply_weiner_filter()

    #Remove the ringing effect and return the Image.
    image = Filter.remove_ringing_effect()
    
    #Clean the image
    #image = Filter.clean_image()

    #Resize the image
    #image_1,image_2 = Filter.resize_image()


    #cv2.imwrite("dog.jpg",image)
    cv2.imshow("Restored Image", image)
    #cv2.imshow("Blurred Image", image_2)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    


if __name__ == '__main__':
    main()

