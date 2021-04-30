# Motion Blur Remover Using Image Processing
<img align = "center" width = "600" height = "330" src = "https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/Motion%20Blur%20Remover/Assets/Image%20Deblurring.jpg">
  
In this task the goal is to remove Blur from an image using image processing concepts.Your program should remove the
blur from the image to such an extent that the viewer should be able to see the details clearly in the image. Your program
take an input blurred image and output an image which is deblurred. Following things should be achieved when this task is
completed:

1. `Completely deblurred output image.`
2. `Output image should be displayed on the screen.`
3. `The program should be general. This means that it should work for any image which are blurred equally.`
4. `The code should neatly commented and linted. Pylint can be used to lint the code.`
5. `The program should be fast and accurate.`
6. `Ringing Effect obtained after deblurring should be as minimum as possible.`

## What is Motion Blur?
<img align = "center" width = "300" height = "250" src = "https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/Motion%20Blur%20Remover/Assets/Blurred%20Image.gif">

Motion Blur is a degradation of image caused due to the moment of the object relative to the sensor in the camera when the
shutter is open. Motion Blur can also be caused due to the movement of camera as well. For example if you take a picture while
moving your camera the resultant image will be motion blurred. There are 3 types of blur:

- `Horizontal Blur` : Linear motion is horizontal direction
- `Vertical Blur` : Linear motion in vertical direction
- `Circular Blur` : Linear motion is circular direction

The motion blur can be completely removed by process called deconvolution in image processing. Based on the type of of motion
blur, the kernel used for deconvolution will be different for each blur. For example, for horizontal blur the horizontal deconvolution
kernel will be used. Depending on the extent of motion blur the size of kernel will increase or decrease. More information about motion
blur can be found [here](https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/AV0506/s0198594.pdf)

## Point Spread Function (PSF)
A Point Spread Function is a function which is convolved with a sharp image to produce the blurred Image. As in our task we don't have
sharp image but have blurred image, so we need to compute the point PSF of the image to obtain the sharp image. Mathematically the equation
can be written as:

`B = PSF * S`

Where,
B = Blurred Image.
PSF = point spread function.
S = Sharp Image.

So to compute sharp image the formula will become:

`S = PSF/B`

## Algorithm to deblur an Image

<BR>
  
<img align = "center" width = "400" height = "210" src = "https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/Motion%20Blur%20Remover/Assets/Algorithm.jpg">

<BR>
  
Whichever filter you use , the algorithm for deblurring an image will always remain the same. Follow these steps to transform the blurred
image to an estimate of its ideal form:

1. `Find the type of motion blur (vertical, horizontal or circular) in the image.`
2. `Change the contrast of the image if necessary`
3. `Zero pad the image before applying Fourier Transform.`
4. `Obtain the point spread function (PSF) or power spectral density (PSD)`
5. `Make the deconvolution kernel using PSF obtained in step 4`
6. `Apply the Filter (I applied Weiner Filter)`
7. `Remove the ringing effect noise after the deblurred image is obtained.`
8. `Resize the image if necessary.`
9. `Display and save the deblurred image in the necessary folder.`

## Filters used for deblurring

1. [Weiner Filter (If noise is present)](https://en.wikipedia.org/wiki/Wiener_filter#:~:text=In%20signal%20processing%2C%20the%20Wiener,noise%20spectra%2C%20and%20additive%20noise.)
2. [Inverse Filter (If image is noiseless)](http://www.owlnet.rice.edu/~elec539/Projects99/BACH/proj2/inverse.html)


## Learning Modules

<img align="center" width="500" height="334" src="https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/Dino%20T-Rex%20Game%20Using%20Gesture%20Recognition/Assets/Learning%20Modules.jpg">

To built the project you need to get familiar with the learning modules given below. You can use ideas from these modules but don't copy paste the code.
Learn them step by step in the sequence given below:

1. [Computer Vision](https://tryolabs.com/resources/introductory-guide-computer-vision/)
2. [Python Programming](https://www.w3schools.com/python/)
3. [Weiner Deconvolution](https://pyautogui.readthedocs.io/en/latest/)
4. [Numpy Library](https://www.w3schools.com/python/numpy/numpy_intro.asp)
5. [Open CV library](https://www.geeksforgeeks.org/opencv-python-tutorial/)
6. [Image processing](https://en.wikipedia.org/wiki/Digital_image_processing)
7. [Kernel](https://en.wikipedia.org/wiki/Kernel_(image_processing))

## Expected Output
[![alt text][1]][2]

[1]: https://github.com/varun7860/Artificial-Intelligence/blob/main/Image%20Processing/Dino%20T-Rex%20Game%20Using%20Gesture%20Recognition/Assets/Output.png
[2]: https://youtu.be/Jr3z_QA5mb0

